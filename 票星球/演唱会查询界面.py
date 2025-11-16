import sys
import csv
import requests
import json
from datetime import datetime, timedelta
import execjs
import time
import random

from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QPushButton, QTextEdit, QTableWidget,
                             QTableWidgetItem, QHeaderView, QMessageBox, QProgressBar,
                             QTabWidget, QFileDialog, QLineEdit, QGroupBox, QLCDNumber, QSizePolicy,
                             QSpinBox, QDateTimeEdit, QCheckBox)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QDateTime, QTimer

# 全局access_token变量
ACCESS_TOKEN ='eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkE1LAzEQhv_LnPeQSfPZ40pFQRGKRTxJsjsLi3azJClYS_-7iQGPep153udl5gLpnG7CSLDlrINToni_TAG2F_DzV1vA7d3D2yN0kE6-_x0qrrQzjGjkaKTg2qgJhRWFK8lDFY0VE1psmPWDlxw5YwzNYOQPdszDfxhvtn34qJX94XW3h2sHq4t5znNYarIgObzT0jwWmZWjx8nKiaqHKaeEap6nlaLL4c_KTUGHSC7T83wsrajLpVYotEqUD6U4lOzLrq-157UCHdDn2kBtkKG9fgMAAP__.eljFNr8ShQyET7qX5UjKIAK4VFoXdufS4LsIoZ5WELrPxhVC57s4GPPPKTzxFUl4k174dzfkLUqV7UIBjt69YY8K2FMGjr5agKlDJOKG9FcO3Uaw23245OtP24GKE4YPnHM7rtLXHzB8FfPTSJ9A6goisrKqp-e4lbiWWE7S13U'
def base36encode(number):
    """
    将整数转换为36进制字符串
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("Number must be a non-negative integer")

    if number == 0:
        return "0"

    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = ""

    while number:
        number, i = divmod(number, 36)
        result = alphabet[i] + result

    return result


def generate_front_trace_id():
    """
    生成front-trace-id，模拟JavaScript中的JO函数:
    function JO() {
        return Date.now().toString(36) + Math.random().toString(36).substring(2)
    }
    """
    # 获取当前时间戳(毫秒)
    timestamp = int(time.time() * 1000)
    timestamp_36 = base36encode(timestamp)

    # 生成随机数部分
    random_value = random.random()
    random_str = ""
    temp = random_value

    for _ in range(12):  # 限制长度
        temp *= 36
        digit = int(temp)
        random_str += "0123456789abcdefghijklmnopqrstuvwxyz"[digit]
        temp -= digit
        if temp == 0:
            break

    # 去掉"0."前缀
    random_part = random_str[2:] if random_str.startswith("0.") else random_str

    return timestamp_36 + random_part


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
            "access-token": ACCESS_TOKEN,
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
            time = int(datetime.now().timestamp() * 1000)
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
                "access-token": ACCESS_TOKEN,
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
            url = 'https://m.piaoxingqiu.com/cyy_gatewayapi/show/pub/v5/show/' + showid + '/static'

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
                "access-token": ACCESS_TOKEN,
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

    def fetch_show_sessions(self, show_id, access_token):
        """获取演出场次信息"""
        try:
            # 生成front-trace-id
            time = int(datetime.now().timestamp() * 1000)
            fronttraceid = self.get_url(time)

            url = f'https://m.piaoxingqiu.com/cyy_gatewayapi/show/pub/v5/show/{show_id}/sessions'

            params = {
                "lang": "zh",
                "terminalSrc": "WEB",
                "utcOffset": "480",
                "ver": "4.45.3",
                "src": "WEB",
                "source": "FROM_QUICK_ORDER",
                "isQueryShowBasicInfo": "true"
            }

            headers = {
                "accept": "*/*",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "access-token": access_token,
                "angry-dog": "c23_5vKQMIPGArOqgMpOmn5JNCsJ7gPGnyo5ZmwiZfY29FcpEWCibFNX6HdPfbs-rKFV9-A-tZsgTvOwQlI0g3h4LN3IoRx5CT2EJs4SSzqWsNyCWpuFDDuqBAyI6VTuNU5Od0lJTWFGemN2V3dEbw.WyIxLjAuMCIsIldFQiJd",
                "cache-control": "no-cache",
                "front-trace-id": fronttraceid,
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
                "ver": "4.45.3"
            }

            response = requests.get(url, params=params, headers=headers, timeout=10)
            return response.json()
        except Exception as e:
            print(f"获取演出场次信息时出错: {e}")
            raise

    def fetch_pre_order_info(self, show_id, session_id, seat_plan_id, ticket_price, access_token):
        """获取预下单信息，包括观众信息"""
        try:
            url = "https://m.piaoxingqiu.com/cyy_gatewayapi/trade/buyer/order/v5/pre_order"

            params = {
                "lang": "zh",
                "terminalSrc": "WEB",
                "utcOffset": "480",
                "ver": "4.45.3"
            }

            headers = {
                "accept": "*/*",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "access-token": access_token,
                "angry-dog": "rJaEnCS0Vmd1KaKMTgEoWEHoWk7zyWWqWIqmLQmDkBhwil_oUympYG-EHrzswhUh_Edju6vFNv2-MvFsgBP3LJJjvu7Ws_r-BY8PZh7qgASmoSCOTdLy4bxhtGEZp3dmc3o5Mzh0U0xRUmNObGdBbg.WyIxLjAuMCIsIldFQiJd",
                "cache-control": "no-cache",
                "content-type": "application/json",
                "front-trace-id": generate_front_trace_id(),
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
                "ver": "4.45.3"
            }

            order_data = {
                "src": "WEB",
                "ver": "4.45.3",
                "priorityId": "",
                "items": [
                    {
                        "sku": {
                            "skuId": seat_plan_id,
                            "skuType": "SINGLE",
                            "ticketPrice": ticket_price,
                            "qty": 1,
                            "ticketItems": []
                        },
                        "spu": {
                            "showId": show_id,
                            "sessionId": session_id
                        }
                    }
                ],
                "orderSource": "COMMON"
            }

            response = requests.post(url, params=params, headers=headers, json=order_data, timeout=10)
            return response.json()
        except Exception as e:
            print(f"获取预下单信息时出错: {e}")
            raise

    def fetch_user_audiences(self, show_id, access_token):
        """获取用户观众信息"""
        try:
            # 生成front-trace-id
            time = int(datetime.now().timestamp() * 1000)
            fronttraceid = self.get_url(time)

            url = "https://m.piaoxingqiu.com/cyy_gatewayapi/user/buyer/v3/user_audiences"

            params = {
                "idTypes": "",
                "lang": "zh",
                "length": "500",
                "offset": "0",
                "showId": show_id,
                "terminalSrc": "WEB",
                "utcOffset": "480",
                "ver": "4.45.3",
                "src": "WEB"
            }

            headers = {
                "accept": "*/*",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "access-token": access_token,
                "angry-dog": "N5tiqV_kfS1heIyTjKzVdbKhun7TX60fxvcFYOjwv944b7MHXyY3eJQFJ39iQV-eSMQI5TNE28MkB0pe4fbfenPzJkq1qxsz-3nH_LsAjUt1SyUdHSEbp8Zy_7-1xvIzMFZJODdmalo2TE8xZU1lTA.WyIxLjAuMCIsIldFQiJd",
                "cache-control": "no-cache",
                "front-trace-id": fronttraceid,
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
                "ver": "4.45.3"
            }

            response = requests.get(url, params=params, headers=headers, timeout=10)
            result = response.json()
            print(result)
            return result
        except Exception as e:
            print(f"获取用户观众信息时出错: {e}")
            # 返回空数据而不是抛出异常
            return {"statusCode": 200, "data": [], "pagination": {"count": 0, "offset": 0, "length": 500, "countable": True, "sortingConditions": [], "pageSize": 500, "total": 0, "pageNo": 1}}

    def create_order(self, order_data, access_token):
        """创建订单"""
        try:
            url = "https://m.piaoxingqiu.com/cyy_gatewayapi/trade/buyer/order/v5/create_order"

            params = {
                "lang": "zh",
                "terminalSrc": "WEB",
                "utcOffset": "480",
                "ver": "4.45.3"
            }

            headers = {
                "accept": "*/*",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "access-token": access_token,
                "angry-dog": "O_DHmB8Kas0ET-3IGtMUV2B1m10VzM-QYNff3rEyJSJElB2Xzx68-yESNWBBwd47s_DdEFvHiGobWk9migax5_0jcvT-2BO2-NGQqMFjV8V-AOpC6SsHKcTVLHvi574FbnphMlcyU1RLd05nc29HdA.WyIxLjAuMCIsIldFQiJd",
                "cache-control": "no-cache",
                "content-type": "application/json",
                "front-trace-id": generate_front_trace_id(),
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
                "ver": "4.45.3"
            }

            response = requests.post(url, params=params, headers=headers, json=order_data, timeout=10)
            return response.json()
        except Exception as e:
            print(f"创建订单时出错: {e}")
            raise

    def add_audience_info(self, name, id_no, access_token):
        """添加实名信息"""
        try:
            url = "https://m.piaoxingqiu.com/cyy_gatewayapi/user/buyer/v4/user_audiences"

            params = {
                "lang": "zh",
                "terminalSrc": "WEB",
                "utcOffset": "480",
                "ver": "4.45.3"
            }

            headers = {
                "accept": "*/*",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "access-token": access_token,
                "angry-dog": "IoT5PjcDuSNvxstPpJaUx6dK94SrYBPFaujM4BpGbVFc5JPdz_bKm4HglbdSp-v4r88aRLWAgqp90htEh8pLhigOqa0tDbIm7g_BDZK1aHy9Jp6-3kXvnLsWlEUTmVL4SXRVZXJkaFh2eXlUZWRDbg.WyIxLjAuMCIsIldFQiJd",
                "cache-control": "no-cache",
                "content-type": "application/json",
                "front-trace-id": generate_front_trace_id(),
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
                "ver": "4.45.3"
            }

            audience_data = {
                "src": "WEB",
                "ver": "4.45.3",
                "bizCode": "FHL_M",
                "name": name,
                "idType": "ID_CARD",
                "idNo": id_no
            }

            response = requests.post(url, params=params, headers=headers, json=audience_data, timeout=10)
            return response.json()
        except Exception as e:
            print(f"添加实名信息时出错: {e}")
            raise

    def create_order(self, order_data, access_token):
        """创建订单"""
        try:
            url = "https://m.piaoxingqiu.com/cyy_gatewayapi/trade/buyer/order/v5/create_order"

            params = {
                "lang": "zh",
                "terminalSrc": "WEB",
                "utcOffset": "480",
                "ver": "4.45.3"
            }

            headers = {
                "accept": "*/*",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "access-token": access_token,
                "angry-dog": "O_DHmB8Kas0ET-3IGtMUV2B1m10VzM-QYNff3rEyJSJElB2Xzx68-yESNWBBwd47s_DdEFvHiGobWk9migax5_0jcvT-2BO2-NGQqMFjV8V-AOpC6SsHKcTVLHvi574FbnphMlcyU1RLd05nc29HdA.WyIxLjAuMCIsIldFQiJd",
                "cache-control": "no-cache",
                "content-type": "application/json",
                "front-trace-id": generate_front_trace_id(),
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
                "ver": "4.45.3"
            }

            response = requests.post(url, params=params, headers=headers, json=order_data, timeout=10)
            return response.json()
        except Exception as e:
            print(f"创建订单时出错: {e}")
            raise


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


class OrderSubmitThread(QThread):
    # 定义信号，用于线程间通信
    order_result = pyqtSignal(object)  # 订单结果信号
    order_error = pyqtSignal(str)      # 错误信号
    countdown_updated = pyqtSignal(str)  # 倒计时更新信号
    time_updated = pyqtSignal(str)     # 时间更新信号
    log_message = pyqtSignal(str)      # 日志消息信号

    def __init__(self, order_data, access_token, thread_count=1, parent=None):
        super().__init__(parent)
        self.order_data = order_data
        self.access_token = access_token
        self.thread_count = thread_count
        self.fetcher = DataFetcher()
        self.is_running = True
        self.countdown_time = 0  # 倒计时时间（秒）

    def set_countdown(self, seconds):
        """设置倒计时时间"""
        self.countdown_time = seconds

    def stop(self):
        """停止线程"""
        self.is_running = False

    def run(self):
        try:
            # 如果设置了倒计时，则先倒计时
            if self.countdown_time > 0:
                for i in range(self.countdown_time, 0, -1):
                    if not self.is_running:
                        return
                    # 发送倒计时更新信号
                    self.countdown_updated.emit(f"倒计时: {i} 秒")
                    # 发送当前时间更新信号
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.time_updated.emit(current_time)
                    # 等待1秒
                    self.msleep(1000)
            
            # 倒计时结束后，发送当前时间更新信号
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.time_updated.emit(current_time)
            
            # 检查是否需要继续执行
            if not self.is_running:
                return
            
            # 持续提交订单直到停止
            success_count = 0
            error_count = 0
            
            self.log_message.emit(f"开始提交订单，使用 {self.thread_count} 个线程")
            
            while self.is_running:
                try:
                    # 调用创建订单API
                    result = self.fetcher.create_order(self.order_data, self.access_token)
                    success_count += 1
                    self.log_message.emit(f"订单提交成功 #{success_count}: {json.dumps(result, ensure_ascii=False)[:100]}...")
                    # 发送订单结果信号
                    self.order_result.emit(result)
                    # 等待一小段时间避免请求过于频繁
                    self.msleep(100)
                except Exception as e:
                    error_count += 1
                    self.log_message.emit(f"订单提交错误 #{error_count}: {str(e)}")
                    # 发送错误信号
                    self.order_error.emit(str(e))
                    # 继续尝试而不是退出
                    self.msleep(1000)  # 出错后等待更长时间
                    
            self.log_message.emit(f"订单提交已停止。成功: {success_count}, 失败: {error_count}")
        except Exception as e:
            # 发送错误信号
            self.order_error.emit(str(e))
            self.log_message.emit(f"线程异常: {str(e)}")


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

        # 订单提交线程
        self.order_thread = None
        self.order_threads = []  # 多线程列表

        # 启动时间更新定时器
        self.time_timer = QTimer(self)
        self.time_timer.timeout.connect(self.update_current_time)
        self.time_timer.start(1000)  # 每秒更新一次

        # 加载城市数据
        self.load_cities()

    def create_order_tab(self):
        """创建订单输出界面"""
        self.order_tab = QWidget()
        layout = QVBoxLayout()
        self.order_tab.setLayout(layout)
        
        # 订单信息显示区域
        self.order_info_label = QLabel("订单信息:")
        self.order_info_text = QTextEdit()
        self.order_info_text.setReadOnly(True)
        
        # 订单结果区域
        self.order_result_label = QLabel("订单结果:")
        self.order_result_text = QTextEdit()
        self.order_result_text.setReadOnly(True)
        
        layout.addWidget(self.order_info_label)
        layout.addWidget(self.order_info_text)
        layout.addWidget(self.order_result_label)
        layout.addWidget(self.order_result_text)
        
        self.tab_widget.addTab(self.order_tab, "订单输出")

    def create_log_tab(self):
        """创建日志输出界面"""
        self.log_tab = QWidget()
        layout = QVBoxLayout()
        self.log_tab.setLayout(layout)
        
        # 日志显示区域
        self.log_label = QLabel("运行日志:")
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        
        layout.addWidget(self.log_label)
        layout.addWidget(self.log_text)
        
        self.tab_widget.addTab(self.log_tab, "运行日志")

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
        
        # 创建演出数据展示标签页
        self.create_show_data_tab()
        
        # 创建演出场次信息标签页
        self.create_show_sessions_tab()
        
        # 创建观众信息标签页
        self.create_audience_tab()
        
        # 创建订单输出标签页
        self.create_order_tab()
        
        # 创建日志标签页
        self.create_log_tab()
        
        # 添加状态栏
        self.status_bar = self.statusBar()
        
        # 初始化演出数据
        self.show_data = []

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

    def update_sessions_show_list(self, shows):
        """更新演出场次标签页中的演出选择列表"""
        self.sessions_show_combo.clear()
        for show in shows:
            if isinstance(show, dict):
                show_name = show.get("showName", "")
                show_id = show.get("showId", "")
                if show_name and show_id:
                    # 在下拉列表中显示演出名称，但将完整的演出数据作为选项数据
                    self.sessions_show_combo.addItem(show_name, show)

    def update_current_time(self):
        """更新当前时间显示"""
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        # 如果在观众信息标签页，更新那里的时间显示
        if hasattr(self, 'audience_tab') and self.tab_widget.currentWidget() == self.audience_tab:
            if hasattr(self, 'current_time_display'):
                self.current_time_display.setText(current_time)

    def create_show_data_tab(self):
        self.show_data_tab = QWidget()
        layout = QVBoxLayout()
        self.show_data_tab.setLayout(layout)

        # 演出数据表格
        self.show_data_table = QTableWidget()
        self.show_data_table.setColumnCount(8)
        self.show_data_table.setHorizontalHeaderLabels([
            "演出ID", "演出名称", "演出日期", "城市",
            "状态", "最新销售时间", "海报链接", "状态标签"
        ])
        self.show_data_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.show_data_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.show_data_table.setSelectionMode(QTableWidget.SingleSelection)

        # 按钮布局
        button_layout = QHBoxLayout()
        self.load_show_data_btn = QPushButton("加载演出数据")
        self.load_show_data_btn.clicked.connect(self.load_show_data)
        self.export_show_data_btn = QPushButton("导出为CSV")
        self.export_show_data_btn.clicked.connect(self.export_show_data_to_csv)
        self.export_show_data_btn.setEnabled(False)
        button_layout.addWidget(self.load_show_data_btn)
        button_layout.addWidget(self.export_show_data_btn)
        button_layout.addStretch()

        layout.addLayout(button_layout)
        layout.addWidget(QLabel("演出数据:"))
        layout.addWidget(self.show_data_table)

        self.tab_widget.addTab(self.show_data_tab, "演出数据")

    def load_show_data(self):
        """加载演出数据到表格"""
        # 解析详细信息标签页中的JSON数据
        detail_text = self.detail_text.toPlainText()
        if not detail_text:
            QMessageBox.warning(self, "警告", "请先查询并查看演出详情")
            return

        try:
            detail_data = json.loads(detail_text)
            shows_data = []

            # 从详细信息中提取演出数据
            shows = []
            # 检查不同的可能数据结构路径
            if isinstance(detail_data, dict):
                if 'data' in detail_data:
                    if isinstance(detail_data['data'], dict):
                        # 检查是否有basicInfo
                        if 'basicInfo' in detail_data['data']:
                            # 检查是否有巡演信息
                            if 'tour' in detail_data['data'] and 'shows' in detail_data['data']['tour']:
                                # 巡演信息格式
                                shows = detail_data['data']['tour']['shows']
                            else:
                                # 单个演出信息格式
                                shows = [detail_data['data']]
                        elif 'tour' in detail_data['data'] and 'shows' in detail_data['data']['tour']:
                            # 巡演信息格式
                            shows = detail_data['data']['tour']['shows']
                        elif 'shows' in detail_data['data']:
                            shows = detail_data['data']['shows']
                    elif isinstance(detail_data['data'], list):
                        # 如果data直接是数组
                        shows = detail_data['data']
                elif 'shows' in detail_data:
                    shows = detail_data['shows']
                elif 'tour' in detail_data and 'shows' in detail_data['tour']:
                    # 巡演信息格式（顶层）
                    shows = detail_data['tour']['shows']

            # 如果还没找到数据，直接使用整个响应作为单个演出
            if not shows and isinstance(detail_data, dict):
                shows = [detail_data]

            print(f"找到 {len(shows)} 条演出数据")

            for show in shows:
                if isinstance(show, dict):
                    # 根据数据结构提取信息
                    if 'showId' in show:
                        # 巡演场次数据
                        show_info = {
                            "showId": show.get("showId", ""),
                            "showName": show.get("showName", ""),
                            "showDate": show.get("showDate", ""),
                            "cityName": show.get("cityName", ""),
                            "showStatus": show.get("showStatus", "ONSALE"),
                            "existLatestSaleTime": show.get("existLatestSaleTime", False),
                            "posterUrl": show.get("posterUrl", ""),
                            "showStatusTag": show.get("showStatusTag", "售票中")
                        }
                    else:
                        # 基本演出信息
                        basic_info = show.get("basicInfo", show)  # 如果有basicInfo则使用，否则使用show本身
                        show_info = {
                            "showId": basic_info.get("bizShowId", basic_info.get("showId", basic_info.get("id", ""))),
                            "showName": basic_info.get("showName", basic_info.get("name", "")),
                            "showDate": basic_info.get("showDate",
                                                       basic_info.get("showTimeDesc", basic_info.get("show_time", ""))),
                            "cityName": basic_info.get("cityName", basic_info.get("city", "")),
                            "showStatus": basic_info.get("showDetailStatus",
                                                         basic_info.get("preSale", False) and "PRESALE" or "ONSALE"),
                            "existLatestSaleTime": basic_info.get("existLatestSaleTime", False),
                            "posterUrl": basic_info.get("posterUrl", basic_info.get("poster", "")),
                            "showStatusTag": basic_info.get("showDetailStatus",
                                                            basic_info.get("preSale", False) and "预订中" or "售票中")
                        }
                    shows_data.append(show_info)

            if not shows_data:
                # 如果仍然没有数据，尝试使用演出列表中的数据
                for row in range(self.shows_table.rowCount()):
                    show_info = {
                        "showId": self.shows_table.item(row, 1).text() if self.shows_table.item(row, 1) else "",
                        "showName": self.shows_table.item(row, 0).text() if self.shows_table.item(row, 0) else "",
                        "showDate": self.shows_table.item(row, 2).text() if self.shows_table.item(row, 2) else "",
                        "cityName": self.shows_table.item(row, 3).text() if self.shows_table.item(row, 3) else "",
                        "showStatus": "ONSALE",
                        "existLatestSaleTime": False,
                        "posterUrl": "",
                        "showStatusTag": "售票中"
                    }
                    shows_data.append(show_info)

            self.display_show_data(shows_data)
            self.export_show_data_btn.setEnabled(True)
        except json.JSONDecodeError as e:
            QMessageBox.critical(self, "错误", f"无法解析演出详情数据，请确保已正确加载详情信息\n错误详情: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"加载演出数据时出错: {str(e)}")
            import traceback
            traceback.print_exc()

    def display_show_data(self, data):
        """在表格中显示演出数据"""
        # 清空现有数据
        self.show_data_table.setRowCount(0)

        # 设置表格行数
        self.show_data_table.setRowCount(len(data))

        # 填充表格数据
        for row, show in enumerate(data):
            if isinstance(show, dict):
                self.show_data_table.setItem(row, 0, QTableWidgetItem(show.get("showId", "")))
                self.show_data_table.setItem(row, 1, QTableWidgetItem(show.get("showName", "")))
                self.show_data_table.setItem(row, 2, QTableWidgetItem(show.get("showDate", "")))
                self.show_data_table.setItem(row, 3, QTableWidgetItem(show.get("cityName", "")))
                self.show_data_table.setItem(row, 4, QTableWidgetItem(show.get("showStatus", "")))
                self.show_data_table.setItem(row, 5, QTableWidgetItem(str(show.get("existLatestSaleTime", ""))))
                self.show_data_table.setItem(row, 6, QTableWidgetItem(show.get("posterUrl", "")))
                self.show_data_table.setItem(row, 7, QTableWidgetItem(show.get("showStatusTag", "")))

        self.show_data = data

        # 更新演出场次标签页中的演出选择列表
        self.update_sessions_show_list(data)

    def export_show_data_to_csv(self):
        """导出演出数据为CSV"""
        try:
            file_path, _ = QFileDialog.getSaveFileName(
                self, "保存CSV文件", "演出数据.csv", "CSV Files (*.csv);;All Files (*)"
            )

            if file_path:
                with open(file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
                    writer = csv.writer(csvfile)

                    # 写入表头
                    headers = ["演出ID", "演出名称", "演出日期", "城市",
                               "状态", "最新销售时间", "海报链接", "状态标签"]
                    writer.writerow(headers)

                    # 写入数据
                    for row in range(self.show_data_table.rowCount()):
                        row_data = []
                        for col in range(self.show_data_table.columnCount()):
                            item = self.show_data_table.item(row, col)
                            row_data.append(item.text() if item else "")
                        writer.writerow(row_data)

                QMessageBox.information(self, "成功", "数据已成功导出为CSV文件")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"导出CSV文件时出错: {str(e)}")

    def create_show_sessions_tab(self):
        self.show_sessions_tab = QWidget()
        layout = QVBoxLayout()
        self.show_sessions_tab.setLayout(layout)

        # 演出选择区域
        show_selection_layout = QHBoxLayout()
        show_selection_label = QLabel("从演出数据中选择:")
        self.sessions_show_combo = QComboBox()
        self.sessions_show_combo.setMinimumWidth(300)
        self.fetch_sessions_btn = QPushButton("获取场次信息")
        self.fetch_sessions_btn.clicked.connect(self.fetch_show_sessions_clicked)
        show_selection_layout.addWidget(show_selection_label)
        show_selection_layout.addWidget(self.sessions_show_combo)
        show_selection_layout.addWidget(self.fetch_sessions_btn)

        # 场次信息表格
        self.sessions_table = QTableWidget()
        self.sessions_table.setColumnCount(6)
        self.sessions_table.setHorizontalHeaderLabels([
            "场次ID", "场次名称", "开始时间", "结束时间", "状态", "是否有票"
        ])
        self.sessions_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.sessions_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.sessions_table.setSelectionMode(QTableWidget.SingleSelection)

        # 座位计划信息表格
        self.seat_plans_table = QTableWidget()
        self.seat_plans_table.setColumnCount(7)
        self.seat_plans_table.setHorizontalHeaderLabels([
            "选择", "座位计划ID", "座位计划名称", "价格", "类别", "是否套票", "限购数量", "套票详情"
        ])
        self.seat_plans_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.seat_plans_table.cellDoubleClicked.connect(self.on_seat_plan_double_clicked)

        # 添加控件到布局
        layout.addLayout(show_selection_layout)
        layout.addWidget(QLabel("场次信息:"))
        layout.addWidget(self.sessions_table)
        layout.addWidget(QLabel("座位计划信息 (双击行获取观众信息):"))
        layout.addWidget(self.seat_plans_table)

        self.tab_widget.addTab(self.show_sessions_tab, "演出场次")

    def create_audience_tab(self):
        self.audience_tab = QWidget()
        layout = QVBoxLayout()
        self.audience_tab.setLayout(layout)

        # 实名信息添加区域
        identity_group = QGroupBox("添加实名信息")
        identity_layout = QVBoxLayout()
        identity_group.setLayout(identity_layout)

        # 姓名输入
        name_layout = QHBoxLayout()
        name_label = QLabel("姓名:")
        self.name_input = QLineEdit()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)

        # 身份证号输入
        id_layout = QHBoxLayout()
        id_label = QLabel("身份证号:")
        self.id_input = QLineEdit()
        id_layout.addWidget(id_label)
        id_layout.addWidget(self.id_input)

        # 添加按钮
        self.add_identity_btn = QPushButton("添加实名信息")
        self.add_identity_btn.clicked.connect(self.add_identity_info)

        identity_layout.addLayout(name_layout)
        identity_layout.addLayout(id_layout)
        identity_layout.addWidget(self.add_identity_btn)

        # 观众信息表格
        self.audience_table = QTableWidget()
        self.audience_table.setColumnCount(9)  # 增加一列显示状态
        self.audience_table.setHorizontalHeaderLabels([
            "ID", "姓名", "身份证号", "证件类型", "年龄", "城市代码", "联系方式", "是否可选", "状态"
        ])
        self.audience_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 选中座位计划信息区域
        self.selected_seat_plan_label = QLabel("选中的座位计划信息:")
        self.selected_seat_plan_info = QTextEdit()
        self.selected_seat_plan_info.setMaximumHeight(100)
        self.selected_seat_plan_info.setReadOnly(True)

        # 获取观众信息按钮
        self.fetch_audience_btn = QPushButton("获取观众信息")
        self.fetch_audience_btn.clicked.connect(self.fetch_audience_info)

        # 提交订单区域
        order_group = QGroupBox("提交订单")
        order_layout = QVBoxLayout()
        order_group.setLayout(order_layout)

        # 倒计时设置
        countdown_layout = QHBoxLayout()
        countdown_label = QLabel("倒计时(秒):")
        self.countdown_input = QLineEdit("0")
        self.countdown_input.setPlaceholderText("输入倒计时秒数，0表示立即提交")
        countdown_layout.addWidget(countdown_label)
        countdown_layout.addWidget(self.countdown_input)
        
        # 线程数设置
        thread_layout = QHBoxLayout()
        thread_label = QLabel("线程数:")
        self.thread_count_spinbox = QSpinBox()
        self.thread_count_spinbox.setMinimum(1)
        self.thread_count_spinbox.setMaximum(100)
        self.thread_count_spinbox.setValue(1)
        thread_layout.addWidget(thread_label)
        thread_layout.addWidget(self.thread_count_spinbox)
        
        # 当前时间显示
        self.current_time_label = QLabel("当前时间:")
        self.current_time_display = QLabel(QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss"))
        time_layout = QHBoxLayout()
        time_layout.addWidget(self.current_time_label)
        time_layout.addWidget(self.current_time_display)
        time_layout.addStretch()

        # 定时提交设置
        schedule_layout = QHBoxLayout()
        schedule_label = QLabel("定时提交:")
        self.schedule_datetime = QDateTimeEdit()
        self.schedule_datetime.setDateTime(QDateTime.currentDateTime().addSecs(60))  # 默认设置为1分钟后
        self.schedule_datetime.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.schedule_datetime.setMinimumDateTime(QDateTime.currentDateTime())
        self.schedule_enable_checkbox = QCheckBox("启用定时提交")
        self.schedule_enable_checkbox.stateChanged.connect(self.toggle_schedule_inputs)
        schedule_layout.addWidget(schedule_label)
        schedule_layout.addWidget(self.schedule_datetime)
        schedule_layout.addWidget(self.schedule_enable_checkbox)

        # 按钮布局
        button_layout = QHBoxLayout()
        self.submit_order_btn = QPushButton("提交订单")
        self.submit_order_btn.clicked.connect(self.create_order)
        self.submit_order_btn.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        
        self.stop_order_btn = QPushButton("停止提交")
        self.stop_order_btn.clicked.connect(self.stop_order_submission)
        self.stop_order_btn.setStyleSheet("background-color: #f44336; color: white; font-weight: bold;")
        self.stop_order_btn.setEnabled(False)
        
        button_layout.addWidget(self.submit_order_btn)
        button_layout.addWidget(self.stop_order_btn)

        # 倒计时显示
        self.countdown_display = QLabel("倒计时: 未开始")
        self.countdown_display.setAlignment(Qt.AlignCenter)
        self.countdown_display.setStyleSheet("font-size: 16px; font-weight: bold; color: #2196F3;")

        # 添加控件到订单布局
        order_layout.addLayout(countdown_layout)
        order_layout.addLayout(thread_layout)
        order_layout.addLayout(time_layout)
        order_layout.addLayout(schedule_layout)
        order_layout.addWidget(self.countdown_display)
        order_layout.addLayout(button_layout)

        # 添加控件到布局
        layout.addWidget(identity_group)
        layout.addWidget(self.selected_seat_plan_label)
        layout.addWidget(self.selected_seat_plan_info)
        layout.addWidget(self.fetch_audience_btn)
        layout.addWidget(QLabel("观众信息:"))
        layout.addWidget(self.audience_table)
        layout.addWidget(order_group)

        self.tab_widget.addTab(self.audience_tab, "观众信息")

    def on_seat_plan_double_clicked(self, row, column):
        """当座位计划表格被双击时，获取对应的观众信息"""
        self.fetch_audience_info_from_seat_plan(row)

    def fetch_audience_info_from_seat_plan(self, seat_plan_row):
        """从座位计划获取观众信息"""
        # 获取选中的座位计划信息
        if seat_plan_row < 0:
            QMessageBox.warning(self, "警告", "请选择一个座位计划")
            return

        # 获取座位计划ID和价格
        seat_plan_id_item = self.seat_plans_table.item(seat_plan_row, 1)  # ID在第1列（原来是第0列）
        seat_plan_name_item = self.seat_plans_table.item(seat_plan_row, 2)  # 名称在第2列（原来是第1列）
        seat_plan_price_item = self.seat_plans_table.item(seat_plan_row, 3)  # 价格在第3列（原来是第2列）

        # 获取选中的场次信息（不是默认第一个，而是用户选择的场次）
        selected_session_row = self.sessions_table.currentRow()
        if selected_session_row < 0:
            # 如果没有选中场次，默认使用第一个场次
            session_id_item = self.sessions_table.item(0, 0)
            # 提示用户最好选择一个场次
            QMessageBox.information(self, "提示", "未选择场次，默认使用第一个场次")
        else:
            session_id_item = self.sessions_table.item(selected_session_row, 0)

        if not (seat_plan_id_item and seat_plan_name_item and seat_plan_price_item and session_id_item):
            QMessageBox.warning(self, "警告", "座位计划或场次信息不完整")
            return

        seat_plan_id = seat_plan_id_item.text() if seat_plan_id_item else ""
        seat_plan_name = seat_plan_name_item.text() if seat_plan_name_item else ""
        seat_plan_price = seat_plan_price_item.text() if seat_plan_price_item else ""
        session_id = session_id_item.text() if session_id_item else ""

        # 获取演出ID
        selected_show = self.sessions_show_combo.currentData()
        show_id = selected_show.get('showId') if selected_show else None

        if not show_id:
            QMessageBox.warning(self, "警告", "演出信息不完整")
            return

        # 显示选中的座位计划信息
        info_text = f"座位计划名称: {seat_plan_name}\n座位计划ID: {seat_plan_id}\n价格: {seat_plan_price}\n场次ID: {session_id}\n演出ID: {show_id}"
        self.selected_seat_plan_info.setPlainText(info_text)

        # 从价格文本中提取数字
        import re
        price_match = re.search(r'(\d+\.?\d*)', seat_plan_price.replace(',', ''))
        if price_match:
            ticket_price = float(price_match.group(1))
        else:
            # 如果无法提取价格，使用默认值0
            ticket_price = 0.0

        # 调用预下单API获取观众信息
        try:
            fetcher = DataFetcher()
            access_token = ACCESS_TOKEN

            # 调用预下单API获取观众信息
            data = fetcher.fetch_pre_order_info(show_id, session_id, seat_plan_id, ticket_price, access_token)
            self.display_audience_data(data)
            
            # 如果没有获取到观众信息，尝试通过用户观众接口获取
            audiences = []
            if isinstance(data, dict) and 'data' in data:
                if isinstance(data['data'], dict) and 'audiences' in data['data']:
                    audiences = data['data']['audiences']
                elif isinstance(data['data'], list):
                    audiences = data['data']
            
            if not audiences:
                try:
                    QMessageBox.information(self, "提示", "预下单未返回观众信息，正在尝试通过用户观众接口获取...")
                    user_audiences_data = fetcher.fetch_user_audiences(show_id, access_token)
                    self.display_audience_data(user_audiences_data)
                except Exception as e2:
                    QMessageBox.critical(self, "错误", f"获取观众信息时出错: {str(e2)}")
            else:
                # 切换到观众信息标签页
                self.tab_widget.setCurrentWidget(self.audience_tab)
                
        except Exception as e:
            # 如果预下单获取观众信息失败，则尝试通过用户观众接口获取
            try:
                QMessageBox.information(self, "提示", f"预下单获取观众信息失败: {str(e)}，正在尝试通过用户观众接口获取...")
                data = fetcher.fetch_user_audiences(show_id, access_token)
                self.display_audience_data(data)
                # 切换到观众信息标签页
                self.tab_widget.setCurrentWidget(self.audience_tab)
            except Exception as e2:
                QMessageBox.critical(self, "错误", f"获取观众信息时出错: {str(e2)}")

    def fetch_audience_info(self):
        """获取观众信息"""
        # 获取选中的座位计划信息
        selected_seat_plan_row = None
        # 查找选中的座位计划（通过复选框）
        for row in range(self.seat_plans_table.rowCount()):
            checkbox_item = self.seat_plans_table.item(row, 0)
            if checkbox_item and checkbox_item.checkState() == Qt.Checked:
                selected_seat_plan_row = row
                break

        # 如果没有通过复选框选择，则检查是否有行被选中
        if selected_seat_plan_row is None:
            current_row = self.seat_plans_table.currentRow()
            if current_row >= 0:
                selected_seat_plan_row = current_row
            else:
                QMessageBox.warning(self, "警告", "请先选择一个座位计划")
                return

        # 获取选中的场次信息
        selected_session_row = self.sessions_table.currentRow()
        if selected_session_row < 0:
            # 如果没有选中场次，默认使用第一个场次
            reply = QMessageBox.question(self, "提示", "未选择场次，默认使用第一个场次，是否继续？",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.No:
                return
            session_id_item = self.sessions_table.item(0, 0)
        else:
            session_id_item = self.sessions_table.item(selected_session_row, 0)

        # 获取座位计划ID和价格
        seat_plan_id_item = self.seat_plans_table.item(selected_seat_plan_row, 1)  # ID在第1列（原来是第0列）
        seat_plan_name_item = self.seat_plans_table.item(selected_seat_plan_row, 2)  # 名称在第2列（原来是第1列）
        seat_plan_price_item = self.seat_plans_table.item(selected_seat_plan_row, 3)  # 价格在第3列（原来是第2列）

        if not (seat_plan_id_item and seat_plan_name_item and seat_plan_price_item and session_id_item):
            QMessageBox.warning(self, "警告", "座位计划或场次信息不完整")
            return

        seat_plan_id = seat_plan_id_item.text() if seat_plan_id_item else ""
        seat_plan_name = seat_plan_name_item.text() if seat_plan_name_item else ""
        seat_plan_price = seat_plan_price_item.text() if seat_plan_price_item else ""
        session_id = session_id_item.text() if session_id_item else ""

        # 获取演出ID
        selected_show = self.sessions_show_combo.currentData()
        show_id = selected_show.get('showId') if selected_show else None

        if not show_id:
            QMessageBox.warning(self, "警告", "演出信息不完整")
            return

        # 显示选中的座位计划信息
        info_text = f"座位计划名称: {seat_plan_name}\n座位计划ID: {seat_plan_id}\n价格: {seat_plan_price}\n场次ID: {session_id}\n演出ID: {show_id}"
        self.selected_seat_plan_info.setPlainText(info_text)

        # 从价格文本中提取数字
        import re
        price_match = re.search(r'(\d+\.?\d*)', seat_plan_price.replace(',', ''))
        if price_match:
            ticket_price = float(price_match.group(1))
        else:
            # 如果无法提取价格，使用默认值0
            ticket_price = 0.0

        # 调用预下单API获取观众信息
        try:
            fetcher = DataFetcher()
            access_token = ACCESS_TOKEN

            # 调用预下单API获取观众信息
            data = fetcher.fetch_pre_order_info(show_id, session_id, seat_plan_id, ticket_price, access_token)
            self.display_audience_data(data)
            
            # 如果没有获取到观众信息，尝试通过用户观众接口获取
            audiences = []
            if isinstance(data, dict) and 'data' in data:
                if isinstance(data['data'], dict) and 'audiences' in data['data']:
                    audiences = data['data']['audiences']
                elif isinstance(data['data'], list):
                    audiences = data['data']
            
            if not audiences:
                try:
                    QMessageBox.information(self, "提示", "预下单未返回观众信息，正在尝试通过用户观众接口获取...")
                    user_audiences_data = fetcher.fetch_user_audiences(show_id, access_token)
                    self.display_audience_data(user_audiences_data)
                except Exception as e2:
                    QMessageBox.critical(self, "错误", f"获取观众信息时出错: {str(e2)}")
            else:
                # 切换到观众信息标签页
                self.tab_widget.setCurrentWidget(self.audience_tab)
                
        except Exception as e:
            # 如果预下单获取观众信息失败，则尝试通过用户观众接口获取
            try:
                QMessageBox.information(self, "提示", f"预下单获取观众信息失败: {str(e)}，正在尝试通过用户观众接口获取...")
                data = fetcher.fetch_user_audiences(show_id, access_token)
                self.display_audience_data(data)
                # 切换到观众信息标签页
                self.tab_widget.setCurrentWidget(self.audience_tab)
            except Exception as e2:
                QMessageBox.critical(self, "错误", f"获取观众信息时出错: {str(e2)}")

    def display_sessions_data(self, data):
        """在表格中显示场次和座位计划信息"""
        # 清空现有数据
        self.sessions_table.setRowCount(0)
        self.seat_plans_table.setRowCount(0)
        
        # 获取场次数据
        sessions = data.get('data', [])
        
        # 显示场次信息
        self.sessions_table.setRowCount(len(sessions))
        for row, session in enumerate(sessions):
            if isinstance(session, dict):
                self.sessions_table.setItem(row, 0, QTableWidgetItem(session.get("bizShowSessionId", "")))
                self.sessions_table.setItem(row, 1, QTableWidgetItem(session.get("sessionName", "")))
                
                # 格式化时间
                begin_time = session.get("beginDateTime", "")
                end_time = session.get("endDateTime", "")
                if begin_time:
                    begin_time = datetime.fromtimestamp(begin_time/1000).strftime('%Y-%m-%d %H:%M')
                if end_time:
                    end_time = datetime.fromtimestamp(end_time/1000).strftime('%Y-%m-%d %H:%M')
                
                self.sessions_table.setItem(row, 2, QTableWidgetItem(begin_time))
                self.sessions_table.setItem(row, 3, QTableWidgetItem(end_time))
                self.sessions_table.setItem(row, 4, QTableWidgetItem(session.get("sessionStatus", "")))
                self.sessions_table.setItem(row, 5, QTableWidgetItem(str(session.get("hasStock", ""))))
        
        # 如果有场次数据，显示第一个场次的座位计划
        if sessions:
            first_session = sessions[0]
            seat_plans = first_session.get("seatPlans", [])
            self.seat_plans_table.setRowCount(len(seat_plans))
            
            for row, seat_plan in enumerate(seat_plans):
                if isinstance(seat_plan, dict):
                    # 添加复选框用于选择座位计划
                    checkbox = QTableWidgetItem()
                    checkbox.setCheckState(Qt.Unchecked)
                    self.seat_plans_table.setItem(row, 0, checkbox)
                    
                    self.seat_plans_table.setItem(row, 1, QTableWidgetItem(seat_plan.get("seatPlanId", "")))
                    self.seat_plans_table.setItem(row, 2, QTableWidgetItem(seat_plan.get("seatPlanName", "")))

                    # 价格信息
                    price_vo = seat_plan.get("originalPriceVO", {})
                    price = f"{price_vo.get('prefix', '')}{price_vo.get('yuanNum', '')}.{price_vo.get('centNum', '')}"
                    self.seat_plans_table.setItem(row, 3, QTableWidgetItem(price))

                    self.seat_plans_table.setItem(row, 4, QTableWidgetItem(seat_plan.get("seatPlanCategory", "")))
                    self.seat_plans_table.setItem(row, 5, QTableWidgetItem(str(seat_plan.get("isCombo", ""))))
                    self.seat_plans_table.setItem(row, 6, QTableWidgetItem(str(seat_plan.get("limitation", ""))))

                    # 套票详情
                    items = seat_plan.get("items", [])
                    combo_details = ""
                    if items:
                        details = []
                        for item in items:
                            details.append(f"{item.get('itemSeatPlanName', '')} x {item.get('unitQty', '')}")
                        combo_details = ", ".join(details)
                    self.seat_plans_table.setItem(row, 7, QTableWidgetItem(combo_details))
            
            # 默认选择第一个场次
            self.sessions_table.selectRow(0)

    def display_audience_data(self, data):
        """在表格中显示观众信息"""
        # 清空现有数据
        self.audience_table.setRowCount(0)

        # 获取观众数据
        audiences = []
        if isinstance(data, dict):
            # 检查是否有错误码（如Token无效）
            status_code = data.get('statusCode')
            if status_code and status_code != 200 and status_code != 15012010:
                # 如果有错误码且不是成功或Token无效，直接返回
                return
                
            # 尝试多种可能的数据结构路径
            # 尝试多种可能的数据结构路径
            if 'data' in data and isinstance(data['data'], dict) and 'audiences' in data['data']:
                audiences = data['data']['audiences']
            elif 'data' in data and isinstance(data['data'], list):
                audiences = data['data']
            elif 'result' in data and isinstance(data['result'], dict) and 'audiences' in data['result']:
                audiences = data['result']['audiences']
            elif 'result' in data and isinstance(data['result'], list):
                audiences = data['result']
            elif 'audiences' in data:
                audiences = data['audiences']
            else:
                audiences = []
            
            # 处理分页数据
            if 'pagination' in data and isinstance(data.get('data'), list):
                # 如果有分页信息且数据在data字段中，直接使用data字段
                audiences = data['data']

        # 显示观众信息
        self.audience_table.setRowCount(len(audiences))
        for row, audience in enumerate(audiences):
            if isinstance(audience, dict):
                # 添加复选框用于选择观众
                checkbox = QTableWidgetItem()
                checkbox.setCheckState(Qt.Unchecked)
                self.audience_table.setItem(row, 0, checkbox)

                self.audience_table.setItem(row, 1, QTableWidgetItem(str(audience.get("id", audience.get("audienceId", "")))))
                self.audience_table.setItem(row, 2, QTableWidgetItem(str(audience.get("name", ""))))
                self.audience_table.setItem(row, 3, QTableWidgetItem(str(audience.get("idType", audience.get("id_type", "")))))
                self.audience_table.setItem(row, 4, QTableWidgetItem(str(audience.get("age", ""))))
                self.audience_table.setItem(row, 5, QTableWidgetItem(str(audience.get("cityCode", audience.get("city_code", "")))))
                self.audience_table.setItem(row, 6, QTableWidgetItem(str(audience.get("contactWay", audience.get("contact", "")))))
                self.audience_table.setItem(row, 7, QTableWidgetItem(str(audience.get("isOptional", audience.get("is_optional", "")))))
                self.audience_table.setItem(row, 8, QTableWidgetItem(str(audience.get("status", "")) if "status" in audience else ("有效" if audience.get("isValid", audience.get("is_valid", True)) else "无效")))
                # 如果有身份证号，可以额外处理显示
                id_no = audience.get("idNo", audience.get("id_no", ""))
                if id_no and row < self.audience_table.rowCount():
                    # 可以选择是否在其他列显示身份证号信息
                    pass

    def load_cities(self):
        """加载城市数据"""
        self.city_combo.clear()
        self.city_combo.addItem("加载中...", None)
        self.city_combo.setEnabled(False)

        self.city_loader_thread = CityLoaderThread()
        self.city_loader_thread.data_loaded.connect(self.on_cities_loaded)
        self.city_loader_thread.error_occurred.connect(self.on_error)
        self.city_loader_thread.start()

    def on_cities_loaded(self, cities):
        """城市数据加载完成后的处理"""
        self.cities = cities
        self.city_combo.clear()
        for city in cities:
            self.city_combo.addItem(city['cityName'], city)
        self.city_combo.setEnabled(True)

    def on_error(self, error_message):
        """错误处理"""
        QMessageBox.critical(self, "错误", error_message)

    def query_shows(self):
        """查询演出"""
        selected_city = self.city_combo.currentData()
        if not selected_city:
            QMessageBox.warning(self, "警告", "请选择一个城市")
            return

        self.city_id = selected_city['cityId']
        self.query_btn.setEnabled(False)
        self.progress_bar.setVisible(True)

        self.show_loader_thread = ShowLoaderThread(self.city_id)
        self.show_loader_thread.shows_loaded.connect(self.on_shows_loaded)
        self.show_loader_thread.error_occurred.connect(self.on_error)
        self.show_loader_thread.start()

    def on_shows_loaded(self, shows):
        """演出数据加载完成后的处理"""
        self.current_shows = shows
        self.shows_table.setRowCount(len(shows))

        for row, show in enumerate(shows):
            if isinstance(show, dict):
                self.shows_table.setItem(row, 0, QTableWidgetItem(show.get("showName", "")))
                self.shows_table.setItem(row, 1, QTableWidgetItem(show.get("showId", "")))
                self.shows_table.setItem(row, 2, QTableWidgetItem(show.get("showDate", "")))
                self.shows_table.setItem(row, 3, QTableWidgetItem(show.get("cityName", "")))
                self.shows_table.setItem(row, 4, QTableWidgetItem(show.get("venueId", "")))
                self.shows_table.setItem(row, 5, QTableWidgetItem(show.get("firstShowTime", "")))
                self.shows_table.setItem(row, 6, QTableWidgetItem(show.get("lastShowTime", "")))

        self.query_btn.setEnabled(True)
        self.progress_bar.setVisible(False)

    def on_show_selected(self):
        """当演出被选中时"""
        selected_row = self.shows_table.currentRow()
        if selected_row >= 0:
            self.detail_btn.setEnabled(True)
        else:
            self.detail_btn.setEnabled(False)

    def show_detail(self):
        """查看演出详情"""
        selected_row = self.shows_table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "警告", "请选择一个演出")
            return

        selected_show = self.current_shows[selected_row]
        self.city_id = selected_show['cityId']
        self.show_id = selected_show['showId']
        self.site_id = selected_show['siteId']

        self.show_detail_thread = ShowDetailThread(self.city_id, self.show_id, self.site_id)
        self.show_detail_thread.detail_loaded.connect(self.on_detail_loaded)
        self.show_detail_thread.error_occurred.connect(self.on_error)
        self.show_detail_thread.start()

    def on_detail_loaded(self, detail_data):
        """演出详情加载完成后的处理"""
        self.detail_text.setPlainText(json.dumps(detail_data, ensure_ascii=False, indent=2))

    def fetch_show_sessions_clicked(self):
        """获取演出场次信息"""
        selected_show = self.sessions_show_combo.currentData()
        if not selected_show:
            QMessageBox.warning(self, "警告", "请选择一个演出")
            return

        self.city_id = selected_show['cityId']
        self.show_id = selected_show['showId']

        try:
            fetcher = DataFetcher()
            access_token = ACCESS_TOKEN

            data = fetcher.fetch_show_sessions(self.show_id, access_token)
            self.display_sessions_data(data)

            # 切换到演出场次标签页
            self.tab_widget.setCurrentWidget(self.show_sessions_tab)
        except Exception as e:
            QMessageBox.critical(self, "错误", f"获取演出场次信息时出错: {str(e)}")

    def add_identity_info(self):
        """添加实名信息"""
        name = self.name_input.text().strip()
        id_no = self.id_input.text().strip()

        if not name or not id_no:
            QMessageBox.warning(self, "警告", "请填写姓名和身份证号")
            return

        try:
            fetcher = DataFetcher()
            access_token = ACCESS_TOKEN

            data = fetcher.add_audience_info(name, id_no, access_token)
            self.display_audience_data(data)

            # 切换到观众信息标签页
            self.tab_widget.setCurrentWidget(self.audience_tab)
        except Exception as e:
            QMessageBox.critical(self, "错误", f"添加实名信息时出错: {str(e)}")

    def toggle_schedule_inputs(self):
        """切换定时提交输入框的启用状态"""
        enabled = self.schedule_enable_checkbox.isChecked()
        self.countdown_input.setEnabled(not enabled)
        self.schedule_datetime.setEnabled(enabled)

    def create_order(self):
        """创建订单"""
        # 检查是否选择了座位计划
        selected_seat_plan_row = None
        # 查找选中的座位计划（通过复选框）
        for row in range(self.seat_plans_table.rowCount()):
            checkbox_item = self.seat_plans_table.item(row, 0)
            if checkbox_item and checkbox_item.checkState() == Qt.Checked:
                selected_seat_plan_row = row
                break
        
        # 如果没有通过复选框选择，则检查是否有行被选中
        if selected_seat_plan_row is None:
            current_row = self.seat_plans_table.currentRow()
            if current_row >= 0:
                selected_seat_plan_row = current_row
            else:
                QMessageBox.warning(self, "警告", "请先选择一个座位计划")
                return
        
        # 获取选中的场次信息
        selected_session_row = self.sessions_table.currentRow()
        if selected_session_row < 0:
            QMessageBox.warning(self, "警告", "请先选择一个场次")
            return
        
        # 获取座位计划ID和价格
        seat_plan_id_item = self.seat_plans_table.item(selected_seat_plan_row, 1)  # ID在第1列
        seat_plan_name_item = self.seat_plans_table.item(selected_seat_plan_row, 2)  # 名称在第2列
        seat_plan_price_item = self.seat_plans_table.item(selected_seat_plan_row, 3)  # 价格在第3列
        
        # 获取场次ID
        session_id_item = self.sessions_table.item(selected_session_row, 0)
        
        if not (seat_plan_id_item and seat_plan_name_item and seat_plan_price_item and session_id_item):
            QMessageBox.warning(self, "警告", "座位计划或场次信息不完整")
            return
        
        seat_plan_id = seat_plan_id_item.text() if seat_plan_id_item else ""
        seat_plan_name = seat_plan_name_item.text() if seat_plan_name_item else ""
        seat_plan_price = seat_plan_price_item.text() if seat_plan_price_item else ""
        session_id = session_id_item.text() if session_id_item else ""
        
        # 获取演出ID
        selected_show = self.sessions_show_combo.currentData()
        show_id = selected_show.get('showId') if selected_show else None
        
        if not show_id:
            QMessageBox.warning(self, "警告", "演出信息不完整")
            return
        
        # 从价格文本中提取数字
        import re
        price_match = re.search(r'(\d+\.?\d*)', seat_plan_price.replace(',', ''))
        if price_match:
            ticket_price = float(price_match.group(1))
        else:
            # 如果无法提取价格，使用默认值0
            ticket_price = 0.0
        
        # 检查是否选择了观众
        selected_audience_ids = []
        for row in range(self.audience_table.rowCount()):
            checkbox_item = self.audience_table.item(row, 0)
            if checkbox_item and checkbox_item.checkState() == Qt.Checked:
                audience_id_item = self.audience_table.item(row, 1)
                if audience_id_item:
                    selected_audience_ids.append(audience_id_item.text())
        
        if not selected_audience_ids:
            QMessageBox.warning(self, "警告", "请至少选择一个观众")
            return
        
        # 构建订单数据
        order_data = {
            "src": "WEB",
            "ver": "4.45.3",
            "addressParam": {},
            "locationParam": {
                "locationCityId": "BL1034",  # 默认城市ID，实际应根据用户选择确定
                "bsCityId": "BL1034"
            },
            "paymentParam": {
                "totalAmount": ticket_price,
                "payAmount": ticket_price
            },
            "priceItemParam": [
                {
                    "applyTickets": [],
                    "priceItemName": "票款总额",
                    "priceItemVal": ticket_price,
                    "priceItemType": "TICKET_FEE",
                    "priceItemSpecies": "SEAT_PLAN",
                    "direction": "INCREASE",
                    "priceDisplay": ticket_price
                }
            ],
            "items": [
                {
                    "sku": {
                        "skuId": seat_plan_id,
                        "skuType": "SINGLE",
                        "ticketPrice": ticket_price,
                        "qty": 1,
                        "ticketItems": []
                    },
                    "spu": {
                        "showId": show_id,
                        "sessionId": session_id,
                        "promotionVersionHash": "EMPTY_PROMOTION_HASH",
                        "addPromoVersionHash": "EMPTY_PROMOTION_HASH"
                    },
                    "deliverMethod": "ID_CARD"
                }
            ],
            "priorityId": "",
            "sourceOrderId": "",
            "addPurchasePromotionId": "",
            "scene": "",
            "many2OneAudience": {},
            "orderSource": "COMMON"
        }
        
        # 为每个选中的观众添加ticketItems
        for audience_id in selected_audience_ids:
            order_data["items"][0]["sku"]["ticketItems"].append({
                "id": "1761454218936100000003",  # 示例ID，实际应根据情况生成
                "audienceId": audience_id
            })
        
        # 显示订单信息在订单输出界面
        order_info_text = f"""
