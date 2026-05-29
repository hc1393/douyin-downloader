# -*- coding: utf-8 -*-
"""
图表绘制引擎 — 所有图表的核心绘制逻辑

此模块是 charts.py（文件输出）和 gui.py（Qt 画布）的共享绘制引擎。
每个函数接收 matplotlib Axes 对象和颜色方案，在其上绘制图表。
"""

import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats as scipy_stats


# ============================================================
# 颜色方案
# ============================================================

COLORS_LIGHT = {
    "up": "#ef4444",        # 阳线 (红)
    "down": "#22c55e",      # 阴线 (绿)
    "price": "#1f77b4",     # 收盘价线
    "ma5": "#ff7f0e",       # MA5
    "ma10": "#2ca02c",      # MA10
    "ma20": "#9467bd",      # MA20
    "dif": "#1f77b4",       # DIF
    "dea": "#ff7f0e",       # DEA
    "rsi": "#9467bd",       # RSI
    "boll_mid": "#ff7f0e",  # 布林中轨
    "boll_upper": "#d62728",# 布林上轨
    "boll_lower": "#2ca02c",# 布林下轨
    "fill": "#cccccc",      # 填充色
    "grid": "#cccccc",      # 网格
    "zero": "#888888",      # 零线
    "hist": "#6c8ebf",      # 直方图
    "mean": "#d62728",      # 均值线
}

COLORS_DARK = {
    "up": "#ef4444",
    "down": "#22c55e",
    "price": "#89b4fa",
    "ma5": "#f9a825",
    "ma10": "#42a5f5",
    "ma20": "#ab47bc",
    "dif": "#89b4fa",
    "dea": "#f9a825",
    "rsi": "#ce93d8",
    "boll_mid": "#f9a825",
    "boll_upper": "#ef4444",
    "boll_lower": "#22c55e",
    "fill": "#555555",
    "grid": "#333344",
    "zero": "#555555",
    "hist": "#6c8ebf",
    "mean": "#ef4444",
}


def get_colors(theme: str = "light") -> dict:
    """获取颜色方案"""
    return COLORS_DARK if theme == "dark" else COLORS_LIGHT


# ============================================================
# 绘制函数 — 每个函数在给定的 Axes 上绘制
# ============================================================

def draw_candlestick(ax_price, ax_volume, data: pd.DataFrame,
                     colors: dict = None, show_ma: bool = True):
    """
    绘制K线图 + 成交量

    Args:
        ax_price: 价格图的 Axes
        ax_volume: 成交量图的 Axes
        data: OHLCV 数据 (已切片到显示范围)
        colors: 颜色方案
        show_ma: 是否显示均线
    """
    if colors is None:
        colors = COLORS_LIGHT

    up = data[data["close"] >= data["open"]]
    down = data[data["close"] < data["open"]]

    # 阳线
    ax_price.bar(up.index, up["close"] - up["open"], bottom=up["open"],
                 width=0.8, color=colors["up"], alpha=0.9)
    ax_price.bar(up.index, up["high"] - up["close"], bottom=up["close"],
                 width=0.1, color=colors["up"])
    ax_price.bar(up.index, up["low"] - up["open"], bottom=up["open"],
                 width=0.1, color=colors["up"])

    # 阴线
    ax_price.bar(down.index, down["close"] - down["open"], bottom=down["open"],
                 width=0.8, color=colors["down"], alpha=0.9)
    ax_price.bar(down.index, down["high"] - down["open"], bottom=down["open"],
                 width=0.1, color=colors["down"])
    ax_price.bar(down.index, down["low"] - down["close"], bottom=down["close"],
                 width=0.1, color=colors["down"])

    # 均线
    if show_ma:
        for col, label, key in [("ma5", "MA5", "ma5"),
                                 ("ma10", "MA10", "ma10"),
                                 ("ma20", "MA20", "ma20")]:
            if col in data.columns:
                ax_price.plot(data.index, data[col], label=label,
                              linewidth=1, alpha=0.8, color=colors[key])

    ax_price.legend(loc="upper left", fontsize=8)
    ax_price.grid(True, alpha=0.3)
    ax_price.set_ylabel("价格")

    # 成交量
    vol_colors = [colors["up"] if c >= o else colors["down"]
                  for c, o in zip(data["close"], data["open"])]
    ax_volume.bar(data.index, data["volume"], color=vol_colors,
                  alpha=0.7, width=0.8)
    ax_volume.set_ylabel("成交量")
    ax_volume.grid(True, alpha=0.3)


