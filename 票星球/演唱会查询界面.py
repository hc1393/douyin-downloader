import sys
import csv
import requests
import json
from datetime import datetime
import execjs
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QComboBox, QPushButton, QTextEdit, QTableWidget,
                             QTableWidgetItem, QHeaderView, QMessageBox, QProgressBar,
                             QTabWidget)
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class DataFetcher:
    def get_url(self, time):
        try:
            with open('加密参数.js', 'r', encoding='utf-8') as f:
                j = f.read()
                ctx = execjs.compile(j)
                result = ctx.call('JO', time)
            return result
        except Exception as e:
            print(f"获取URL参数时出错: {e}")
            return ""

    def get_cookie(self, time):
        try:
            with open('加密参数.js', 'r', encoding='utf-8') as f:
                j = f.read()
                ctx = execjs.compile(j)
                result = ctx.call('get_cookie_tex', time)
            return result
        except Exception as e:
            print(f"获取Cookie时出错: {e}")
            return ""

    def fetch_cities(self):
        url = "https://m.piaoxingqiu.com/cyy_gatewayapi/home/pub/v3/citys"
        
        params = {
            "lang": "zh",
            "terminalSrc": "WEB",
            "utcOffset": "480",
            "ver": "4.45.3",
            "src": "WEB"
        }
        
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "access-token": "eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkE1LxDAURf_LW3fxkr58dJYjIwqKIMosJUlTKHaakqbgOMx_NzEwS92-e-658C6wnte70HvYcWxgW318nIcAuwvY8bsGcP_w9PEMDayb3d-OkktlNHrfc6YFcaXlwKijzOXmexH1BSNFLXbWWcEZR0SmnRa_2Cm5_zBeba9hypPzNk3XBhYT05jGMJdazlP49HOV6MHyjhCHVmFfJMxxoUyVvCw-mhT-3Gsz6qI3yb-NpzzJlGRtR5yQCZYfEF3uHg_7MnteCtCA_1oqSBol4fUHAAD__w.B0kt3RKBDSLKG_b1jfVTXrwh4Nw4i3Pi1JkHBE8VO_mmN7epR8p_3RzFOaSBv-ZcssNrhcQlgfExiWbTx1HD-MCpCNxOyDd1DiDhDkiOG1Il9ZfoGipRWr6j0GMGXnhAOuJPHBindVg9wHa68Cw_biPD3U2kgMuafiR1vLHD_TM",
            "angry-dog": "41gkqjPgPBO9eDrvV4Cl3-7UNwP6er0fTzjnNjBBQJhczlFMZXBgbk1GF9Xzsf-FUxePhwxI9FgyfY-i1d9e4QYJ3ul61j3y_h8jnffXVlvQVcFWIH4vFgYSVIWldeJbYUZUMW1aQXlnUWROYWNOOQ.WyIxLjAuMCIsIldFQiJd",
            "cache-control": "no-cache",
            "front-trace-id": "mh6fpp3rgos9biahfe",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "src": "WEB",
            "terminal-src": "WEB",
            "utc-offset": "480",
            "ver": "4.45.3"
        }
        
        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            return response.json()
        except Exception as e:
            print(f"获取城市数据时出错: {e}")
            return {}

    def fetch_request(self, cityid):
        try:
            time = int(datetime.now().timestamp()*1000)
            fronttraceid = self.get_url(time)
            cookie = self.get_cookie(time)
            url = "https://m.piaoxingqiu.com/cyy_gatewayapi/home/pub/v3/show_list/search_by_front"

            params = {
                "cityId": cityid,
                "lang": "zh",
                "length": "100",  # 增加获取数量
                "offset": "0",
                "pageIndex": "0",
                "pageLength": "100",  # 增加获取数量
                "pageType": "ALL_PAGE",
                "terminalSrc": "WEB",
                "utcOffset": "480",
                "ver": "4.45.3",
                "src": "WEB"
            }

            headers = {
                "accept": "*/*",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "access-token": "",
                "cache-control": "no-cache",
                "front-trace-id": fronttraceid,
                'cookie': cookie,
                "pragma": "no-cache",
                "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "src": "WEB",
                "terminal-src": "WEB",
                "utc-offset": "480",
                "ver": "4.45.1"
            }

            response = requests.get(url, params=params, headers=headers, timeout=10)
            return response.json()
        except Exception as e:
            print(f"获取演出数据时出错: {e}")
            return {}

    def extract_show_data(self, response_data):
        try:
            extracted_data = []
            # 检查不同的可能数据结构
            search_data = []
            if isinstance(response_data, dict):
                # 尝试多种可能的数据结构路径
                if 'data' in response_data:
                    data_section = response_data['data']
                    if 'searchData' in data_section:
                        search_data = data_section['searchData']
                    elif 'showList' in data_section:
                        search_data = data_section['showList']
                    elif isinstance(data_section, list):
                        search_data = data_section
                elif 'searchData' in response_data:
                    search_data = response_data['searchData']
                elif 'result' in response_data:
                    search_data = response_data['result']
            
            # 如果还没找到数据，直接使用整个响应
            if not search_data and isinstance(response_data, list):
                search_data = response_data
                
            print(f"找到 {len(search_data)} 条演出数据")
            
            for item in search_data:
                if isinstance(item, dict):
                    show_info = {
                        'showName': item.get('showName', ''),
                        'showId': item.get('showId', ''),
                        'stdShowId': item.get('stdShowId', ''),
                        'showDate': item.get('showDate', ''),
                        'cityName': item.get('cityName', ''),
                        'venueId': item.get('venueId', ''),
                        'firstShowTime': item.get('firstShowTime', ''),
                        'lastShowTime': item.get('lastShowTime', ''),
                        'latestShowTime': item.get('latestShowTime', '')
                    }
                    extracted_data.append(show_info)
            return extracted_data
        except Exception as e:
            print(f"提取演出数据时出错: {e}")
            return []

    def fetch_show_detail(self, cityid, showid, siteid):
        try:
            url = 'https://m.piaoxingqiu.com/cyy_gatewayapi/show/pub/v5/show/'+showid+'/static'

            params = {
                "lang": "zh",
                "terminalSrc": "WEB",
                "utcOffset": "480",
                "ver": "4.45.3",
                "src": "WEB",
                "cityId": cityid,
                "source": "FROM_QUICK_ORDER",
                "siteId": siteid
            }

            headers = {
                "accept": "*/*",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "access-token": "eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkE1LxDAURf_LW3fxkr58dJYjIwqKIMosJUlTKHaakqbgOMx_NzEwS92-e-658C6wnte70HvYcWxgW318nIcAuwvY8bsGcP_w9PEMDayb3d-OkktlNHrfc6YFcaXlwKijzOXmexH1BSNFLXbWWcEZR0SmnRa_2Cm5_zBeba9hypPzNk3XBhYT05jGMJdazlP49HOV6MHyjhCHVmFfJMxxoUyVvCw-mhT-3Gsz6qI3yb-NpzzJlGRtR5yQCZYfEF3uHg_7MnteCtCA_1oqSBol4fUHAAD__w.B0kt3RKBDSLKG_b1jfVTXrwh4Nw4i3Pi1JkHBE8VO_mmN7epR8p_3RzFOaSBv-ZcssNrhcQlgfExiWbTx1HD-MCpCNxOyDd1DiDhDkiOG1Il9ZfoGipRWr6j0GMGXnhAOuJPHBindVg9wHa68Cw_biPD3U2kgMuafiR1vLHD_TM",
                "angry-dog": "XfMaanV2lDr07s5j_tlWOLxe8XBTuuav_aAja31PVpXbLegQfjjjys0Xi8KEd_1pAMX1ERmkvlv8cw2uK2FzlAw5BnlfXKiAc0leclVVKNDQ4L19U1pAgf10UiHML9ahc25ZOWhVNU9iUGVWd2dVYg.WyIxLjAuMCIsIldFQiJd",
                "cache-control": "no-cache",
                "front-trace-id": "mh6eee1g0pvsdggsfax",
                "pragma": "no-cache",
                "sec-ch-ua": "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "src": "WEB",
                "terminal-src": "WEB",
                "utc-offset": "480",
                "ver": "4.45.3"
            }

            response = requests.get(url, params=params, headers=headers, timeout=10)
            return response.json()
        except Exception as e:
            print(f"获取演出详情时出错: {e}")
            return {}