订单信息预览:
-----------
演出ID: {show_id}
场次ID: {session_id}
座位计划ID: {seat_plan_id}
座位计划名称: {seat_plan_name}
票价: {ticket_price}
选中观众数量: {len(selected_audience_ids)}
观众ID列表: {', '.join(selected_audience_ids)}
        """
        
        self.order_info_text.setPlainText(order_info_text)
        
        # 检查是否启用定时提交
        if self.schedule_enable_checkbox.isChecked():
            # 获取定时提交的时间
            schedule_time = self.schedule_datetime.dateTime()
            current_time = QDateTime.currentDateTime()
            
            # 检查时间是否有效（不能是过去的时间）
            if schedule_time <= current_time:
                QMessageBox.warning(self, "警告", "定时提交时间必须晚于当前时间")
                return
            
            # 计算时间差（秒）
            secs_to_start = current_time.secsTo(schedule_time)
            
            # 设置倒计时为定时时间
            countdown_seconds = secs_to_start
            self.countdown_display.setText(f"定时提交已设置，将在 {schedule_time.toString('yyyy-MM-dd hh:mm:ss')} 开始提交")
        else:
            # 获取倒计时设置
            countdown_text = self.countdown_input.text()
            try:
                countdown_seconds = int(countdown_text) if countdown_text else 0
            except ValueError:
                countdown_seconds = 0
        
        # 获取线程数
        thread_count = self.thread_count_spinbox.value()
        
        # 禁用提交按钮，启用停止按钮
        self.submit_order_btn.setEnabled(False)
        self.stop_order_btn.setEnabled(True)
        if not self.schedule_enable_checkbox.isChecked():
            self.countdown_display.setText("准备提交...")
        
        # 清空之前的线程列表
        self.order_threads = []
        
        # 启动多个订单提交线程
        access_token = ACCESS_TOKEN
        
        for i in range(thread_count):
            thread = OrderSubmitThread(order_data, access_token, thread_count)
            thread.set_countdown(countdown_seconds)
            thread.order_result.connect(self.on_order_result)
            thread.order_error.connect(self.on_order_error)
            thread.countdown_updated.connect(self.on_countdown_updated)
            thread.time_updated.connect(self.on_time_updated)
            thread.log_message.connect(self.on_log_message)
            thread.finished.connect(lambda tid=i: self.on_order_thread_finished(tid))
            self.order_threads.append(thread)
            thread.start()
            
        # 切换到日志标签页
        self.tab_widget.setCurrentWidget(self.log_tab)

    def stop_order_submission(self):
        """停止订单提交"""
        for thread in self.order_threads:
            if thread.isRunning():
                thread.stop()
        self.countdown_display.setText("提交已停止")
        self.log_text.append(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 提交已停止")
            
    def on_order_result(self, result):
        """订单提交结果处理"""
        # 显示订单创建结果在订单输出界面
        result_text = json.dumps(result, ensure_ascii=False, indent=2)
        self.order_result_text.setPlainText(result_text)
        
        # 切换到订单输出标签页
        self.tab_widget.setCurrentWidget(self.order_tab)
        
        # 显示消息框通知用户
        # QMessageBox.information(self, "订单提交结果", "订单已提交，结果已在订单输出页面显示")

    def on_order_error(self, error_msg):
        """订单提交错误处理"""
        QMessageBox.critical(self, "订单提交错误", f"提交订单时出错: {error_msg}")

    def on_countdown_updated(self, countdown_text):
        """倒计时更新处理"""
        self.countdown_display.setText(countdown_text)


    def on_time_updated(self, time_text):
        """时间更新处理"""
        self.current_time_display.setText(time_text)

    def on_order_thread_finished(self, thread_id=None):
        """订单线程结束处理"""
        # 检查是否所有线程都已完成
        all_finished = all(not thread.isRunning() for thread in self.order_threads)
        
        if all_finished:
            self.submit_order_btn.setEnabled(True)
            self.stop_order_btn.setEnabled(False)
            self.countdown_display.setText("提交完成/已停止")
            
    def on_log_message(self, message):
        """处理日志消息"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {message}"
        self.log_text.append(log_message)
        # 自动滚动到最新日志
        self.log_text.moveCursor(QTextCursor.End)

    def display_audience_data(self, data):
        """在表格中显示观众信息"""
        # 清空现有数据
        self.audience_table.setRowCount(0)

        # 获取观众数据
        audiences = []
        if isinstance(data, dict):
            # 检查是否有错误码（如Token无效）
            status_code = data.get('statusCode')
            if status_code and status_code != 200 and status_code != 15012010:
                # 如果有错误码且不是成功或Token无效，直接返回
                return
                
            # 尝试多种可能的数据结构路径
            if 'data' in data and isinstance(data['data'], dict) and 'audiences' in data['data']:
                audiences = data['data']['audiences']
            elif 'data' in data and isinstance(data['data'], list):
                audiences = data['data']
            elif 'result' in data and isinstance(data['result'], dict) and 'audiences' in data['result']:
                audiences = data['result']['audiences']
            elif 'result' in data and isinstance(data['result'], list):
                audiences = data['result']
            elif 'audiences' in data:
                audiences = data['audiences']
            else:
                audiences = []
            
            # 处理分页数据
            if 'pagination' in data and isinstance(data.get('data'), list):
                # 如果有分页信息且数据在data字段中，直接使用data字段
                audiences = data['data']

        # 显示观众信息
        self.audience_table.setRowCount(len(audiences))
        for row, audience in enumerate(audiences):
            if isinstance(audience, dict):
                # 添加复选框用于选择观众
                checkbox = QTableWidgetItem()
                checkbox.setCheckState(Qt.Unchecked)
                self.audience_table.setItem(row, 0, checkbox)

                self.audience_table.setItem(row, 1, QTableWidgetItem(str(audience.get("id", audience.get("audienceId", "")))))
                self.audience_table.setItem(row, 2, QTableWidgetItem(str(audience.get("name", ""))))
                self.audience_table.setItem(row, 3, QTableWidgetItem(str(audience.get("idType", audience.get("id_type", "")))))
                self.audience_table.setItem(row, 4, QTableWidgetItem(str(audience.get("age", ""))))
                self.audience_table.setItem(row, 5, QTableWidgetItem(str(audience.get("cityCode", audience.get("city_code", "")))))
                self.audience_table.setItem(row, 6, QTableWidgetItem(str(audience.get("contactWay", audience.get("contact", "")))))
                self.audience_table.setItem(row, 7, QTableWidgetItem(str(audience.get("isOptional", audience.get("is_optional", "")))))
                self.audience_table.setItem(row, 8, QTableWidgetItem(str(audience.get("status", "")) if "status" in audience else ("有效" if audience.get("isValid", audience.get("is_valid", True)) else "无效")))

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

        # 清空演出场次标签页中的演出选择列表
        self.sessions_show_combo.clear()

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

            # 更新演出场次标签页中的演出选择列表
            self.update_sessions_show_list(shows)

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

    def fetch_show_sessions_clicked(self):
        """获取演出场次信息 - 按钮点击事件"""
        # 获取选中的演出ID
        selected_show = self.sessions_show_combo.currentData()
        if not selected_show:
            QMessageBox.warning(self, "警告", "请先选择一个演出")
            return

        show_id = selected_show.get('showId')
        if not show_id:
            QMessageBox.warning(self, "警告", "选中的演出信息不完整")
            return

        # 调用实际的API请求
        try:
            # 使用已有的演出场次请求功能
            fetcher = DataFetcher()
            access_token = ACCESS_TOKEN
            data = fetcher.fetch_show_sessions(show_id, access_token)
            self.display_sessions_data(data)
        except Exception as e:
            # 如果API请求失败，回退到使用ss.txt中的示例数据
            try:
                with open('ss.txt', 'r', encoding='utf-8') as f:
                    content = f.read()
                    # 提取JSON部分
                    json_start = content.find('{')
                    json_end = content.rfind('}') + 1
                    if json_start != -1 and json_end > json_start:
                        json_str = content[json_start:json_end]
                        data = json.loads(json_str)
                        self.display_sessions_data(data)
                    else:
                        QMessageBox.critical(self, "错误", "无法从ss.txt中解析JSON数据")
            except Exception as fallback_error:
                QMessageBox.critical(self, "错误",
                                     f"获取场次信息时出错: {str(e)}\n回退读取也失败: {str(fallback_error)}")

    def add_identity_info(self):
        """添加实名信息"""
        name = self.name_input.text().strip()
        id_no = self.id_input.text().strip()

        if not name or not id_no:
            QMessageBox.warning(self, "警告", "请填写完整的姓名和身份证号")
            return

        # 验证身份证号格式（简单验证）
        if len(id_no) != 18:
            QMessageBox.warning(self, "警告", "身份证号格式不正确")
            return

        try:
            # 调用添加实名信息的API
            fetcher = DataFetcher()
            access_token = ACCESS_TOKEN
            result = fetcher.add_audience_info(name, id_no, access_token)

            if result.get("statusCode") == 200:
                QMessageBox.information(self, "成功", "实名信息添加成功")
                # 清空输入框
                self.name_input.clear()
                self.id_input.clear()
            else:
                error_msg = result.get("errorMessage", "添加失败")
                QMessageBox.critical(self, "错误", f"添加实名信息失败: {error_msg}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"添加实名信息时出错: {str(e)}")


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