def draw_macd(ax_price, ax_macd, data: pd.DataFrame, colors: dict = None):
    """
    绘制 MACD 指标

    Args:
        ax_price: 价格图的 Axes
        ax_macd: MACD 图的 Axes
        data: 含 MA/DIF/DEA/MACD 列的数据
        colors: 颜色方案
    """
    if colors is None:
        colors = COLORS_LIGHT

    # 价格 + 均线
    ax_price.plot(data.index, data["close"], label="收盘价",
                  linewidth=1.2, color=colors["price"])
    if "ma5" in data.columns:
        ax_price.plot(data.index, data["ma5"], label="MA5",
                      linewidth=0.8, alpha=0.7, color=colors["ma5"])
    if "ma20" in data.columns:
        ax_price.plot(data.index, data["ma20"], label="MA20",
                      linewidth=0.8, alpha=0.7, color=colors["ma20"])
    ax_price.legend(loc="upper left", fontsize=8)
    ax_price.grid(True, alpha=0.3)

    # MACD
    if "dif" in data.columns and "dea" in data.columns:
        ax_macd.plot(data.index, data["dif"], label="DIF",
                     linewidth=1, color=colors["dif"])
        ax_macd.plot(data.index, data["dea"], label="DEA",
                     linewidth=1, color=colors["dea"])
        macd_colors = [colors["up"] if v >= 0 else colors["down"]
                       for v in data["macd"]]
        ax_macd.bar(data.index, data["macd"], color=macd_colors,
                    alpha=0.6, width=0.8)
        ax_macd.axhline(y=0, color=colors["zero"], linewidth=0.5)
        ax_macd.legend(loc="upper left", fontsize=8)
    ax_macd.grid(True, alpha=0.3)


def draw_rsi(ax, data: pd.DataFrame, colors: dict = None):
    """
    绘制 RSI 指标

    Args:
        ax: 绘图的 Axes
        data: 含 rsi 列的数据
        colors: 颜色方案
    """
    if colors is None:
        colors = COLORS_LIGHT

    ax.plot(data.index, data["rsi"], label="RSI",
            linewidth=1.2, color=colors["rsi"])
    ax.axhline(y=70, color=colors["up"], linestyle="--",
               linewidth=0.8, label="超买(70)")
    ax.axhline(y=30, color=colors["down"], linestyle="--",
               linewidth=0.8, label="超卖(30)")
    ax.axhline(y=50, color=colors["zero"], linestyle="-", linewidth=0.5)
    ax.fill_between(data.index, 70, 100, alpha=0.1, color=colors["up"])
    ax.fill_between(data.index, 0, 30, alpha=0.1, color=colors["down"])
    ax.set_ylim(0, 100)
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(True, alpha=0.3)


def draw_drawdown(ax_price, ax_dd, df: pd.DataFrame, colors: dict = None):
    """
    绘制回撤图

    Args:
        ax_price: 价格图的 Axes
        ax_dd: 回撤图的 Axes
        df: 完整行情数据
        colors: 颜色方案
    """
    from analysis.statistical import drawdown_series
    if colors is None:
        colors = COLORS_LIGHT

    dd = drawdown_series(df)

    ax_price.plot(df.index, df["close"], label="收盘价",
                  linewidth=1.2, color=colors["price"])
    ax_price.legend(loc="upper left", fontsize=8)
    ax_price.grid(True, alpha=0.3)

    ax_dd.fill_between(dd.index, dd.values, 0,
                       color=colors["up"], alpha=0.4)
    ax_dd.plot(dd.index, dd.values, color=colors["up"], linewidth=0.8)
    ax_dd.set_ylabel("回撤")
    ax_dd.grid(True, alpha=0.3)


def draw_returns_dist(ax_hist, ax_qq, df: pd.DataFrame, symbol: str = "",
                      colors: dict = None):
    """
    绘制收益率分布图

    Args:
        ax_hist: 直方图的 Axes
        ax_qq: QQ 图的 Axes
        df: 行情数据
        symbol: 股票代码
        colors: 颜色方案
    """
    from analysis.statistical import daily_returns
    if colors is None:
        colors = COLORS_LIGHT

    ret = daily_returns(df).dropna()

    # 直方图
    ax_hist.hist(ret.values, bins=50, density=True, alpha=0.7,
                 color=colors["hist"], edgecolor="none")
    ax_hist.axvline(x=ret.mean(), color=colors["mean"], linestyle="--",
                    label=f"均值: {ret.mean():.4f}")
    ax_hist.axvline(x=0, color=colors["zero"], linestyle="-", linewidth=0.5)
    ax_hist.set_xlabel("日收益率")
    ax_hist.set_ylabel("密度")
    ax_hist.legend(fontsize=8)
    ax_hist.grid(True, alpha=0.3)

    # QQ 图
    scipy_stats.probplot(ret.values, dist="norm", plot=ax_qq)
    ax_qq.grid(True, alpha=0.3)


