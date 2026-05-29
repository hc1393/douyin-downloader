# -*- coding: utf-8 -*-
"""
回测引擎 — 简单事件驱动回测框架

功能:
  - 基于信号的买卖回测
  - 支持手续费和滑点
  - 计算回测指标 (收益率、夏普比率、最大回撤、胜率等)
  - 输出资金曲线和交易记录
"""

import pandas as pd
import numpy as np


class BacktestEngine:
    """
    简单回测引擎

    用法:
        engine = BacktestEngine(initial_capital=100000)
        result = engine.run(df, signal_column="signal")
        print(result["metrics"])
    """

    def __init__(self, initial_capital: float = 100000,
                 commission: float = 0.001, slippage: float = 0.001):
        """
        Args:
            initial_capital: 初始资金
            commission: 手续费率 (默认0.1%)
            slippage: 滑点率 (默认0.1%)
        """
        self.initial_capital = initial_capital
        self.commission = commission
        self.slippage = slippage

    def run(self, df: pd.DataFrame, signal_column: str = "signal") -> dict:
        """
        执行回测

        Args:
            df: 含信号列的行情数据
            signal_column: 信号列名 (1=买入, -1=卖出, 0=无操作)

        Returns:
            {
                'trades': DataFrame 交易记录,
                'equity': Series 资金曲线,
                'metrics': dict 回测指标,
                'df': DataFrame 含回测列的原始数据,
            }
        """
        if signal_column not in df.columns:
            raise ValueError(f"数据中缺少信号列: {signal_column}")

        data = df.copy()
        data["signal"] = data[signal_column]

        # 初始化
        capital = self.initial_capital
        position = 0  # 持仓数量
        equity_list = []
        trades = []

        for i in range(len(data)):
            price = data["close"].iloc[i]
            signal = data["signal"].iloc[i]
            date = data.index[i]

            if signal == 1 and position == 0:
                # 买入
                buy_price = price * (1 + self.slippage)
                shares = int(capital * 0.95 / buy_price)  # 留5%现金
                if shares > 0:
                    cost = shares * buy_price * (1 + self.commission)
                    capital -= cost
                    position = shares
                    trades.append({
                        "日期": date, "类型": "买入",
                        "价格": buy_price, "数量": shares,
                        "成本": cost, "资金": capital,
                    })

            elif signal == -1 and position > 0:
                # 卖出
                sell_price = price * (1 - self.slippage)
                revenue = position * sell_price * (1 - self.commission)
                capital += revenue
                trades.append({
                    "日期": date, "类型": "卖出",
                    "价格": sell_price, "数量": position,
                    "收入": revenue, "资金": capital,
                })
                position = 0

            # 计算当前权益
            equity = capital + position * price
            equity_list.append(equity)

        # 构建结果
        data["equity"] = equity_list
        equity_series = pd.Series(equity_list, index=data.index)
        trades_df = pd.DataFrame(trades) if trades else pd.DataFrame()

        metrics = self._calculate_metrics(equity_series, trades_df, data)

        return {
            "trades": trades_df,
            "equity": equity_series,
            "metrics": metrics,
            "df": data,
        }

    def _calculate_metrics(self, equity: pd.Series, trades: pd.DataFrame,
                           df: pd.DataFrame) -> dict:
        """计算回测指标"""
        total_return = (equity.iloc[-1] / equity.iloc[0]) - 1

        # 年化收益率
        n_days = len(equity)
        ann_return = (1 + total_return) ** (250 / n_days) - 1

        # 最大回撤
        peak = equity.expanding().max()
        drawdown = (equity - peak) / peak
        max_dd = abs(drawdown.min())

        # 夏普比率
        daily_returns = equity.pct_change().dropna()
        sharpe = 0
        if daily_returns.std() > 0:
            sharpe = (daily_returns.mean() * 250 - 0.03) / (
                daily_returns.std() * np.sqrt(250))

        # 交易统计
        n_trades = len(trades[trades["类型"] == "卖出"]) if not trades.empty else 0
        win_trades = 0
        if n_trades > 0 and not trades.empty:
            buy_trades = trades[trades["类型"] == "买入"]
            sell_trades = trades[trades["类型"] == "卖出"]
            if len(buy_trades) == len(sell_trades):
                win_trades = sum(
                    sell_trades["价格"].values > buy_trades["价格"].values)

        win_rate = win_trades / n_trades if n_trades > 0 else 0

        # 买入持有收益
        buy_hold_return = (df["close"].iloc[-1] / df["close"].iloc[0]) - 1

        return {
            "初始资金": f"{self.initial_capital:,.0f}",
            "最终权益": f"{equity.iloc[-1]:,.0f}",
            "总收益率": f"{total_return * 100:.2f}%",
            "年化收益率": f"{ann_return * 100:.2f}%",
            "最大回撤": f"{max_dd * 100:.2f}%",
            "夏普比率": f"{sharpe:.2f}",
            "交易次数": n_trades,
            "胜率": f"{win_rate * 100:.1f}%",
            "买入持有收益": f"{buy_hold_return * 100:.2f}%",
            "超额收益": f"{(total_return - buy_hold_return) * 100:.2f}%",
        }


def backtest_strategy(df: pd.DataFrame, strategy: str = "combined",
                      initial_capital: float = 100000,
                      commission: float = 0.001,
                      slippage: float = 0.001,
                      **kwargs) -> dict:
    """
    一键回测

    Args:
        df: 含技术指标的数据
        strategy: 策略名称
        initial_capital: 初始资金
        commission: 手续费率
        slippage: 滑点率
        **kwargs: 策略参数

    Returns:
        BacktestEngine.run() 的结果
    """
    from analysis.strategy import generate_signals

    signal = generate_signals(df, strategy, **kwargs)
    df = df.copy()
    df["signal"] = signal

    engine = BacktestEngine(
        initial_capital=initial_capital,
        commission=commission,
        slippage=slippage,
    )
    return engine.run(df, signal_column="signal")


def compare_strategies(df: pd.DataFrame, strategies: list = None,
                       initial_capital: float = 100000) -> pd.DataFrame:
    """
    对比多个策略的回测结果

    Args:
        df: 含技术指标的数据
        strategies: 策略列表，默认全部
        initial_capital: 初始资金

    Returns:
        对比表格 DataFrame
    """
    from analysis.strategy import STRATEGIES

    if strategies is None:
        strategies = ["ma_cross", "macd", "rsi", "bollinger", "kdj", "combined"]

    results = []
    for name in strategies:
        try:
            result = backtest_strategy(
                df, strategy=name, initial_capital=initial_capital)
            metrics = result["metrics"]
            metrics["策略"] = name
            results.append(metrics)
        except Exception as e:
            print(f"[回测] 策略 {name} 失败: {e}")

    if not results:
        return pd.DataFrame()

    df_result = pd.DataFrame(results)
    df_result = df_result.set_index("策略")
    return df_result