class CityLoaderThread(QThread):
    # 定义信号，用于线程间通信
    data_loaded = pyqtSignal(list)  # 城市数据加载完成信号
    error_occurred = pyqtSignal(str)  # 错误信号

    def __init__(self, parent=None):
        super().__init__(parent)
        self.fetcher = DataFetcher()

    def run(self):
        try:
            # 从CSV文件中加载城市数据
            cities = []
            with open('城市数据.csv', 'r', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cities.append({
                        'cityId': row['cityId'],
                        'cityName': row['cityName'],
                        'siteId': row['siteId']
                    })
            self.data_loaded.emit(cities)
        except Exception as e:
            self.error_occurred.emit(str(e))


class ShowLoaderThread(QThread):
    shows_loaded = pyqtSignal(list)  # 演出数据加载完成信号
    error_occurred = pyqtSignal(str)  # 错误信号

    def __init__(self, city_id, parent=None):
        super().__init__(parent)
        self.city_id = city_id
        self.fetcher = DataFetcher()

    def run(self):
        try:
            response_data = self.fetcher.fetch_request(self.city_id)
            # 打印响应数据以便调试
            # print("API响应数据:", json.dumps(response_data, ensure_ascii=False, indent=2))
            extracted_data = self.fetcher.extract_show_data(response_data)
            self.shows_loaded.emit(extracted_data)
        except Exception as e:
            self.error_occurred.emit(str(e))


class ShowDetailThread(QThread):
    detail_loaded = pyqtSignal(dict)  # 详细信息加载完成信号
    error_occurred = pyqtSignal(str)  # 错误信号

    def __init__(self, city_id, show_id, site_id, parent=None):
        super().__init__(parent)
        self.city_id = city_id
        self.show_id = show_id
        self.site_id = site_id
        self.fetcher = DataFetcher()

    def run(self):
        try:
            detail_data = self.fetcher.fetch_show_detail(self.city_id, self.show_id, self.site_id)
            self.detail_loaded.emit(detail_data)
        except Exception as e:
            self.error_occurred.emit(str(e))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("演唱会查询系统")
        self.setGeometry(100, 100, 1000, 700)
        
        # 初始化UI
        self.init_ui()
        
        # 初始化数据
        self.cities = []
        self.current_shows = []
        self.selected_city = None
        
        # 加载城市数据
        self.load_cities()

    def init_ui(self):
        # 创建主部件和布局
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        # 创建标签页
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)
        
        # 创建查询标签页
        self.create_query_tab()
        
        # 创建结果标签页
        self.create_result_tab()
        
        # 创建详细信息标签页
        self.create_detail_tab()
        
        # 添加状态栏
        self.status_bar = self.statusBar()

    def create_query_tab(self):
        self.query_tab = QWidget()
        layout = QVBoxLayout()
        self.query_tab.setLayout(layout)
        
        # 城市选择区域
        city_layout = QHBoxLayout()
        city_label = QLabel("选择城市:")
        self.city_combo = QComboBox()
        self.city_combo.setMinimumWidth(200)
        refresh_btn = QPushButton("刷新城市列表")
        refresh_btn.clicked.connect(self.load_cities)
        
        city_layout.addWidget(city_label)
        city_layout.addWidget(self.city_combo)
        city_layout.addWidget(refresh_btn)
        city_layout.addStretch()
        
        # 查询按钮
        self.query_btn = QPushButton("查询演唱会")
        self.query_btn.clicked.connect(self.query_shows)
        self.query_btn.setEnabled(False)  # 初始禁用，等城市数据加载完成后再启用
        
        # 进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        
        # 添加控件到布局
        layout.addLayout(city_layout)
        layout.addWidget(self.query_btn)
        layout.addWidget(self.progress_bar)
        layout.addStretch()
        
        self.tab_widget.addTab(self.query_tab, "查询")

    def create_result_tab(self):
        self.result_tab = QWidget()
        layout = QVBoxLayout()
        self.result_tab.setLayout(layout)
        
        # 演出表格
        self.shows_table = QTableWidget()
        self.shows_table.setColumnCount(7)
        self.shows_table.setHorizontalHeaderLabels([
            "演出名称", "演出ID", "演出日期", "城市", 
            "场馆ID", "首次演出时间", "最后演出时间"
        ])
        self.shows_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.shows_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.shows_table.setSelectionMode(QTableWidget.SingleSelection)
        self.shows_table.itemSelectionChanged.connect(self.on_show_selected)
        
        # 查看详情按钮
        self.detail_btn = QPushButton("查看演出详情")
        self.detail_btn.clicked.connect(self.show_detail)
        self.detail_btn.setEnabled(False)
        
        layout.addWidget(QLabel("演出列表:"))
        layout.addWidget(self.shows_table)
        layout.addWidget(self.detail_btn)
        
        self.tab_widget.addTab(self.result_tab, "演出列表")

    def create_detail_tab(self):
        self.detail_tab = QWidget()
        layout = QVBoxLayout()
        self.detail_tab.setLayout(layout)
        
        # 详细信息文本框
        self.detail_text = QTextEdit()
        self.detail_text.setReadOnly(True)
        
        layout.addWidget(QLabel("演出详细信息:"))
        layout.addWidget(self.detail_text)
        
        self.tab_widget.addTab(self.detail_tab, "详细信息")

    def load_cities(self):
        """加载城市数据"""
        self.status_bar.showMessage("正在加载城市数据...")
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)  # 设置为忙碌状态
        
        # 启动城市加载线程
        self.city_loader_thread = CityLoaderThread()
        self.city_loader_thread.data_loaded.connect(self.on_cities_loaded)
        self.city_loader_thread.error_occurred.connect(self.on_city_load_error)
        self.city_loader_thread.start()

    def on_cities_loaded(self, cities):
        """城市数据加载完成"""
        self.cities = cities
        self.city_combo.clear()
        
        for city in cities:
            self.city_combo.addItem(city['cityName'], city)
        
        self.query_btn.setEnabled(True)
        self.progress_bar.setVisible(False)
        self.status_bar.showMessage("城市数据加载完成", 3000)

    def on_city_load_error(self, error_msg):
        """城市数据加载出错"""
        self.progress_bar.setVisible(False)
        self.status_bar.showMessage("城市数据加载失败", 3000)
        QMessageBox.critical(self, "错误", f"加载城市数据时出错: {error_msg}")

    def query_shows(self):
        """查询演唱会"""
        index = self.city_combo.currentIndex()
        if index >= 0:
            self.selected_city = self.city_combo.currentData()
            city_id = self.selected_city['cityId']
            
            self.status_bar.showMessage("正在查询演出信息...")
            self.progress_bar.setVisible(True)
            self.progress_bar.setRange(0, 0)  # 设置为忙碌状态
            
            # 启动演出加载线程
            self.show_loader_thread = ShowLoaderThread(city_id)
            self.show_loader_thread.shows_loaded.connect(self.on_shows_loaded)
            self.show_loader_thread.error_occurred.connect(self.on_show_load_error)
            self.show_loader_thread.start()

    def on_shows_loaded(self, shows):
        """演出数据加载完成"""
        try:
            self.current_shows = shows
            self.shows_table.setRowCount(len(shows))
            
            print(f"准备显示 {len(shows)} 条演出数据")
            
            for row, show in enumerate(shows):
                # 使用 get 方法安全地获取字段值，并确保转换为字符串
                self.shows_table.setItem(row, 0, QTableWidgetItem(str(show.get('showName', '') or '')))
                self.shows_table.setItem(row, 1, QTableWidgetItem(str(show.get('showId', '') or '')))
                self.shows_table.setItem(row, 2, QTableWidgetItem(str(show.get('showDate', '') or '')))
                self.shows_table.setItem(row, 3, QTableWidgetItem(str(show.get('cityName', '') or '')))
                self.shows_table.setItem(row, 4, QTableWidgetItem(str(show.get('venueId', '') or '')))
                self.shows_table.setItem(row, 5, QTableWidgetItem(str(show.get('firstShowTime', '') or '')))
                self.shows_table.setItem(row, 6, QTableWidgetItem(str(show.get('lastShowTime', '') or '')))
            
            self.progress_bar.setVisible(False)
            self.status_bar.showMessage(f"查询完成，共找到 {len(shows)} 场演出", 3000)
            
            # 切换到结果标签页
            self.tab_widget.setCurrentWidget(self.result_tab)
        except Exception as e:
            self.progress_bar.setVisible(False)
            self.status_bar.showMessage("处理演出数据时出错", 3000)
            QMessageBox.critical(self, "错误", f"处理演出数据时出错: {str(e)}")
            import traceback
            traceback.print_exc()

    def on_show_load_error(self, error_msg):
        """演出数据加载出错"""
        self.progress_bar.setVisible(False)
        self.status_bar.showMessage("演出数据查询失败", 3000)
        QMessageBox.critical(self, "错误", f"查询演出数据时出错: {error_msg}")

    def on_show_selected(self):
        """当选中某场演出时"""
        selected_rows = self.shows_table.selectionModel().selectedRows()
        self.detail_btn.setEnabled(len(selected_rows) > 0)

    def show_detail(self):
        """显示演出详情"""
        selected_rows = self.shows_table.selectionModel().selectedRows()
        if not selected_rows:
            return
            
        row = selected_rows[0].row()
        show = self.current_shows[row]
        
        if not self.selected_city:
            QMessageBox.warning(self, "警告", "请先选择城市")
            return
            
        show_id = show.get('showId')
        city_id = self.selected_city['cityId']
        site_id = self.selected_city['siteId']
        
        if not show_id:
            QMessageBox.warning(self, "警告", "选中的演出信息不完整")
            return
        
        self.status_bar.showMessage("正在获取演出详细信息...")
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)  # 设置为忙碌状态
        
        # 启动详情加载线程
        self.detail_thread = ShowDetailThread(city_id, show_id, site_id)
        self.detail_thread.detail_loaded.connect(self.on_detail_loaded)
        self.detail_thread.error_occurred.connect(self.on_detail_load_error)
        self.detail_thread.start()

    def on_detail_loaded(self, detail_data):
        """详情数据加载完成"""
        try:
            # 格式化JSON数据并显示
            formatted_json = json.dumps(detail_data, ensure_ascii=False, indent=2)
            self.detail_text.setPlainText(formatted_json)
            
            self.progress_bar.setVisible(False)
            self.status_bar.showMessage("详细信息加载完成", 3000)
            
            # 切换到详情标签页
            self.tab_widget.setCurrentWidget(self.detail_tab)
        except Exception as e:
            self.progress_bar.setVisible(False)
            self.status_bar.showMessage("处理详细信息时出错", 3000)
            QMessageBox.critical(self, "错误", f"处理详细信息时出错: {str(e)}")

    def on_detail_load_error(self, error_msg):
        """详情数据加载出错"""
        self.progress_bar.setVisible(False)
        self.status_bar.showMessage("详细信息加载失败", 3000)
        QMessageBox.critical(self, "错误", f"加载详细信息时出错: {error_msg}")


def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"程序运行时出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()