def draw_bollinger(ax, data: pd.DataFrame, colors: dict = None):
    """
    绘制布林带

    Args:
        ax: 绘图的 Axes
        data: 含 boll_mid/boll_upper/boll_lower 列的数据
        colors: 颜色方案
    """
    if colors is None:
        colors = COLORS_LIGHT

    ax.plot(data.index, data["close"], label="收盘价",
            linewidth=1.2, color=colors["price"])
    ax.plot(data.index, data["boll_mid"], label="中轨",
            linewidth=0.8, color=colors["boll_mid"])
    ax.plot(data.index, data["boll_upper"], label="上轨",
            linewidth=0.8, color=colors["boll_upper"], linestyle="--")
    ax.plot(data.index, data["boll_lower"], label="下轨",
            linewidth=0.8, color=colors["boll_lower"], linestyle="--")
    ax.fill_between(data.index, data["boll_upper"], data["boll_lower"],
                    alpha=0.1, color=colors["fill"])
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(True, alpha=0.3)


def draw_correlation(ax, corr_matrix: pd.DataFrame):
    """
    绘制相关性热力图

    Args:
        ax: 绘图的 Axes
        corr_matrix: 相关性矩阵
    """
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="RdYlGn",
                center=0, square=True, ax=ax)


def draw_obv(ax_price, ax_obv, data: pd.DataFrame, colors: dict = None):
    """
    绘制 OBV 指标

    Args:
        ax_price: 价格图的 Axes
        ax_obv: OBV 图的 Axes
        data: 含 obv 列的数据
        colors: 颜色方案
    """
    if colors is None:
        colors = COLORS_LIGHT

    ax_price.plot(data.index, data["close"], label="收盘价",
                  linewidth=1.2, color=colors["price"])
    ax_price.legend(loc="upper left", fontsize=8)
    ax_price.grid(True, alpha=0.3)

    if "obv" in data.columns:
        obv_normalized = data["obv"] / data["obv"].abs().max()
        ax_obv.plot(data.index, obv_normalized, label="OBV(归一化)",
                    linewidth=1, color=colors["rsi"])
        ax_obv.axhline(y=0, color=colors["zero"], linewidth=0.5)
        ax_obv.legend(loc="upper left", fontsize=8)
    ax_obv.grid(True, alpha=0.3)


def draw_vwap(ax, data: pd.DataFrame, colors: dict = None):
    """
    绘制 VWAP 图

    Args:
        ax: 绘图的 Axes
        data: 含 vwap 列的数据
        colors: 颜色方案
    """
    if colors is None:
        colors = COLORS_LIGHT

    ax.plot(data.index, data["close"], label="收盘价",
            linewidth=1.2, color=colors["price"])
    if "vwap" in data.columns:
        ax.plot(data.index, data["vwap"], label="VWAP",
                linewidth=1.2, color=colors["boll_mid"], linestyle="--")
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(True, alpha=0.3)


def draw_ichimoku(ax, data: pd.DataFrame, colors: dict = None):
    """
    绘制一目均衡图

    Args:
        ax: 绘图的 Axes
        data: 含 ichimoku_* 列的数据
        colors: 颜色方案
    """
    if colors is None:
        colors = COLORS_LIGHT

    ax.plot(data.index, data["close"], label="收盘价",
            linewidth=1.2, color=colors["price"])

    lines = [
        ("tenkan_sen", "转换线", "#1f77b4"),
        ("kijun_sen", "基准线", "#ff7f0e"),
        ("senkou_a", "先行A", "#2ca02c"),
        ("senkou_b", "先行B", "#d62728"),
        ("chikou_span", "迟行线", "#9467bd"),
    ]
    for col, label, color in lines:
        if col in data.columns:
            ax.plot(data.index, data[col], label=label,
                    linewidth=0.8, color=color, alpha=0.8)

    # 云带填充
    if "senkou_a" in data.columns and "senkou_b" in data.columns:
        ax.fill_between(data.index, data["senkou_a"], data["senkou_b"],
                        where=data["senkou_a"] >= data["senkou_b"],
                        alpha=0.1, color=colors["down"])
        ax.fill_between(data.index, data["senkou_a"], data["senkou_b"],
                        where=data["senkou_a"] < data["senkou_b"],
                        alpha=0.1, color=colors["up"])

    ax.legend(loc="upper left", fontsize=8)
    ax.grid(True, alpha=0.3)
