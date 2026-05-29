# -*- coding: utf-8 -*-
"""项目全局配置"""

import os
from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent

# 数据缓存目录
CACHE_DIR = PROJECT_ROOT / "data" / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

# 输出目录（图表、报告）
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 默认参数
DEFAULT_MA_PERIODS = [5, 10, 20, 60, 120, 250]  # 均线周期
DEFAULT_RSI_PERIOD = 14
DEFAULT_MACD_FAST = 12
DEFAULT_MACD_SLOW = 26
DEFAULT_MACD_SIGNAL = 9
DEFAULT_BOLL_PERIOD = 20
DEFAULT_BOLL_STD = 2
DEFAULT_ATR_PERIOD = 14
DEFAULT_KDJ_PERIOD = 9

# 数据源优先级
DATA_SOURCE_PRIORITY = ["akshare", "yfinance"]

# A股市场代码前缀
A_SHARE_PREFIXES = {
    "sh": "上海",
    "sz": "深圳",
    "bj": "北京",
}
