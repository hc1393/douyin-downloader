# -*- coding: utf-8 -*-
"""
策略信号模块 — 生成买卖信号

支持策略:
  - MA 均线交叉 (金叉/死叉)
  - MACD 交叉信号
  - RSI 超买超卖
  - 布林带突破
  - KDJ 交叉
  - 组合策略 (多指标投票)
"""

import pandas as pd
import numpy as np


def signal_ma_cross(df: pd.DataFrame, fast: str = "ma5",
                    slow: str = "ma20") -> pd.Series:
    """
    均线交叉信号

    Args:
        df: 含 MA 列的数据
        fast: 快线列名
        slow: 慢线列名

    Returns:
        信号序列: 1=买入, -1=卖出, 0=无信号
    """
    if fast not in df.columns or slow not in df.columns:
        return pd.Series(0, index=df.index)

    signal = pd.Series(0, index=df.index)
    cross_up = (df[fast] > df[slow]) & (df[fast].shift(1) <= df[slow].shift(1))
    cross_down = (df[fast] < df[slow]) & (df[fast].shift(1) >= df[slow].shift(1))
    signal[cross_up] = 1
    signal[cross_down] = -1
    return signal


def signal_macd(df: pd.DataFrame) -> pd.Series:
    """
    MACD 交叉信号

    Returns:
        信号序列: 1=金叉买入, -1=死叉卖出, 0=无信号
    """
    if "dif" not in df.columns or "dea" not in df.columns:
        return pd.Series(0, index=df.index)

    signal = pd.Series(0, index=df.index)
    cross_up = (df["dif"] > df["dea"]) & (df["dif"].shift(1) <= df["dea"].shift(1))
    cross_down = (df["dif"] < df["dea"]) & (df["dif"].shift(1) >= df["dea"].shift(1))
    signal[cross_up] = 1
    signal[cross_down] = -1
    return signal


def signal_rsi(df: pd.DataFrame, oversold: float = 30,
               overbought: float = 70) -> pd.Series:
    """
    RSI 超买超卖信号

    Args:
        oversold: 超卖阈值 (默认30)
        overbought: 超买阈值 (默认70)

    Returns:
        信号序列: 1=超卖买入, -1=超买卖出, 0=无信号
    """
    if "rsi" not in df.columns:
        return pd.Series(0, index=df.index)

    signal = pd.Series(0, index=df.index)
    # 从超卖区向上突破
    cross_up = (df["rsi"] > oversold) & (df["rsi"].shift(1) <= oversold)
    # 从超买区向下突破
    cross_down = (df["rsi"] < overbought) & (df["rsi"].shift(1) >= overbought)
    signal[cross_up] = 1
    signal[cross_down] = -1
    return signal


def signal_bollinger(df: pd.DataFrame) -> pd.Series:
    """
    布林带信号

    Returns:
        信号序列: 1=触及下轨买入, -1=触及上轨卖出, 0=无信号
    """
    if "boll_upper" not in df.columns or "boll_lower" not in df.columns:
        return pd.Series(0, index=df.index)

    signal = pd.Series(0, index=df.index)
    # 价格从下轨下方回到上方
    buy = (df["close"] > df["boll_lower"]) & (df["close"].shift(1) <= df["boll_lower"].shift(1))
    # 价格从上轨上方回到下方
    sell = (df["close"] < df["boll_upper"]) & (df["close"].shift(1) >= df["boll_upper"].shift(1))
    signal[buy] = 1
    signal[sell] = -1
    return signal


def signal_kdj(df: pd.DataFrame) -> pd.Series:
    """
    KDJ 交叉信号

    Returns:
        信号序列: 1=金叉买入, -1=死叉卖出, 0=无信号
    """
    if "k" not in df.columns or "d" not in df.columns:
        return pd.Series(0, index=df.index)

    signal = pd.Series(0, index=df.index)
    cross_up = (df["k"] > df["d"]) & (df["k"].shift(1) <= df["d"].shift(1))
    cross_down = (df["k"] < df["d"]) & (df["k"].shift(1) >= df["d"].shift(1))
    signal[cross_up] = 1
    signal[cross_down] = -1
    return signal


def signal_combined(df: pd.DataFrame, strategies: list = None,
                    min_votes: int = 2) -> pd.Series:
    """
    组合策略 — 多指标投票

    Args:
        df: 含所有指标的数据
        strategies: 策略列表，默认 [ma_cross, macd, rsi, kdj]
        min_votes: 最少投票数才触发信号 (默认2)

    Returns:
        信号序列: 1=多数看多, -1=多数看空, 0=无共识
    """
    if strategies is None:
        strategies = [
            signal_ma_cross(df),
            signal_macd(df),
            signal_rsi(df),
            signal_kdj(df),
        ]

    votes = pd.DataFrame({"s" + str(i): s for i, s in enumerate(strategies)})

    buy_votes = (votes > 0).sum(axis=1)
    sell_votes = (votes < 0).sum(axis=1)

    signal = pd.Series(0, index=df.index)
    signal[buy_votes >= min_votes] = 1
    signal[sell_votes >= min_votes] = -1
    return signal


# 策略注册表
STRATEGIES = {
    "ma_cross": signal_ma_cross,
    "macd": signal_macd,
    "rsi": signal_rsi,
    "bollinger": signal_bollinger,
    "kdj": signal_kdj,
    "combined": signal_combined,
}


def generate_signals(df: pd.DataFrame, strategy: str = "combined",
                     **kwargs) -> pd.Series:
    """
    生成交易信号

    Args:
        df: 含技术指标的数据
        strategy: 策略名称
        **kwargs: 策略参数

    Returns:
        信号序列
    """
    if strategy not in STRATEGIES:
        raise ValueError(f"未知策略: {strategy}，可选: {list(STRATEGIES.keys())}")

    func = STRATEGIES[strategy]
    return func(df, **kwargs)


def signal_summary(signal: pd.Series) -> dict:
    """
    信号统计摘要

    Returns:
        {'total_signals': N, 'buy_signals': N, 'sell_signals': N, ...}
    """
    buy_count = (signal == 1).sum()
    sell_count = (signal == -1).sum()
    return {
        "总信号数": int(buy_count + sell_count),
        "买入信号": int(buy_count),
        "卖出信号": int(sell_count),
        "信号频率": f"{(buy_count + sell_count) / len(signal) * 100:.2f}%",
    }
