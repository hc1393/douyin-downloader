# 量化分析系统

纯分析工具，不含交易功能。支持A股和美股的数据爬取、技术分析、统计分析和可视化。

## 安装

```bash
pip install -r requirements.txt
```

## 使用

```bash
# 分析A股（自动判断市场）
python main.py 600519              # 茅台
python main.py 000001              # 平安银行
python main.py 000858              # 五粮液

# 分析美股
python main.py AAPL --market us
python main.py TSLA --market us

# 指定时间范围
python main.py 600519 --start 2023-01-01 --end 2024-01-01

# 对比分析多只股票
python main.py 600519 000858 --compare
python main.py AAPL TSLA GOOG --market us --compare
```

## 输出

- `output/` 目录下生成图表：K线图、MACD、RSI、回撤图、收益率分布图、布林带
- 终端输出：统计报告（年化收益、夏普比率、最大回撤等）

## 项目结构

```
quant_analysis/
├── main.py              # 主入口
├── requirements.txt
├── config/settings.py   # 全局配置
├── data/
│   └── fetcher.py       # 数据爬取（AKShare + yfinance）
├── analysis/
│   ├── technical.py     # 技术分析（MA/MACD/RSI/KDJ/BOLL/ATR）
│   └── statistical.py   # 统计分析（收益/波动/回撤/夏普）
├── visualization/
│   └── charts.py        # 图表绘制
├── utils/
│   └── helpers.py       # 工具函数
└── output/              # 图表输出目录
```
