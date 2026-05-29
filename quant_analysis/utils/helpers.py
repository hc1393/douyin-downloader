# -*- coding: utf-8 -*-
"""工具函数"""

import pandas as pd
from tabulate import tabulate


def format_number(n, decimals=2):
    """格式化数字"""
    if abs(n) >= 1e8:
        return f"{n / 1e8:.{decimals}f}亿"
    elif abs(n) >= 1e4:
        return f"{n / 1e4:.{decimals}f}万"
    else:
        return f"{n:.{decimals}f}"


def print_df(df: pd.DataFrame, title: str = "", max_rows: int = 20):
    """格式化打印 DataFrame"""
    if title:
        print(f"\n{title}")
        print("=" * 60)
    print(tabulate(df.head(max_rows), headers="keys", tablefmt="simple",
                   floatfmt=".2f", showindex=True))
    if len(df) > max_rows:
        print(f"... 共 {len(df)} 行，显示前 {max_rows} 行")


def validate_symbol(symbol: str) -> str:
    """验证并标准化股票代码"""
    symbol = symbol.strip().upper()
    # 移除可能的市场前缀
    for prefix in ["SH.", "SZ.", "BJ.", "SS.", "HK."]:
        if symbol.startswith(prefix):
            symbol = symbol[len(prefix):]
    return symbol
