# -*- coding: utf-8 -*-
"""技术分析模块 — 均线、MACD、RSI、KDJ、布林带、ATR等"""

import pandas as pd
import numpy as np
from config.settings import (
    DEFAULT_MA_PERIODS, DEFAULT_RSI_PERIOD,
    DEFAULT_MACD_FAST, DEFAULT_MACD_SLOW, DEFAULT_MACD_SIGNAL,
    DEFAULT_BOLL_PERIOD, DEFAULT_BOLL_STD, DEFAULT_ATR_PERIOD,
    DEFAULT_KDJ_PERIOD,
)


def ma(df: pd.DataFrame, periods: list = None, column: str = "close") -> pd.DataFrame:
    """
    计算移动平均线

    Args:
        df: 行情数据
        periods: 均线周期列表，默认 [5, 10, 20, 60, 120, 250]
        column: 计算列名

    Returns:
        原始数据附加 MA 列
    """
    if periods is None:
        periods = DEFAULT_MA_PERIODS
    result = df.copy()
    for p in periods:
        result[f"ma{p}"] = result[column].rolling(window=p, min_periods=1).mean()
    return result


def ema(series: pd.Series, period: int) -> pd.Series:
    """指数移动平均"""
    return series.ewm(span=period, adjust=False).mean()


def macd(df: pd.DataFrame, fast: int = None, slow: int = None,
         signal: int = None) -> pd.DataFrame:
    """
    计算 MACD 指标

    Returns:
        附加 dif, dea, macd 三列
    """
    if fast is None:
        fast = DEFAULT_MACD_FAST
    if slow is None:
        slow = DEFAULT_MACD_SLOW
    if signal is None:
        signal = DEFAULT_MACD_SIGNAL

    result = df.copy()
    close = result["close"]
    ema_fast = ema(close, fast)
    ema_slow = ema(close, slow)

    result["dif"] = ema_fast - ema_slow
    result["dea"] = ema(result["dif"], signal)
    result["macd"] = 2 * (result["dif"] - result["dea"])
    return result


def rsi(df: pd.DataFrame, period: int = None) -> pd.DataFrame:
    """
    计算 RSI 相对强弱指标

    Returns:
        附加 rsi 列
    """
    if period is None:
        period = DEFAULT_RSI_PERIOD

    result = df.copy()
    delta = result["close"].diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.ewm(alpha=1 / period, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    result["rsi"] = 100 - (100 / (1 + rs))
    return result


def kdj(df: pd.DataFrame, period: int = None) -> pd.DataFrame:
    """
    计算 KDJ 指标

    Returns:
        附加 k, d, j 三列
    """
    if period is None:
        period = DEFAULT_KDJ_PERIOD

    result = df.copy()
    low_min = result["low"].rolling(window=period, min_periods=1).min()
    high_max = result["high"].rolling(window=period, min_periods=1).max()

    rsv = (result["close"] - low_min) / (high_max - low_min).replace(0, np.nan) * 100

    result["k"] = rsv.ewm(alpha=1 / 3, adjust=False).mean()
    result["d"] = result["k"].ewm(alpha=1 / 3, adjust=False).mean()
    result["j"] = 3 * result["k"] - 2 * result["d"]
    return result


def bollinger(df: pd.DataFrame, period: int = None,
              std_dev: float = None) -> pd.DataFrame:
    """
    计算布林带

    Returns:
        附加 boll_mid, boll_upper, boll_lower 三列
    """
    if period is None:
        period = DEFAULT_BOLL_PERIOD
    if std_dev is None:
        std_dev = DEFAULT_BOLL_STD

    result = df.copy()
    result["boll_mid"] = result["close"].rolling(window=period, min_periods=1).mean()
    std = result["close"].rolling(window=period, min_periods=1).std()
    result["boll_upper"] = result["boll_mid"] + std_dev * std
    result["boll_lower"] = result["boll_mid"] - std_dev * std
    return result


def atr(df: pd.DataFrame, period: int = None) -> pd.DataFrame:
    """
    计算 ATR 平均真实波幅

    Returns:
        附加 atr 列
    """
    if period is None:
        period = DEFAULT_ATR_PERIOD

    result = df.copy()
    high = result["high"]
    low = result["low"]
    prev_close = result["close"].shift(1)

    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs(),
    ], axis=1).max(axis=1)

    result["atr"] = tr.ewm(span=period, adjust=False).mean()
    return result


def volume_ratio(df: pd.DataFrame, period: int = 5) -> pd.DataFrame:
    """
    计算量比（当日成交量 / 过去N日平均成交量）

    Returns:
        附加 volume_ratio 列
    """
    result = df.copy()
    avg_vol = result["volume"].rolling(window=period, min_periods=1).mean()
    result["volume_ratio"] = result["volume"] / avg_vol.replace(0, np.nan)
    return result


def support_resistance(df: pd.DataFrame, window: int = 20,
                       num_levels: int = 3) -> dict:
    """
    识别支撑位和阻力位（基于局部极值）

    Returns:
        {'support': [价格列表], 'resistance': [价格列表]}
    """
    close = df["close"].values
    highs = []
    lows = []

    for i in range(window, len(close) - window):
        if close[i] == max(close[i - window:i + window + 1]):
            highs.append(close[i])
        if close[i] == min(close[i - window:i + window + 1]):
            lows.append(close[i])

    # 聚类合并相近的价位
    def cluster(prices, threshold=0.02):
        if not prices:
            return []
        prices = sorted(prices)
        clusters = [[prices[0]]]
        for p in prices[1:]:
            if (p - clusters[-1][-1]) / clusters[-1][-1] < threshold:
                clusters[-1].append(p)
            else:
                clusters.append([p])
        return [round(np.mean(c), 2) for c in clusters]

    resistance = cluster(highs)[-num_levels:] if highs else []
    support = cluster(lows)[:num_levels] if lows else []

    return {"support": support, "resistance": resistance}


def apply_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """一次性计算所有技术指标"""
    result = df.copy()
    result = ma(result)
    result = macd(result)
    result = rsi(result)
    result = kdj(result)
    result = bollinger(result)
    result = atr(result)
    result = volume_ratio(result)
    return result
