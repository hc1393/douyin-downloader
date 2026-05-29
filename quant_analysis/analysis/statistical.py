# -*- coding: utf-8 -*-
"""统计分析模块 — 收益率、波动率、回撤、相关性等"""

import pandas as pd
import numpy as np
from tabulate import tabulate


def daily_returns(df: pd.DataFrame) -> pd.Series:
    """计算日收益率"""
    return df["close"].pct_change()


def log_returns(df: pd.DataFrame) -> pd.Series:
    """计算对数收益率"""
    return np.log(df["close"] / df["close"].shift(1))


def cumulative_returns(df: pd.DataFrame) -> pd.Series:
    """计算累计收益率"""
    return (1 + daily_returns(df)).cumprod() - 1


def annualized_return(df: pd.DataFrame, trading_days: int = 250) -> float:
    """计算年化收益率"""
    total_return = (df["close"].iloc[-1] / df["close"].iloc[0]) - 1
    n_days = len(df)
    return (1 + total_return) ** (trading_days / n_days) - 1


def annualized_volatility(df: pd.DataFrame, trading_days: int = 250) -> float:
    """计算年化波动率"""
    return daily_returns(df).std() * np.sqrt(trading_days)


def sharpe_ratio(df: pd.DataFrame, risk_free_rate: float = 0.03,
                 trading_days: int = 250) -> float:
    """计算夏普比率"""
    ann_ret = annualized_return(df, trading_days)
    ann_vol = annualized_volatility(df, trading_days)
    if ann_vol == 0:
        return 0
    return (ann_ret - risk_free_rate) / ann_vol


def max_drawdown(df: pd.DataFrame) -> dict:
    """
    计算最大回撤

    Returns:
        {'max_drawdown': 最大回撤比例, 'peak_date': 高点日期, 'trough_date': 低点日期}
    """
    close = df["close"]
    peak = close.expanding().max()
    drawdown = (close - peak) / peak

    max_dd = drawdown.min()
    trough_idx = drawdown.idxmin()
    peak_idx = close.loc[:trough_idx].idxmax()

    return {
        "max_drawdown": abs(max_dd),
        "peak_date": str(peak_idx.date()) if hasattr(peak_idx, 'date') else str(peak_idx),
        "peak_price": close.loc[peak_idx],
        "trough_date": str(trough_idx.date()) if hasattr(trough_idx, 'date') else str(trough_idx),
        "trough_price": close.loc[trough_idx],
    }


def drawdown_series(df: pd.DataFrame) -> pd.Series:
    """计算回撤时间序列"""
    close = df["close"]
    peak = close.expanding().max()
    return (close - peak) / peak


def calmar_ratio(df: pd.DataFrame, trading_days: int = 250) -> float:
    """计算卡尔玛比率（年化收益 / 最大回撤）"""
    mdd = max_drawdown(df)["max_drawdown"]
    if mdd == 0:
        return 0
    return annualized_return(df, trading_days) / mdd


def volatility_clustering(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """
    波动率聚类分析

    Returns:
        附加 vol_20, vol_60, vol_ratio 列
    """
    result = df.copy()
    ret = daily_returns(result)
    result["vol_20"] = ret.rolling(window=window).std() * np.sqrt(250)
    result["vol_60"] = ret.rolling(window=60).std() * np.sqrt(250)
    result["vol_ratio"] = result["vol_20"] / result["vol_60"].replace(0, np.nan)
    return result


def correlation_matrix(symbols_data: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    计算多只股票的相关性矩阵

    Args:
        symbols_data: {'股票名': DataFrame, ...}

    Returns:
        相关性矩阵
    """
    returns = {}
    for name, df in symbols_data.items():
        returns[name] = daily_returns(df)
    return pd.DataFrame(returns).corr()


def rolling_correlation(df1: pd.DataFrame, df2: pd.DataFrame,
                        window: int = 60) -> pd.Series:
    """计算滚动相关性"""
    r1 = daily_returns(df1)
    r2 = daily_returns(df2)
    return r1.rolling(window=window).corr(r2)


def descriptive_stats(df: pd.DataFrame) -> dict:
    """
    描述性统计

    Returns:
        包含各项统计数据的字典
    """
    ret = daily_returns(df).dropna()
    return {
        "起始价格": df["close"].iloc[0],
        "最新价格": df["close"].iloc[-1],
        "最高价": df["high"].max(),
        "最低价": df["low"].min(),
        "总收益率": f"{(df['close'].iloc[-1] / df['close'].iloc[0] - 1) * 100:.2f}%",
        "年化收益率": f"{annualized_return(df) * 100:.2f}%",
        "年化波动率": f"{annualized_volatility(df) * 100:.2f}%",
        "夏普比率": f"{sharpe_ratio(df):.2f}",
        "最大回撤": f"{max_drawdown(df)['max_drawdown'] * 100:.2f}%",
        "卡尔玛比率": f"{calmar_ratio(df):.2f}",
        "日均收益率": f"{ret.mean() * 100:.4f}%",
        "日收益率标准差": f"{ret.std() * 100:.4f}%",
        "偏度": f"{ret.skew():.4f}",
        "峰度": f"{ret.kurtosis():.4f}",
        "正收益天数": int((ret > 0).sum()),
        "负收益天数": int((ret < 0).sum()),
        "最大单日涨幅": f"{ret.max() * 100:.2f}%",
        "最大单日跌幅": f"{ret.min() * 100:.2f}%",
    }


def print_stats(df: pd.DataFrame, symbol: str = ""):
    """打印格式化的统计报告"""
    stats = descriptive_stats(df)
    print(f"\n{'=' * 50}")
    print(f"  统计分析报告 {symbol}")
    print(f"{'=' * 50}")
    for k, v in stats.items():
        print(f"  {k:　<10s}  {v}")
    print(f"{'=' * 50}\n")
