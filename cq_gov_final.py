import requests
import re
from bs4 import BeautifulSoup
import csv

def get_cq_gov_page():
    """
    将JavaScript fetch请求转换为Python requests请求（最终优化版）
    原始fetch请求: https://rlsbj.cq.gov.cn/ztzl/zqs2020ndkslygwyzl/gwyks2026/202601/t20260121_15341242.html
    """
    url = "https://rlsbj.cq.gov.cn/ztzl/zqs2020ndkslygwyzl/gwyks2026/202601/t20260121_15341242.html"
    
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
    }
    
    # 创建session对象
    session = requests.Session()
    
    # 设置referrer
    headers["Referer"] = "https://cn.bing.com/"
    
    try:
        # 发送GET请求
        response = session.get(
            url,
            headers=headers,
            timeout=30  # 添加超时设置
        )
        
        # 检查响应状态
        if response.status_code == 200:
            print("请求成功!")
            print("响应状态码:", response.status_code)
            
            # 使用二进制内容并用UTF-8解码
            decoded_content = response.content.decode('utf-8')
            
            # 保存到文件
            with open('cq_gov_page_final.html', 'w', encoding='utf-8') as f:
                f.write(decoded_content)
            print("内容已保存到 cq_gov_page_final.html 文件中")
            
            # 提取页面关键信息
            title_match = re.search(r'<title>(.*?)</title>', decoded_content, re.IGNORECASE | re.DOTALL)
            site_name_match = re.search(r'<meta name="SiteName" content="(.*?)"', decoded_content)
            article_title_match = re.search(r'<meta name="ArticleTitle" content="(.*?)"', decoded_content)
            pub_date_match = re.search(r'<meta name="PubDate" content="(.*?)"', decoded_content)
            
            # 打印提取的信息（这里使用repr()函数避免终端显示乱码问题）
            if title_match:
                title = title_match.group(1).strip()
                print(f"页面标题: {repr(title)}")
            if site_name_match:
                site_name = site_name_match.group(1)
                print(f"站点名称: {repr(site_name)}")
            if article_title_match:
                article_title = article_title_match.group(1)
                print(f"文章标题: {repr(article_title)}")
            if pub_date_match:
                pub_date = pub_date_match.group(1)
                print(f"发布日期: {repr(pub_date)}")
                
            print(f"响应内容长度: {len(decoded_content)} 字符")
            
            # 解析表格数据
            parse_table_data(decoded_content)
            
            # 返回解码后的内容
            return decoded_content
        else:
            print(f"请求失败，状态码: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"请求过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
        return None

def extract_key_info(html_content):
    """
    从HTML内容中提取关键信息
    """
    if not html_content:
        return {}
    
    info = {}
    
    # 提取标题
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE | re.DOTALL)
    if title_match:
        info['title'] = title_match.group(1).strip()
    
    # 提取站点名称
    site_name_match = re.search(r'<meta name="SiteName" content="(.*?)"', html_content)
    if site_name_match:
        info['site_name'] = site_name_match.group(1)
    
    # 提取文章标题
    article_title_match = re.search(r'<meta name="ArticleTitle" content="(.*?)"', html_content)
    if article_title_match:
        info['article_title'] = article_title_match.group(1)
    
    # 提取发布日期
    pub_date_match = re.search(r'<meta name="PubDate" content="(.*?)"', html_content)
    if pub_date_match:
        info['pub_date'] = pub_date_match.group(1)
    
    # 提取关键词
    keywords_match = re.search(r'<meta name="Keywords" content="(.*?)"', html_content)
    if keywords_match:
        info['keywords'] = keywords_match.group(1)
    
    # 提取来源
    source_match = re.search(r'<meta name="ContentSource" content="(.*?)"', html_content)
    if source_match:
        info['content_source'] = source_match.group(1)
    
    return info

def parse_table_data(html_content):
    """
    从HTML中解析表格数据并导出到CSV
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 查找表格元素
    tables = soup.find_all('table')
    
    # 寻找包含指定列名的表格
    target_table = None
    for table in tables:
        # 检查表头是否包含所需字段
        headers = table.find_all(['th', 'td'])
        header_texts = [header.get_text(strip=True) for header in headers[:7]]  # 前7个单元格
        
        # 检查是否包含我们需要的列
        required_headers = ["主管单位", "报考单位", "报考职位", "计划招考人数", "报考人数", "审核通过人数", "交费人数"]
        if all(req_header in header_texts for req_header in required_headers):
            target_table = table
            break
    
    if target_table:
        print("找到目标表格，正在解析数据...")
        
        rows = []
        # 获取所有行
        tr_tags = target_table.find_all('tr')
        
        for i, tr in enumerate(tr_tags):
            row = []
            cells = tr.find_all(['td', 'th'])  # 同时查找td和th
            for cell in cells:
                # 获取单元格文本，去除多余空白
                cell_text = cell.get_text(strip=True)
                row.append(cell_text)
            
            if row:  # 只添加非空行
                rows.append(row)
        
        if rows:
            # 导出到CSV文件
            export_to_csv(rows, 'cq_gov_exam_data.csv')
            print(f"表格数据已导出到 cq_gov_exam_data.csv，共 {len(rows)} 行数据")
            
            # 显示前几行数据
            print("\n前5行数据预览:")
            for i, row in enumerate(rows[:5]):
                print(f"第{i+1}行: {row}")
        else:
            print("未找到表格数据")
            
            # 如果没找到，尝试直接从HTML源码中提取表格数据
            extract_table_from_html_source(html_content)
    else:
        print("未找到包含指定列的表格")
        # 尝试直接从HTML源码中提取表格数据
        extract_table_from_html_source(html_content)

def extract_table_from_html_source(html_content):
    """
    从HTML源码中直接提取表格数据
    """
    # 使用正则表达式查找表格行
    # 匹配<tr>标签及其内容
    tr_pattern = r'<tr[^>]*>.*?</tr>'
    tr_matches = re.findall(tr_pattern, html_content, re.DOTALL)
    
    rows = []
    for tr_match in tr_matches:
        # 提取<td>或<th>中的内容
        cell_pattern = r'<t[dh][^>]*>(.*?)</t[dh]>'
        cells = re.findall(cell_pattern, tr_match, re.DOTALL)
        
        row = []
        for cell in cells:
            # 移除HTML标签，只保留文本内容
            clean_cell = re.sub(r'<[^>]+>', '', cell)
            clean_cell = clean_cell.strip()
            row.append(clean_cell)
        
        if row:  # 只添加非空行
            rows.append(row)
    
    if rows:
        print(f"从HTML源码中提取到 {len(rows)} 行数据")
        export_to_csv(rows, 'cq_gov_exam_data_from_source.csv')
        print("数据已导出到 cq_gov_exam_data_from_source.csv")
        
        # 显示前几行数据
        print("\n前5行数据预览:")
        for i, row in enumerate(rows[:5]):
            print(f"第{i+1}行: {row}")

def export_to_csv(data, filename):
    """
    将数据导出到CSV文件，使用UTF-8-SIG编码
    """
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == "__main__":
    content = get_cq_gov_page()
    if content:
        key_info = extract_key_info(content)
        print("\n提取的关键信息:")
        for key, value in key_info.items():
            print(f"{key}: {repr(value)}")