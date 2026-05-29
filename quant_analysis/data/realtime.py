# -*- coding: utf-8 -*-
"""
实时行情模块 — 轮询式获取最新价格

支持:
  - A股: ak.stock_bid_ask_em (轻量单股票报价)
  - 美股: yf.Ticker.fast_info (最新价格)
  - 分时数据: 1分钟K线
"""

import pandas as pd
import numpy as np
from datetime import datetime


def fetch_realtime_a_share(symbol: str) -> dict:
    """
    获取A股实时报价

    Args:
        symbol: 股票代码，如 '000001'

    Returns:
        dict: {price, change, change_pct, open, high, low, prev_close,
               volume, turnover, bid1, ask1, time}
    """
    import akshare as ak

    try:
        df = ak.stock_bid_ask_em(symbol=symbol)
        if df.empty:
            raise ValueError(f"无法获取 {symbol} 的实时数据")

        # stock_bid_ask_em 返回两列: item, value
        data = dict(zip(df["item"], df["value"]))

        # 解析买卖五档
        price = float(data.get("最新", 0))
        prev_close = float(data.get("昨收", 0))
        change = price - prev_close if prev_close > 0 else 0
        change_pct = (change / prev_close * 100) if prev_close > 0 else 0

        return {
            "price": price,
            "change": round(change, 2),
            "change_pct": round(change_pct, 2),
            "open": float(data.get("今开", 0)),
            "high": float(data.get("最高", 0)),
            "low": float(data.get("最低", 0)),
            "prev_close": prev_close,
            "volume": float(data.get("成交量", 0)),
            "turnover": float(data.get("成交额", 0)),
            "bid1": float(data.get("买入", 0)),
            "ask1": float(data.get("卖出", 0)),
            "time": datetime.now().strftime("%H:%M:%S"),
            "symbol": symbol,
        }

    except Exception as e:
        # 回退: 尝试从全量快照中获取
        try:
            df_all = ak.stock_zh_a_spot_em()
            row = df_all[df_all["代码"] == symbol]
            if row.empty:
                raise ValueError(f"未找到 {symbol}")
            row = row.iloc[0]
            price = float(row.get("最新价", 0))
            prev_close = float(row.get("昨收", 0))
            return {
                "price": price,
                "change": float(row.get("涨跌额", 0)),
                "change_pct": float(row.get("涨跌幅", 0)),
                "open": float(row.get("今开", 0)),
                "high": float(row.get("最高", 0)),
                "low": float(row.get("最低", 0)),
                "prev_close": prev_close,
                "volume": float(row.get("成交量", 0)),
                "turnover": float(row.get("成交额", 0)),
                "bid1": 0,
                "ask1": 0,
                "time": datetime.now().strftime("%H:%M:%S"),
                "symbol": symbol,
            }
        except Exception:
            raise ValueError(f"获取 {symbol} 实时数据失败: {e}")


def fetch_realtime_us(symbol: str) -> dict:
    """
    获取美股实时报价

    Args:
        symbol: 股票代码，如 'AAPL'

    Returns:
        dict: {price, change, change_pct, open, high, low, prev_close,
               volume, time, symbol}
    """
    import yfinance as yf

    ticker = yf.Ticker(symbol)
    fi = ticker.fast_info

    price = fi.last_price
    prev_close = fi.previous_close
    change = price - prev_close if prev_close else 0
    change_pct = (change / prev_close * 100) if prev_close else 0

    return {
        "price": round(price, 2),
        "change": round(change, 2),
        "change_pct": round(change_pct, 2),
        "open": round(fi.get("open", price), 2) if hasattr(fi, "get") else price,
        "high": round(fi.day_high, 2),
        "low": round(fi.day_low, 2),
        "prev_close": round(prev_close, 2),
        "volume": int(fi.last_volume),
        "turnover": 0,
        "bid1": 0,
        "ask1": 0,
        "time": datetime.now().strftime("%H:%M:%S"),
        "symbol": symbol,
    }


def fetch_realtime(symbol: str, market: str = "auto") -> dict:
    """
    智能获取实时报价（自动判断市场）

    Args:
        symbol: 股票代码
        market: 'a'=A股, 'us'=美股, 'auto'=自动判断

    Returns:
        dict: 统一格式的实时报价
    """
    if market == "auto":
        if symbol.isdigit() or symbol.startswith(("sh", "sz", "bj")):
            market = "a"
        else:
            market = "us"

    if market == "a":
        code = symbol.replace("sh", "").replace("sz", "").replace("bj", "")
        return fetch_realtime_a_share(code)
    elif market == "us":
        return fetch_realtime_us(symbol)
    else:
        raise ValueError(f"不支持的市场: {market}")


def fetch_intraday_a_share(symbol: str, period: str = "1") -> pd.DataFrame:
    """
    获取A股分时K线数据

    Args:
        symbol: 股票代码
        period: K线周期 '1'/'5'/'15'/'30'/'60' 分钟

    Returns:
        DataFrame: 含 open/high/low/close/volume 的分时数据
    """
    import akshare as ak

    today = datetime.now().strftime("%Y-%m-%d")
    df = ak.stock_zh_a_hist_min_em(
        symbol=symbol,
        period=period,
        start_date=f"{today} 09:30:00",
        end_date=f"{today} 15:00:00",
        adjust="",
    )

    if df.empty:
        return df

    # 标准化列名
    col_map = {
        "时间": "datetime", "开盘": "open", "收盘": "close",
        "最高": "high", "最低": "low", "成交量": "volume",
        "成交额": "turnover",
    }
    df = df.rename(columns=col_map)
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.set_index("datetime").sort_index()
    return df


def fetch_intraday_us(symbol: str, interval: str = "1m") -> pd.DataFrame:
    """
    获取美股分时K线数据

    Args:
        symbol: 股票代码
        interval: K线周期 '1m'/'5m'/'15m'

    Returns:
        DataFrame: 含 open/high/low/close/volume 的分时数据
    """
    import yfinance as yf

    ticker = yf.Ticker(symbol)
    df = ticker.history(period="1d", interval=interval)

    if df.empty:
        return df

    df.columns = [c.lower() for c in df.columns]
    df = df[["open", "high", "low", "close", "volume"]]
    df.index.name = "datetime"
    df.index = pd.to_datetime(df.index).tz_localize(None)
    return df


def fetch_intraday(symbol: str, market: str = "auto",
                   period: str = "1") -> pd.DataFrame:
    """
    智能获取分时数据

    Args:
        symbol: 股票代码
        market: 'a'=A股, 'us'=美股, 'auto'=自动判断
        period: K线周期 (A股用分钟数, 美股用 '1m' 格式)

    Returns:
        DataFrame: 分时K线数据
    """
    if market == "auto":
        if symbol.isdigit() or symbol.startswith(("sh", "sz", "bj")):
            market = "a"
        else:
            market = "us"

    if market == "a":
        code = symbol.replace("sh", "").replace("sz", "").replace("bj", "")
        return fetch_intraday_a_share(code, period=period)
    elif market == "us":
        interval = f"{period}m" if period.isdigit() else period
        return fetch_intraday_us(symbol, interval=interval)
    else:
        raise ValueError(f"不支持的市场: {market}")
