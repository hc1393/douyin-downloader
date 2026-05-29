# -*- coding: utf-8 -*-
"""数据爬取模块 — 支持A股(AKShare)和美股(yfinance)"""

import pandas as pd
import akshare as ak
import yfinance as yf
from datetime import datetime, timedelta
from pathlib import Path
import hashlib
import json

from config.settings import CACHE_DIR


def _cache_key(symbol: str, start: str, end: str, source: str) -> Path:
    """生成缓存文件路径"""
    raw = f"{symbol}_{start}_{end}_{source}"
    h = hashlib.md5(raw.encode()).hexdigest()[:12]
    return CACHE_DIR / f"{symbol.replace('.', '_')}_{h}.csv"


def _load_cache(cache_path: Path, max_age_hours: int = 12) -> pd.DataFrame | None:
    """加载缓存数据（默认12小时内有效）"""
    if not cache_path.exists():
        return None
    mtime = datetime.fromtimestamp(cache_path.stat().st_mtime)
    if datetime.now() - mtime > timedelta(hours=max_age_hours):
        return None
    try:
        df = pd.read_csv(cache_path, index_col=0, parse_dates=True)
        return df if len(df) > 0 else None
    except Exception:
        return None


def _save_cache(df: pd.DataFrame, cache_path: Path):
    """保存数据到缓存"""
    df.to_csv(cache_path)


def fetch_a_share(symbol: str, start: str = None, end: str = None,
                  adjust: str = "qfq") -> pd.DataFrame:
    """
    获取A股行情数据（通过AKShare）

    Args:
        symbol: 股票代码，如 '000001', '600519'
        start: 开始日期 'YYYY-MM-DD'，默认1年前
        end: 结束日期 'YYYY-MM-DD'，默认今天
        adjust: 复权方式 'qfq'=前复权, 'hfq'=后复权, ''=不复权

    Returns:
        DataFrame with columns: open, high, low, close, volume, amount
    """
    if end is None:
        end = datetime.now().strftime("%Y%m%d")
    else:
        end = end.replace("-", "")
    if start is None:
        start = (datetime.now() - timedelta(days=365)).strftime("%Y%m%d")
    else:
        start = start.replace("-", "")

    cache_path = _cache_key(symbol, start, end, "akshare")
    cached = _load_cache(cache_path)
    if cached is not None:
        return cached

    print(f"[数据] 正在从 AKShare 获取 {symbol} ...")
    df = ak.stock_zh_a_hist(
        symbol=symbol,
        period="daily",
        start_date=start,
        end_date=end,
        adjust=adjust,
    )

    # 标准化列名
    col_map = {
        "日期": "date", "开盘": "open", "收盘": "close",
        "最高": "high", "最低": "low", "成交量": "volume",
        "成交额": "amount", "振幅": "amplitude", "涨跌幅": "pct_change",
        "涨跌额": "change", "换手率": "turnover",
    }
    df = df.rename(columns=col_map)
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date").sort_index()

    _save_cache(df, cache_path)
    print(f"[数据] {symbol} 获取完成，共 {len(df)} 条记录")
    return df


def fetch_us_stock(symbol: str, start: str = None, end: str = None) -> pd.DataFrame:
    """
    获取美股行情数据（通过yfinance）

    Args:
        symbol: 股票代码，如 'AAPL', 'TSLA', 'GOOG'
        start: 开始日期 'YYYY-MM-DD'，默认1年前
        end: 结束日期 'YYYY-MM-DD'，默认今天

    Returns:
        DataFrame with columns: open, high, low, close, volume
    """
    if start is None:
        start = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
    if end is None:
        end = datetime.now().strftime("%Y-%m-%d")

    cache_path = _cache_key(symbol, start, end, "yfinance")
    cached = _load_cache(cache_path)
    if cached is not None:
        return cached

    print(f"[数据] 正在从 yfinance 获取 {symbol} ...")
    ticker = yf.Ticker(symbol)
    df = ticker.history(start=start, end=end)

    if df.empty:
        raise ValueError(f"无法获取 {symbol} 的数据，请检查代码是否正确")

    # 标准化列名
    df.columns = [c.lower() for c in df.columns]
    df = df[["open", "high", "low", "close", "volume"]]
    df.index.name = "date"
    df.index = pd.to_datetime(df.index).tz_localize(None)

    _save_cache(df, cache_path)
    print(f"[数据] {symbol} 获取完成，共 {len(df)} 条记录")
    return df


