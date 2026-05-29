# -*- coding: utf-8 -*-
"""
量化分析系统 — 主入口

功能：
  1. 数据爬取（A股/AKShare，美股/yfinance）
  2. 技术分析（均线、MACD、RSI、KDJ、布林带、ATR）
  3. 统计分析（收益率、波动率、回撤、夏普比率）
  4. 可视化（K线图、指标图、回撤图、分布图）

用法：
  python main.py                          # 分析默认示例股票
  python main.py 600519                   # 分析A股茅台
  python main.py AAPL --market us         # 分析美股苹果
  python main.py 000001 600519 --compare  # 对比分析多只股票
"""

import sys
import argparse
from datetime import datetime

from data.fetcher import fetch, fetch_stock_info_a_share, generate_sample_data
from analysis.technical import apply_all_indicators, support_resistance
from analysis.statistical import (
    descriptive_stats, print_stats, correlation_matrix,
    annualized_return, annualized_volatility, sharpe_ratio, max_drawdown,
)
from visualization.charts import (
    plot_candlestick, plot_macd, plot_rsi, plot_drawdown,
    plot_returns_distribution, plot_bollinger, plot_correlation_heatmap,
)
from utils.helpers import print_df, validate_symbol


def analyze_single(symbol: str, market: str = "auto", start: str = None,
                   end: str = None):
    """单只股票完整分析"""
    print(f"\n{'#' * 60}")
    print(f"  量化分析: {symbol}")
    print(f"  时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'#' * 60}")

    # 1. 获取数据
    print("\n[1/4] 获取行情数据...")
    df = fetch(symbol, start=start, end=end, market=market)
    print(f"  数据范围: {df.index[0].date()} ~ {df.index[-1].date()}")
    print(f"  数据条数: {len(df)}")

    # 获取A股基本信息
    if market in ("a", "auto") and symbol.replace("sh", "").replace("sz", "").isdigit():
        info = fetch_stock_info_a_share(
            symbol.replace("sh", "").replace("sz", "").replace("bj", "")
        )
        if info:
            print(f"  股票名称: {info.get('股票简称', 'N/A')}")
            print(f"  所属行业: {info.get('行业', 'N/A')}")

    # 2. 技术分析
    print("\n[2/4] 计算技术指标...")
    df = apply_all_indicators(df)
    sr = support_resistance(df)
    print(f"  均线(MA5/10/20/60/120/250) ✓")
    print(f"  MACD ✓")
    print(f"  RSI ✓")
    print(f"  KDJ ✓")
    print(f"  布林带 ✓")
    print(f"  ATR ✓")
    print(f"  量比 ✓")
    if sr["support"]:
        print(f"  支撑位: {sr['support']}")
    if sr["resistance"]:
        print(f"  阻力位: {sr['resistance']}")

    # 3. 统计分析
    print("\n[3/4] 统计分析...")
    print_stats(df, symbol)

    # 4. 可视化
    print("[4/4] 生成图表...")
    plot_candlestick(df, symbol=symbol)
    plot_macd(df, symbol=symbol)
    plot_rsi(df, symbol=symbol)
    plot_drawdown(df, symbol=symbol)
    plot_returns_distribution(df, symbol=symbol)
    plot_bollinger(df, symbol=symbol)

    print(f"\n{'=' * 60}")
    print(f"  分析完成! 图表已保存到 output/ 目录")
    print(f"{'=' * 60}")

    return df


def compare_stocks(symbols: list, market: str = "auto", start: str = None,
                   end: str = None):
    """多只股票对比分析"""
    print(f"\n{'#' * 60}")
    print(f"  对比分析: {', '.join(symbols)}")
    print(f"{'#' * 60}")

    # 获取所有数据
    all_data = {}
    for sym in symbols:
        print(f"\n获取 {sym} ...")
        df = fetch(sym, start=start, end=end, market=market)
        df = apply_all_indicators(df)
        all_data[sym] = df

    # 对比统计
    print(f"\n{'=' * 60}")
    print(f"  对比统计")
    print(f"{'=' * 60}")

    headers = ["指标"] + symbols
    rows = []
    for label, func in [
        ("年化收益率", lambda d: f"{annualized_return(d) * 100:.2f}%"),
        ("年化波动率", lambda d: f"{annualized_volatility(d) * 100:.2f}%"),
        ("夏普比率", lambda d: f"{sharpe_ratio(d):.2f}"),
        ("最大回撤", lambda d: f"{max_drawdown(d)['max_drawdown'] * 100:.2f}%"),
    ]:
        row = [label] + [func(d) for d in all_data.values()]
        rows.append(row)

    from tabulate import tabulate
    print(tabulate(rows, headers=headers, tablefmt="simple"))

    # 相关性矩阵
    print("\n相关性矩阵:")
    corr = correlation_matrix(all_data)
    print(tabulate(corr.round(3), headers="keys", tablefmt="simple",
                   showindex=True))

    # 图表
    print("\n生成图表...")
    plot_correlation_heatmap(corr, title="收益率相关性矩阵")

    for sym, df in all_data.items():
        plot_candlestick(df, symbol=sym)

    print(f"\n对比分析完成! 图表已保存到 output/ 目录")
    return all_data


def main():
    parser = argparse.ArgumentParser(description="量化分析系统")
    parser.add_argument("symbols", nargs="*", default=["000001"],
                        help="股票代码，如 600519 AAPL")
    parser.add_argument("--market", default="auto",
                        choices=["auto", "a", "us"],
                        help="市场类型: a=A股, us=美股, auto=自动判断")
    parser.add_argument("--start", default=None, help="开始日期 YYYY-MM-DD")
    parser.add_argument("--end", default=None, help="结束日期 YYYY-MM-DD")
    parser.add_argument("--compare", action="store_true",
                        help="对比分析模式")

    args = parser.parse_args()

    if args.compare or len(args.symbols) > 1:
        compare_stocks(args.symbols, market=args.market,
                       start=args.start, end=args.end)
    else:
        analyze_single(args.symbols[0], market=args.market,
                       start=args.start, end=args.end)


if __name__ == "__main__":
    main()
