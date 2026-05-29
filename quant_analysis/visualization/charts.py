# -*- coding: utf-8 -*-
"""可视化模块 — K线图、指标图、回撤图、相关性热力图等"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")  # 非交互式后端
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.gridspec import GridSpec
import mplfinance as mpf
import seaborn as sns

from config.settings import OUTPUT_DIR

# 中文字体设置
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


def plot_candlestick(df: pd.DataFrame, symbol: str = "", title: str = None,
                     last_n: int = 120, save: bool = True) -> str:
    """
    绘制K线图（含成交量和均线）

    Args:
        df: 行情数据，需要 open/high/low/close/volume 列
        symbol: 股票代码
        title: 图表标题
        last_n: 显示最近N根K线
        save: 是否保存图片

    Returns:
        保存的图片路径
    """
    data = df.tail(last_n).copy()
    if title is None:
        title = f"{symbol} K线图"

    # 计算均线
    ma5 = data["close"].rolling(5).mean()
    ma10 = data["close"].rolling(10).mean()
    ma20 = data["close"].rolling(20).mean()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10), height_ratios=[3, 1],
                                    gridspec_kw={"hspace": 0.1})

    # K线
    up = data[data["close"] >= data["open"]]
    down = data[data["close"] < data["open"]]

    ax1.bar(up.index, up["close"] - up["open"], bottom=up["open"],
            width=0.8, color="red", alpha=0.9)
    ax1.bar(up.index, up["high"] - up["close"], bottom=up["close"],
            width=0.1, color="red")
    ax1.bar(up.index, up["low"] - up["open"], bottom=up["open"],
            width=0.1, color="red")

    ax1.bar(down.index, down["close"] - down["open"], bottom=down["open"],
            width=0.8, color="green", alpha=0.9)
    ax1.bar(down.index, down["high"] - down["open"], bottom=down["open"],
            width=0.1, color="green")
    ax1.bar(down.index, down["low"] - down["close"], bottom=down["close"],
            width=0.1, color="green")

    # 均线
    ax1.plot(data.index, ma5, label="MA5", linewidth=1, alpha=0.8)
    ax1.plot(data.index, ma10, label="MA10", linewidth=1, alpha=0.8)
    ax1.plot(data.index, ma20, label="MA20", linewidth=1, alpha=0.8)

    ax1.set_title(title, fontsize=16, fontweight="bold")
    ax1.legend(loc="upper left", fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_ylabel("价格")

    # 成交量
    colors = ["red" if c >= o else "green"
              for c, o in zip(data["close"], data["open"])]
    ax2.bar(data.index, data["volume"], color=colors, alpha=0.7, width=0.8)
    ax2.set_ylabel("成交量")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    if save:
        path = str(OUTPUT_DIR / f"{symbol}_candlestick.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"[图表] K线图已保存: {path}")
        return path
    else:
        plt.show()
        return ""


def plot_macd(df: pd.DataFrame, symbol: str = "", last_n: int = 120,
              save: bool = True) -> str:
    """绘制 MACD 指标图"""
    data = df.tail(last_n).copy()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 8), height_ratios=[2, 1],
                                    gridspec_kw={"hspace": 0.1})

    # 价格 + 均线
    ax1.plot(data.index, data["close"], label="收盘价", linewidth=1.2)
    if "ma5" in data.columns:
        ax1.plot(data.index, data["ma5"], label="MA5", linewidth=0.8, alpha=0.7)
    if "ma20" in data.columns:
        ax1.plot(data.index, data["ma20"], label="MA20", linewidth=0.8, alpha=0.7)
    ax1.set_title(f"{symbol} MACD", fontsize=14, fontweight="bold")
    ax1.legend(loc="upper left")
    ax1.grid(True, alpha=0.3)

    # MACD
    if "dif" in data.columns and "dea" in data.columns:
        ax2.plot(data.index, data["dif"], label="DIF", linewidth=1)
        ax2.plot(data.index, data["dea"], label="DEA", linewidth=1)
        colors = ["red" if v >= 0 else "green" for v in data["macd"]]
        ax2.bar(data.index, data["macd"], color=colors, alpha=0.6, width=0.8)
        ax2.axhline(y=0, color="gray", linewidth=0.5)
        ax2.legend(loc="upper left")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    if save:
        path = str(OUTPUT_DIR / f"{symbol}_macd.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"[图表] MACD图已保存: {path}")
        return path
    else:
        plt.show()
        return ""


def plot_rsi(df: pd.DataFrame, symbol: str = "", last_n: int = 120,
             save: bool = True) -> str:
    """绘制 RSI 指标图"""
    data = df.tail(last_n).copy()

    fig, ax = plt.subplots(figsize=(16, 5))
    ax.plot(data.index, data["rsi"], label="RSI", linewidth=1.2, color="purple")
    ax.axhline(y=70, color="red", linestyle="--", linewidth=0.8, label="超买(70)")
    ax.axhline(y=30, color="green", linestyle="--", linewidth=0.8, label="超卖(30)")
    ax.axhline(y=50, color="gray", linestyle="-", linewidth=0.5)
    ax.fill_between(data.index, 70, 100, alpha=0.1, color="red")
    ax.fill_between(data.index, 0, 30, alpha=0.1, color="green")
    ax.set_ylim(0, 100)
    ax.set_title(f"{symbol} RSI", fontsize=14, fontweight="bold")
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    if save:
        path = str(OUTPUT_DIR / f"{symbol}_rsi.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"[图表] RSI图已保存: {path}")
        return path
    else:
        plt.show()
        return ""


def plot_drawdown(df: pd.DataFrame, symbol: str = "", save: bool = True) -> str:
    """绘制回撤图"""
    from analysis.statistical import drawdown_series

    dd = drawdown_series(df)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 8), height_ratios=[2, 1],
                                    gridspec_kw={"hspace": 0.15})

    ax1.plot(df.index, df["close"], label="收盘价", linewidth=1.2)
    ax1.set_title(f"{symbol} 价格与回撤", fontsize=14, fontweight="bold")
    ax1.legend(loc="upper left")
    ax1.grid(True, alpha=0.3)

    ax2.fill_between(dd.index, dd.values, 0, color="red", alpha=0.4)
    ax2.plot(dd.index, dd.values, color="red", linewidth=0.8)
    ax2.set_ylabel("回撤")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    if save:
        path = str(OUTPUT_DIR / f"{symbol}_drawdown.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"[图表] 回撤图已保存: {path}")
        return path
    else:
        plt.show()
        return ""


def plot_correlation_heatmap(corr_matrix: pd.DataFrame, title: str = "相关性矩阵",
                             save: bool = True) -> str:
    """绘制相关性热力图"""
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="RdYlGn",
                center=0, square=True, ax=ax)
    ax.set_title(title, fontsize=14, fontweight="bold")

    plt.tight_layout()

    if save:
        path = str(OUTPUT_DIR / "correlation_heatmap.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"[图表] 相关性热力图已保存: {path}")
        return path
    else:
        plt.show()
        return ""


def plot_returns_distribution(df: pd.DataFrame, symbol: str = "",
                              save: bool = True) -> str:
    """绘制收益率分布图"""
    from analysis.statistical import daily_returns

    ret = daily_returns(df).dropna()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # 直方图
    ax1.hist(ret.values, bins=50, density=True, alpha=0.7, color="steelblue",
             edgecolor="white")
    ax1.axvline(x=ret.mean(), color="red", linestyle="--", label=f"均值: {ret.mean():.4f}")
    ax1.axvline(x=0, color="gray", linestyle="-", linewidth=0.5)
    ax1.set_title(f"{symbol} 日收益率分布", fontsize=12, fontweight="bold")
    ax1.set_xlabel("日收益率")
    ax1.set_ylabel("密度")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # QQ图
    from scipy import stats
    stats.probplot(ret.values, dist="norm", plot=ax2)
    ax2.set_title(f"{symbol} Q-Q图", fontsize=12, fontweight="bold")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    if save:
        path = str(OUTPUT_DIR / f"{symbol}_returns_dist.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"[图表] 收益率分布图已保存: {path}")
        return path
    else:
        plt.show()
        return ""


def plot_bollinger(df: pd.DataFrame, symbol: str = "", last_n: int = 120,
                   save: bool = True) -> str:
    """绘制布林带图"""
    data = df.tail(last_n).copy()

    fig, ax = plt.subplots(figsize=(16, 7))
    ax.plot(data.index, data["close"], label="收盘价", linewidth=1.2)
    ax.plot(data.index, data["boll_mid"], label="中轨", linewidth=0.8, color="orange")
    ax.plot(data.index, data["boll_upper"], label="上轨", linewidth=0.8,
            color="red", linestyle="--")
    ax.plot(data.index, data["boll_lower"], label="下轨", linewidth=0.8,
            color="green", linestyle="--")
    ax.fill_between(data.index, data["boll_upper"], data["boll_lower"],
                    alpha=0.1, color="gray")
    ax.set_title(f"{symbol} 布林带", fontsize=14, fontweight="bold")
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    if save:
        path = str(OUTPUT_DIR / f"{symbol}_bollinger.png")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"[图表] 布林带图已保存: {path}")
        return path
    else:
        plt.show()
        return ""