def fetch_stock_info_a_share(symbol: str) -> dict:
    """获取A股基本信息"""
    try:
        df = ak.stock_individual_info_em(symbol=symbol)
        info = dict(zip(df["item"], df["value"]))
        return info
    except Exception as e:
        print(f"[警告] 获取股票信息失败: {e}")
        return {}


def fetch_index_a_share(symbol: str = "000001", start: str = None,
                        end: str = None) -> pd.DataFrame:
    """
    获取A股指数数据

    Args:
        symbol: 指数代码 '000001'=上证, '399001'=深证, '399006'=创业板
    """
    if end is None:
        end = datetime.now().strftime("%Y%m%d")
    else:
        end = end.replace("-", "")
    if start is None:
        start = (datetime.now() - timedelta(days=365)).strftime("%Y%m%d")
    else:
        start = start.replace("-", "")

    cache_path = _cache_key(f"idx_{symbol}", start, end, "akshare")
    cached = _load_cache(cache_path)
    if cached is not None:
        return cached

    print(f"[数据] 正在获取指数 {symbol} ...")
    df = ak.stock_zh_index_daily(symbol=f"sh{symbol}")

    df = df.rename(columns={"date": "date"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date").sort_index()
    df = df.loc[start:end]

    _save_cache(df, cache_path)
    print(f"[数据] 指数 {symbol} 获取完成，共 {len(df)} 条记录")
    return df


def generate_sample_data(symbol: str = "DEMO", days: int = 500,
                        base_price: float = 100.0) -> pd.DataFrame:
    """
    生成模拟行情数据（用于离线测试）

    Args:
        symbol: 股票代码标识
        days: 交易天数
        base_price: 基准价格

    Returns:
        模拟的行情DataFrame
    """
    np.random.seed(hash(symbol) % 2**31)
    dates = pd.bdate_range(end=datetime.now(), periods=days)

    # 模拟价格随机游走
    returns = np.random.normal(0.0003, 0.02, days)
    prices = base_price * np.cumprod(1 + returns)

    # 生成OHLCV
    data = {
        "open": prices * (1 + np.random.uniform(-0.01, 0.01, days)),
        "high": prices * (1 + np.abs(np.random.normal(0, 0.015, days))),
        "low": prices * (1 - np.abs(np.random.normal(0, 0.015, days))),
        "close": prices,
        "volume": np.random.randint(100000, 10000000, days).astype(float),
    }

    df = pd.DataFrame(data, index=dates)
    df.index.name = "date"
    # 确保 high >= max(open, close) 且 low <= min(open, close)
    df["high"] = df[["open", "close", "high"]].max(axis=1)
    df["low"] = df[["open", "close", "low"]].min(axis=1)

    print(f"[数据] 已生成 {symbol} 模拟数据，共 {len(df)} 条记录")
    return df


def fetch(symbol: str, start: str = None, end: str = None,
          market: str = "auto") -> pd.DataFrame:
    """
    智能获取行情数据（自动判断市场）

    Args:
        symbol: 股票代码
            A股: '000001', '600519' 等纯数字
            美股: 'AAPL', 'TSLA' 等字母
        start: 开始日期
        end: 结束日期
        market: 'a'=A股, 'us'=美股, 'auto'=自动判断
    """
    if market == "auto":
        if symbol.isdigit() or symbol.startswith(("sh", "sz", "bj")):
            market = "a"
        else:
            market = "us"

    if market == "a":
        code = symbol.replace("sh", "").replace("sz", "").replace("bj", "")
        return fetch_a_share(code, start, end)
    elif market == "us":
        return fetch_us_stock(symbol, start, end)
    else:
        raise ValueError(f"不支持的市场: {market}")
