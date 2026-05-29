# -*- coding: utf-8 -*-
"""量化分析系统 — 图形界面"""

# ============================================================
# matplotlib 后端必须在任何其他 matplotlib 导入之前设置
# ============================================================
import matplotlib
matplotlib.use("Qt5Agg")

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
import seaborn as sns
from scipy import stats as scipy_stats

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QPushButton,
    QTabWidget, QTableWidget, QTableWidgetItem, QStatusBar, QMessageBox,
    QSplitter, QGroupBox, QHeaderView, QProgressBar, QCheckBox,
)
from PyQt5.QtCore import Qt, QDate, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

from data.fetcher import fetch, generate_sample_data, fetch_stock_info_a_share
from analysis.technical import apply_all_indicators, support_resistance
from analysis.statistical import (
    descriptive_stats, daily_returns, drawdown_series,
    annualized_return, annualized_volatility, sharpe_ratio, max_drawdown,
    correlation_matrix,
)

# ============================================================
# matplotlib 全局样式 — 暗色主题
# ============================================================
plt.rcParams.update({
    "figure.facecolor": "#1e1e2e",
    "axes.facecolor": "#1e1e2e",
    "axes.edgecolor": "#555555",
    "axes.labelcolor": "#cdd6f4",
    "text.color": "#cdd6f4",
    "xtick.color": "#a6adc8",
    "ytick.color": "#a6adc8",
    "grid.color": "#333344",
    "grid.alpha": 0.3,
    "font.sans-serif": ["SimHei", "Microsoft YaHei", "DejaVu Sans"],
    "axes.unicode_minus": False,
    "figure.dpi": 100,
})

# ============================================================
# 暗色主题 QSS 样式表 (Catppuccin Mocha)
# ============================================================
DARK_THEME = """
QMainWindow, QWidget {
    background-color: #1e1e2e;
    color: #cdd6f4;
}
QGroupBox {
    border: 1px solid #45475a;
    border-radius: 6px;
    margin-top: 12px;
    padding-top: 16px;
    font-weight: bold;
    color: #89b4fa;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 12px;
    padding: 0 6px;
}
QLabel {
    color: #cdd6f4;
    font-size: 13px;
}
QLineEdit, QDateEdit, QComboBox {
    background-color: #313244;
    color: #cdd6f4;
    border: 1px solid #45475a;
    border-radius: 4px;
    padding: 6px;
    font-size: 13px;
}
QLineEdit:focus, QDateEdit:focus, QComboBox:focus {
    border: 1px solid #89b4fa;
}
QComboBox::drop-down {
    border: none;
    width: 20px;
}
QComboBox::down-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 6px solid #a6adc8;
    margin-right: 6px;
}
QComboBox QAbstractItemView {
    background-color: #313244;
    color: #cdd6f4;
    selection-background-color: #45475a;
    border: 1px solid #585b70;
}
QPushButton {
    background-color: #89b4fa;
    color: #1e1e2e;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #74c7ec;
}
QPushButton:pressed {
    background-color: #585b70;
}
QPushButton:disabled {
    background-color: #45475a;
    color: #6c7086;
}
QTabWidget::pane {
    border: 1px solid #45475a;
    background-color: #1e1e2e;
    border-radius: 4px;
}
QTabBar::tab {
    background-color: #313244;
    color: #a6adc8;
    padding: 8px 16px;
    margin-right: 2px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    font-size: 13px;
}
QTabBar::tab:selected {
    background-color: #1e1e2e;
    color: #89b4fa;
    border-bottom: 2px solid #89b4fa;
}
QTabBar::tab:hover:!selected {
    background-color: #45475a;
}
QTableWidget {
    background-color: #1e1e2e;
    color: #cdd6f4;
    gridline-color: #313244;
    border: 1px solid #45475a;
    font-size: 12px;
    border-radius: 4px;
}
QTableWidget::item {
    padding: 4px;
}
QTableWidget::item:alternate {
    background-color: #232336;
}
QHeaderView::section {
    background-color: #313244;
    color: #89b4fa;
    padding: 6px;
    border: 1px solid #45475a;
    font-weight: bold;
    font-size: 12px;
}
QStatusBar {
    background-color: #181825;
    color: #a6adc8;
    font-size: 12px;
}
QProgressBar {
    background-color: #313244;
    border: 1px solid #45475a;
    border-radius: 4px;
    text-align: center;
    color: #cdd6f4;
    height: 16px;
}
QProgressBar::chunk {
    background-color: #89b4fa;
    border-radius: 3px;
}
QScrollBar:vertical {
    background-color: #1e1e2e;
    width: 10px;
}
QScrollBar::handle:vertical {
    background-color: #45475a;
    border-radius: 5px;
    min-height: 20px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QCheckBox {
    color: #cdd6f4;
    font-size: 13px;
    spacing: 6px;
}
QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border: 1px solid #45475a;
    border-radius: 3px;
    background-color: #313244;
}
QCheckBox::indicator:checked {
    background-color: #89b4fa;
    border-color: #89b4fa;
}
"""


# ============================================================
# ChartCanvas — 嵌入 matplotlib Figure 的 Qt 画布
# ============================================================
class ChartCanvas(FigureCanvasQTAgg):
    """封装 matplotlib Figure 用于嵌入 PyQt5"""

    def __init__(self, parent=None, nrows=1, ncols=1, height_ratios=None):
        self._fig = Figure(facecolor="#1e1e2e", dpi=100)
        super().__init__(self._fig)
        self.setParent(parent)
        self._nrows = nrows
        self._ncols = ncols
        self._height_ratios = height_ratios
        self._fig.subplots_adjust(hspace=0.35, left=0.08, right=0.95, top=0.93, bottom=0.08)
        self.setMinimumSize(400, 300)

    def clear_and_get_axes(self):
        """清除画布并返回新的 axes 列表"""
        self._fig.clear()
        gs_kw = {}
        if self._height_ratios:
            gs_kw["height_ratios"] = self._height_ratios
        axes = self._fig.subplots(self._nrows, self._ncols, **gs_kw)
        if not isinstance(axes, (list, np.ndarray)):
            axes = [axes]
        else:
            axes = list(axes.flat) if hasattr(axes, "flat") else list(axes)
        return axes

    def refresh(self):
        """重绘画布"""
        self._fig.subplots_adjust(hspace=0.35, left=0.08, right=0.95, top=0.93, bottom=0.08)
        self.draw()

    def get_figure(self):
        return self._fig


# ============================================================
# AnalysisWorker — 后台数据获取与分析线程
# ============================================================
class AnalysisWorker(QThread):
    """在后台线程执行数据获取和分析，避免阻塞 UI"""

    progress = pyqtSignal(str)
    finished = pyqtSignal(dict)
    error = pyqtSignal(str)

    def __init__(self, symbols, market, start, end, demo, parent=None):
        super().__init__(parent)
        self.symbols = symbols
        self.market = market
        self.start = start
        self.end = end
        self.demo = demo

    def run(self):
        try:
            all_data = {}
            all_stats = {}
            all_sr = {}

            for i, sym in enumerate(self.symbols):
                self.progress.emit(f"正在获取数据 {sym} ({i+1}/{len(self.symbols)})...")

                if self.demo:
                    df = generate_sample_data(sym, days=500, base_price=100.0)
                else:
                    df = fetch(sym, start=self.start, end=self.end, market=self.market)

                self.progress.emit(f"正在计算技术指标 {sym}...")
                df = apply_all_indicators(df)
                sr = support_resistance(df)

                self.progress.emit(f"正在统计分析 {sym}...")
                s = descriptive_stats(df)

                all_data[sym] = df
                all_stats[sym] = s
                all_sr[sym] = sr

            corr = None
            if len(self.symbols) > 1:
                self.progress.emit("正在计算相关性矩阵...")
                corr = correlation_matrix(all_data)

            result = {
                "mode": "compare" if len(self.symbols) > 1 else "single",
                "symbols": self.symbols,
                "data": all_data,
                "stats": all_stats,
                "sr": all_sr,
                "corr_matrix": corr,
            }
            self.finished.emit(result)

        except Exception as e:
            self.error.emit(str(e))


# ============================================================
# StatsPanel — 统计数据展示面板
# ============================================================
class StatsPanel(QWidget):
    """显示描述性统计数据的表格面板"""

    HEADERS_CN = [
        "起始价格", "最新价格", "最高价", "最低价",
        "总收益率", "年化收益率", "年化波动率", "夏普比率",
        "最大回撤", "卡尔玛比率", "日均收益率", "日收益率标准差",
        "偏度", "峰度", "正收益天数", "负收益天数",
        "最大单日涨幅", "最大单日跌幅",
    ]

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        title = QLabel("统计指标")
        title.setStyleSheet("font-size: 15px; font-weight: bold; color: #89b4fa; padding: 4px 0;")
        layout.addWidget(title)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["指标", "数值"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.verticalHeader().setVisible(False)
        self._init_rows()
        layout.addWidget(self.table)

    def _init_rows(self):
        self.table.setRowCount(len(self.HEADERS_CN))
        for i, name in enumerate(self.HEADERS_CN):
            item = QTableWidgetItem(name)
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(i, 0, item)

    def update_single(self, stats_dict):
        """更新单只股票统计"""
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["指标", "数值"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self._init_rows()
        for i, name in enumerate(self.HEADERS_CN):
            val = stats_dict.get(name, "N/A")
            item = QTableWidgetItem(str(val))
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(i, 1, item)

    def update_compare(self, stats_dict_map):
        """更新多只股票对比统计"""
        symbols = list(stats_dict_map.keys())
        self.table.setColumnCount(1 + len(symbols))
        headers = ["指标"] + symbols
        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self._init_rows()
        for col_idx, sym in enumerate(symbols):
            stats = stats_dict_map[sym]
            for row_idx, name in enumerate(self.HEADERS_CN):
                val = stats.get(name, "N/A")
                item = QTableWidgetItem(str(val))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row_idx, col_idx + 1, item)


# ============================================================
# QuantGUI — 主窗口
# ============================================================
class QuantGUI(QMainWindow):
    """量化分析系统主界面"""

    def __init__(self):
        super().__init__()
        self._worker = None
        self._current_data = None
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("量化分析系统")
        self.setMinimumSize(1400, 850)
        self.resize(1600, 950)

        # 中央 widget
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(8)

        # --- 左侧面板 ---
        left_panel = self._create_left_panel()
        left_panel.setFixedWidth(240)

        # --- 中间图表区 ---
        self.chart_tabs = self._create_chart_tabs()

        # --- 右侧统计面板 ---
        self.stats_panel = StatsPanel()
        self.stats_panel.setMinimumWidth(280)
        self.stats_panel.setMaximumWidth(360)

        # 用 splitter 让用户可拖拽调整
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(self.chart_tabs)
        splitter.addWidget(self.stats_panel)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setStretchFactor(2, 0)

        main_layout.addWidget(splitter)

        # 状态栏
        self.statusBar().showMessage("就绪  |  输入股票代码后点击 [开始分析]")
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumWidth(200)
        self.progress_bar.setMaximumHeight(16)
        self.progress_bar.setVisible(False)
        self.statusBar().addPermanentWidget(self.progress_bar)

        # 应用样式
        self.setStyleSheet(DARK_THEME)

    # --------------------------------------------------------
    # 左侧面板
    # --------------------------------------------------------
    def _create_left_panel(self):
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(6)

        # 标题
        title = QLabel("量化分析系统")
        title.setStyleSheet(
            "font-size: 18px; font-weight: bold; color: #89b4fa; "
            "padding: 8px 0; border-bottom: 1px solid #45475a; margin-bottom: 8px;"
        )
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # --- 输入区 ---
        group_input = QGroupBox("股票输入")
        g_layout = QVBoxLayout(group_input)
        g_layout.setSpacing(6)

        g_layout.addWidget(QLabel("股票代码"))
        self.input_symbol = QLineEdit()
        self.input_symbol.setPlaceholderText("000001 或 AAPL")
        self.input_symbol.setText("000001")
        g_layout.addWidget(self.input_symbol)

        g_layout.addWidget(QLabel("对比代码 (可选, 逗号分隔)"))
        self.input_compare = QLineEdit()
        self.input_compare.setPlaceholderText("600519, 000858")
        g_layout.addWidget(self.input_compare)

        layout.addWidget(group_input)

        # --- 参数区 ---
        group_params = QGroupBox("分析参数")
        p_layout = QVBoxLayout(group_params)
        p_layout.setSpacing(6)

        p_layout.addWidget(QLabel("市场"))
        self.combo_market = QComboBox()
        self.combo_market.addItems(["自动判断", "A股", "美股", "Demo"])
        p_layout.addWidget(self.combo_market)

        p_layout.addWidget(QLabel("开始日期"))
        self.date_start = QDateEdit()
        self.date_start.setCalendarPopup(True)
        self.date_start.setDisplayFormat("yyyy-MM-dd")
        self.date_start.setDate(QDate.currentDate().addYears(-1))
        p_layout.addWidget(self.date_start)

        p_layout.addWidget(QLabel("结束日期"))
        self.date_end = QDateEdit()
        self.date_end.setCalendarPopup(True)
        self.date_end.setDisplayFormat("yyyy-MM-dd")
        self.date_end.setDate(QDate.currentDate())
        p_layout.addWidget(self.date_end)

        layout.addWidget(group_params)

        # --- 操作按钮 ---
        self.btn_analyze = QPushButton("开始分析")
        self.btn_analyze.setMinimumHeight(44)
        self.btn_analyze.setCursor(Qt.PointingHandCursor)
        self.btn_analyze.clicked.connect(self.on_analyze)
        layout.addWidget(self.btn_analyze)

        # --- 快捷示例 ---
        group_examples = QGroupBox("快捷示例")
        e_layout = QVBoxLayout(group_examples)
        e_layout.setSpacing(4)

        examples = [
            ("Demo 离线测试", "DEMO", "Demo"),
            ("平安银行 (A股)", "000001", "A股"),
            ("贵州茅台 (A股)", "600519", "A股"),
            ("苹果 (美股)", "AAPL", "美股"),
        ]
        for label, sym, market in examples:
            btn = QPushButton(label)
            btn.setStyleSheet(
                "QPushButton { background-color: #313244; color: #cdd6f4; "
                "border: 1px solid #45475a; border-radius: 4px; "
                "padding: 6px; font-size: 12px; font-weight: normal; }"
                "QPushButton:hover { background-color: #45475a; border-color: #89b4fa; }"
            )
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, s=sym, m=market: self._quick_example(s, m))
            e_layout.addWidget(btn)

        layout.addWidget(group_examples)

        # 信息标签
        self.label_info = QLabel("")
        self.label_info.setWordWrap(True)
        self.label_info.setStyleSheet(
            "font-size: 11px; color: #6c7086; padding: 4px; "
            "border-top: 1px solid #45475a; margin-top: 4px;"
        )
        layout.addWidget(self.label_info)

        layout.addStretch()
        return panel

    def _quick_example(self, symbol, market):
        """快捷示例填充"""
        self.input_symbol.setText(symbol)
        self.input_compare.setText("")
        idx = self.combo_market.findText(market)
        if idx >= 0:
            self.combo_market.setCurrentIndex(idx)
        self.on_analyze()

    # --------------------------------------------------------
    # 图表标签页
    # --------------------------------------------------------
    def _create_chart_tabs(self):
        tabs = QTabWidget()

        # K线图 (2行: K线 + 成交量)
        self.canvas_kline = ChartCanvas(nrows=2, ncols=1, height_ratios=[3, 1])
        tabs.addTab(self._wrap_canvas(self.canvas_kline), "K线")

        # MACD (2行: 价格 + MACD)
        self.canvas_macd = ChartCanvas(nrows=2, ncols=1, height_ratios=[2, 1])
        tabs.addTab(self._wrap_canvas(self.canvas_macd), "MACD")

        # RSI
        self.canvas_rsi = ChartCanvas(nrows=1, ncols=1)
        tabs.addTab(self._wrap_canvas(self.canvas_rsi), "RSI")

        # 回撤 (2行: 价格 + 回撤)
        self.canvas_drawdown = ChartCanvas(nrows=2, ncols=1, height_ratios=[2, 1])
        tabs.addTab(self._wrap_canvas(self.canvas_drawdown), "回撤")

        # 收益分布 (1行2列: 直方图 + QQ图)
        self.canvas_returns = ChartCanvas(nrows=1, ncols=2)
        tabs.addTab(self._wrap_canvas(self.canvas_returns), "收益分布")

        # 布林带
        self.canvas_bollinger = ChartCanvas(nrows=1, ncols=1)
        tabs.addTab(self._wrap_canvas(self.canvas_bollinger), "布林带")

        # 相关性矩阵 (多股票时显示)
        self.canvas_corr = ChartCanvas(nrows=1, ncols=1)
        self.corr_tab_index = tabs.addTab(self._wrap_canvas(self.canvas_corr), "相关性")
        tabs.setTabVisible(self.corr_tab_index, False)

        return tabs

    def _wrap_canvas(self, canvas):
        """将 canvas 和 navigation toolbar 包装为 tab 页面"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        toolbar = NavigationToolbar2QT(canvas, self)
        toolbar.setStyleSheet(
            "QToolBar { background-color: #181825; border: none; spacing: 4px; }"
            "QToolButton { background-color: #313244; border: 1px solid #45475a; "
            "border-radius: 3px; padding: 3px; color: #cdd6f4; }"
            "QToolButton:hover { background-color: #45475a; }"
        )
        layout.addWidget(toolbar)
        layout.addWidget(canvas)
        return widget

    # --------------------------------------------------------
    # 分析触发
    # --------------------------------------------------------
    def on_analyze(self):
        """点击分析按钮"""
        symbol = self.input_symbol.text().strip()
        if not symbol:
            QMessageBox.warning(self, "提示", "请输入股票代码")
            return

        symbols = [symbol]
        compare_text = self.input_compare.text().strip()
        if compare_text:
            extra = [s.strip() for s in compare_text.split(",") if s.strip()]
            symbols.extend(extra)

        market_map = {"自动判断": "auto", "A股": "a", "美股": "us", "Demo": "demo"}
        market_text = self.combo_market.currentText()
        market = market_map.get(market_text, "auto")
        demo = market == "demo"
        if demo:
            market = "auto"

        start = self.date_start.date().toString("yyyy-MM-dd")
        end = self.date_end.date().toString("yyyy-MM-dd")

        # 禁用按钮，显示进度
        self.btn_analyze.setEnabled(False)
        self.btn_analyze.setText("分析中...")
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)  # 不确定进度模式

        # 启动后台线程
        self._worker = AnalysisWorker(symbols, market, start, end, demo)
        self._worker.progress.connect(self.on_progress)
        self._worker.finished.connect(self.on_analysis_done)
        self._worker.error.connect(self.on_error)
        self._worker.start()

    def on_progress(self, msg):
        self.statusBar().showMessage(msg)

    def on_error(self, msg):
        self.btn_analyze.setEnabled(True)
        self.btn_analyze.setText("开始分析")
        self.progress_bar.setVisible(False)
        self.statusBar().showMessage(f"错误: {msg}")
        QMessageBox.critical(self, "分析错误", f"分析过程出错:\n\n{msg}")

    def on_analysis_done(self, result):
        """分析完成，绘制所有图表"""
        self._current_data = result
        self.btn_analyze.setEnabled(True)
        self.btn_analyze.setText("开始分析")
        self.progress_bar.setVisible(False)

        symbols = result["symbols"]
        data = result["data"]
        stats = result["stats"]
        sr = result["sr"]
        corr = result["corr_matrix"]

        # 绘制图表 — 使用第一只股票的数据
        primary = symbols[0]
        df = data[primary]

        self.statusBar().showMessage("正在绘制图表...")
        QApplication.processEvents()

        self._draw_kline(df, primary)
        self._draw_macd(df, primary)
        self._draw_rsi(df, primary)
        self._draw_drawdown(df, primary)
        self._draw_returns_dist(df, primary)
        self._draw_bollinger(df, primary)

        # 更新统计面板
        if result["mode"] == "compare":
            self.stats_panel.update_compare(stats)
            # 显示相关性标签页
            self.chart_tabs.setTabVisible(self.corr_tab_index, True)
            if corr is not None:
                self._draw_correlation(corr)
        else:
            self.stats_panel.update_single(stats[primary])
            self.chart_tabs.setTabVisible(self.corr_tab_index, False)

        # 显示支撑阻力信息
        sr_info = sr.get(primary, {})
        support = sr_info.get("support", [])
        resistance = sr_info.get("resistance", [])
        info_parts = []
        if support:
            info_parts.append(f"支撑位: {', '.join(str(round(s, 2)) for s in support)}")
        if resistance:
            info_parts.append(f"阻力位: {', '.join(str(round(r, 2)) for r in resistance)}")

        data_range = f"数据: {df.index[0].date()} ~ {df.index[-1].date()}, {len(df)}条"
        info_parts.append(data_range)
        self.label_info.setText("\n".join(info_parts))

        self.statusBar().showMessage(
            f"分析完成  |  {', '.join(symbols)}  |  "
            f"{df.index[0].date()} ~ {df.index[-1].date()}"
        )

    # --------------------------------------------------------
    # 图表绘制方法 (复制自 visualization/charts.py 的逻辑)
    # --------------------------------------------------------
    def _draw_kline(self, df, symbol):
        """绘制K线图 + 成交量"""
        canvas = self.canvas_kline
        axes = canvas.clear_and_get_axes()
        ax1, ax2 = axes[0], axes[1]

        data = df.tail(120).copy()

        # K线绘制
        up = data[data["close"] >= data["open"]]
        down = data[data["close"] < data["open"]]

        # 阳线 (红)
        ax1.bar(up.index, up["close"] - up["open"], bottom=up["open"],
                width=0.8, color="#ef4444", alpha=0.9)
        ax1.bar(up.index, up["high"] - up["close"], bottom=up["close"],
                width=0.1, color="#ef4444")
        ax1.bar(up.index, up["low"] - up["open"], bottom=up["open"],
                width=0.1, color="#ef4444")

        # 阴线 (绿)
        ax1.bar(down.index, down["close"] - down["open"], bottom=down["open"],
                width=0.8, color="#22c55e", alpha=0.9)
        ax1.bar(down.index, down["high"] - down["open"], bottom=down["open"],
                width=0.1, color="#22c55e")
        ax1.bar(down.index, down["low"] - down["close"], bottom=down["close"],
                width=0.1, color="#22c55e")

        # 均线
        for col, label, color in [
            ("ma5", "MA5", "#f9a825"), ("ma10", "MA10", "#42a5f5"), ("ma20", "MA20", "#ab47bc")
        ]:
            if col in data.columns:
                ax1.plot(data.index, data[col], label=label, linewidth=1, alpha=0.8, color=color)

        ax1.set_title(f"{symbol} K线图", fontsize=14, fontweight="bold")
        ax1.legend(loc="upper left", fontsize=8)
        ax1.grid(True, alpha=0.3)
        ax1.set_ylabel("价格")
        ax1.tick_params(axis="x", rotation=30)

        # 成交量
        colors = ["#ef4444" if c >= o else "#22c55e"
                  for c, o in zip(data["close"], data["open"])]
        ax2.bar(data.index, data["volume"], color=colors, alpha=0.7, width=0.8)
        ax2.set_ylabel("成交量")
        ax2.grid(True, alpha=0.3)
        ax2.tick_params(axis="x", rotation=30)

        canvas.refresh()

    def _draw_macd(self, df, symbol):
        """绘制 MACD"""
        canvas = self.canvas_macd
        axes = canvas.clear_and_get_axes()
        ax1, ax2 = axes[0], axes[1]

        data = df.tail(120).copy()

        ax1.plot(data.index, data["close"], label="收盘价", linewidth=1.2, color="#89b4fa")
        if "ma5" in data.columns:
            ax1.plot(data.index, data["ma5"], label="MA5", linewidth=0.8, alpha=0.7, color="#f9a825")
        if "ma20" in data.columns:
            ax1.plot(data.index, data["ma20"], label="MA20", linewidth=0.8, alpha=0.7, color="#ab47bc")
        ax1.set_title(f"{symbol} MACD", fontsize=14, fontweight="bold")
        ax1.legend(loc="upper left", fontsize=8)
        ax1.grid(True, alpha=0.3)
        ax1.tick_params(axis="x", rotation=30)

        if "dif" in data.columns and "dea" in data.columns:
            ax2.plot(data.index, data["dif"], label="DIF", linewidth=1, color="#89b4fa")
            ax2.plot(data.index, data["dea"], label="DEA", linewidth=1, color="#f9a825")
            colors = ["#ef4444" if v >= 0 else "#22c55e" for v in data["macd"]]
            ax2.bar(data.index, data["macd"], color=colors, alpha=0.6, width=0.8)
            ax2.axhline(y=0, color="#555555", linewidth=0.5)
            ax2.legend(loc="upper left", fontsize=8)
        ax2.grid(True, alpha=0.3)
        ax2.tick_params(axis="x", rotation=30)

        canvas.refresh()

    def _draw_rsi(self, df, symbol):
        """绘制 RSI"""
        canvas = self.canvas_rsi
        axes = canvas.clear_and_get_axes()
        ax = axes[0]

        data = df.tail(120).copy()

        ax.plot(data.index, data["rsi"], label="RSI", linewidth=1.2, color="#ce93d8")
        ax.axhline(y=70, color="#ef4444", linestyle="--", linewidth=0.8, label="超买(70)")
        ax.axhline(y=30, color="#22c55e", linestyle="--", linewidth=0.8, label="超卖(30)")
        ax.axhline(y=50, color="#555555", linestyle="-", linewidth=0.5)
        ax.fill_between(data.index, 70, 100, alpha=0.1, color="#ef4444")
        ax.fill_between(data.index, 0, 30, alpha=0.1, color="#22c55e")
        ax.set_ylim(0, 100)
        ax.set_title(f"{symbol} RSI", fontsize=14, fontweight="bold")
        ax.legend(loc="upper left", fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.tick_params(axis="x", rotation=30)

        canvas.refresh()

    def _draw_drawdown(self, df, symbol):
        """绘制回撤"""
        canvas = self.canvas_drawdown
        axes = canvas.clear_and_get_axes()
        ax1, ax2 = axes[0], axes[1]

        dd = drawdown_series(df)

        ax1.plot(df.index, df["close"], label="收盘价", linewidth=1.2, color="#89b4fa")
        ax1.set_title(f"{symbol} 价格与回撤", fontsize=14, fontweight="bold")
        ax1.legend(loc="upper left", fontsize=8)
        ax1.grid(True, alpha=0.3)
        ax1.tick_params(axis="x", rotation=30)

        ax2.fill_between(dd.index, dd.values, 0, color="#ef4444", alpha=0.4)
        ax2.plot(dd.index, dd.values, color="#ef4444", linewidth=0.8)
        ax2.set_ylabel("回撤")
        ax2.grid(True, alpha=0.3)
        ax2.tick_params(axis="x", rotation=30)

        canvas.refresh()

    def _draw_returns_dist(self, df, symbol):
        """绘制收益率分布"""
        canvas = self.canvas_returns
        axes = canvas.clear_and_get_axes()
        ax1, ax2 = axes[0], axes[1]

        ret = daily_returns(df).dropna()

        # 直方图
        ax1.hist(ret.values, bins=50, density=True, alpha=0.7, color="#6c8ebf",
                 edgecolor="#1e1e2e")
        ax1.axvline(x=ret.mean(), color="#ef4444", linestyle="--",
                    label=f"均值: {ret.mean():.4f}")
        ax1.axvline(x=0, color="#555555", linestyle="-", linewidth=0.5)
        ax1.set_title(f"{symbol} 日收益率分布", fontsize=12, fontweight="bold")
        ax1.set_xlabel("日收益率")
        ax1.set_ylabel("密度")
        ax1.legend(fontsize=8)
        ax1.grid(True, alpha=0.3)

        # QQ图
        scipy_stats.probplot(ret.values, dist="norm", plot=ax2)
        ax2.set_title(f"{symbol} Q-Q图", fontsize=12, fontweight="bold")
        ax2.grid(True, alpha=0.3)

        canvas.refresh()

    def _draw_bollinger(self, df, symbol):
        """绘制布林带"""
        canvas = self.canvas_bollinger
        axes = canvas.clear_and_get_axes()
        ax = axes[0]

        data = df.tail(120).copy()

        ax.plot(data.index, data["close"], label="收盘价", linewidth=1.2, color="#89b4fa")
        ax.plot(data.index, data["boll_mid"], label="中轨", linewidth=0.8, color="#f9a825")
        ax.plot(data.index, data["boll_upper"], label="上轨", linewidth=0.8,
                color="#ef4444", linestyle="--")
        ax.plot(data.index, data["boll_lower"], label="下轨", linewidth=0.8,
                color="#22c55e", linestyle="--")
        ax.fill_between(data.index, data["boll_upper"], data["boll_lower"],
                        alpha=0.1, color="#555555")
        ax.set_title(f"{symbol} 布林带", fontsize=14, fontweight="bold")
        ax.legend(loc="upper left", fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.tick_params(axis="x", rotation=30)

        canvas.refresh()

    def _draw_correlation(self, corr_matrix):
        """绘制相关性热力图"""
        canvas = self.canvas_corr
        axes = canvas.clear_and_get_axes()
        ax = axes[0]

        sns.heatmap(
            corr_matrix, annot=True, fmt=".2f", cmap="RdYlGn",
            center=0, square=True, ax=ax,
            annot_kws={"fontsize": 12, "color": "#1e1e2e"},
            cbar_kws={"shrink": 0.8},
        )
        ax.set_title("收益率相关性矩阵", fontsize=14, fontweight="bold")
        ax.tick_params(axis="x", rotation=30)
        ax.tick_params(axis="y", rotation=0)

        canvas.refresh()

    # --------------------------------------------------------
    # 窗口事件
    # --------------------------------------------------------
    def closeEvent(self, event):
        """关闭窗口时清理线程"""
        if self._worker and self._worker.isRunning():
            self._worker.terminate()
            self._worker.wait(2000)
        event.accept()


# ============================================================
# 入口
# ============================================================
def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Fusion 风格确保 QSS 生效

    # 设置应用字体
    font = QFont("Microsoft YaHei", 9)
    app.setFont(font)

    window = QuantGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
