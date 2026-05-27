import json
import re
from typing import List, Dict, Any

class RobustJsonParser:
    """强大的JSON解析器，专门处理复杂的嵌套和转义问题"""
    
    @staticmethod
    def deep_unescape(text: str) -> str:
        """深度处理转义字符"""
        # 保存原始长度用于比较
        original_len = len(text)
        
        # 循环处理直到不再变化
        prev_len = 0
        while len(text) != prev_len:
            prev_len = len(text)
            
            # 按优先级处理不同层级的转义
            text = text.replace('\\\\\\\\', '\\\\')  # 四个反斜杠 -> 两个
            text = text.replace('\\\\\\"', '\\"')    # 三个反斜杠+引号 -> 反斜杠+引号
            text = text.replace('\\\\{', '\\{')      # 两个反斜杠+{ -> 反斜杠+{
            text = text.replace('\\\\}', '\\}')      # 两个反斜杠+} -> 反斜杠+}
            text = text.replace('\\\\[', '\\[')      # 两个反斜杠+[ -> 反斜杠+[
            text = text.replace('\\\\]', '\\]')      # 两个反斜杠+] -> 反斜杠+]
            
        print(f"深度转义处理: {original_len} -> {len(text)} 字符")
        return text
    
    @staticmethod
    def extract_json_objects(text: str) -> List[str]:
        """提取所有完整的JSON对象"""
        objects = []
        brace_stack = []
        start_pos = -1
        
        for i, char in enumerate(text):
            if char == '{':
                if not brace_stack:
                    start_pos = i
                brace_stack.append(i)
            elif char == '}':
                if brace_stack:
                    brace_stack.pop()
                    if not brace_stack and start_pos != -1:
                        # 找到一个完整的对象
                        json_obj = text[start_pos:i+1]
                        objects.append(json_obj)
                        start_pos = -1
        
        return objects
    
    @staticmethod
    def safe_json_load(json_str: str) -> Any:
        """安全的JSON加载，带有多重尝试"""
        # 尝试1: 直接解析
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            pass
        
        # 尝试2: 移除外层引号后解析
        cleaned = json_str.strip()
        if (cleaned.startswith('"') and cleaned.endswith('"')) or \
           (cleaned.startswith("'") and cleaned.endswith("'")):
            cleaned = cleaned[1:-1]
            try:
                return json.loads(cleaned)
            except json.JSONDecodeError:
                pass
        
        # 尝试3: 深度转义后解析
        unescaped = RobustJsonParser.deep_unescape(cleaned)
        try:
            return json.loads(unescaped)
        except json.JSONDecodeError:
            pass
        
        # 尝试4: 使用正则表达式提取JSON对象
        json_objects = RobustJsonParser.extract_json_objects(unescaped)
        for obj_str in json_objects:
            try:
                return json.loads(obj_str)
            except json.JSONDecodeError:
                continue
        
        return None
    
    @staticmethod
    def recursive_find_key(data: Any, target_key: str) -> Any:
        """递归查找指定键的值"""
        if isinstance(data, dict):
            if target_key in data:
                return data[target_key]
            for value in data.values():
                result = RobustJsonParser.recursive_find_key(value, target_key)
                if result is not None:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = RobustJsonParser.recursive_find_key(item, target_key)
                if result is not None:
                    return result
        return None

def parse_complex_game_data(json_data: str) -> List[Dict]:
    """解析复杂的嵌套游戏数据"""
    print("开始解析复杂的游戏数据...")
    print(f"原始数据长度: {len(json_data)}")
    
    # 使用强大解析器
    parser = RobustJsonParser()
    
    # 第一步：解析最外层
    outer_data = parser.safe_json_load(json_data)
    if not outer_data:
        print("❌ 外层数据解析失败")
        return []
    
    print("✅ 外层数据解析成功")
    
    # 第二步：查找rsp.response.data路径
    rsp_data = parser.recursive_find_key(outer_data, 'data')
    if not rsp_data or not isinstance(rsp_data, str):
        print("❌ 未找到有效的rsp.response.data")
        return []
    
    print(f"✅ 找到内层data，长度: {len(rsp_data)}")
    
    # 第三步：解析内层JSON
    inner_data = parser.safe_json_load(rsp_data)
    if not inner_data:
        print("❌ 内层JSON解析失败")
        return []
    
    print("✅ 内层JSON解析成功")
    
    # 第四步：查找角色列表
    role_list_data = parser.recursive_find_key(inner_data, 'roleList')
    if not role_list_data:
        print("❌ 未找到角色列表")
        return []
    
    print(f"✅ 找到角色列表数据，类型: {type(role_list_data)}")
    
    # 第五步：解析角色列表
    roles = []
    if isinstance(role_list_data, str):
        # 如果是字符串，需要进一步解析
        print("角色列表是字符串格式，继续解析...")
        role_list_obj = parser.safe_json_load(role_list_data)
        if isinstance(role_list_obj, list):
            roles = role_list_obj
        else:
            # 尝试手动解析
            roles = manual_extract_roles(role_list_data)
    elif isinstance(role_list_data, list):
        # 如果直接就是列表
        roles = role_list_data
    
    print(f"🎉 成功解析 {len(roles)} 个角色!")
    return roles

def manual_extract_roles(role_str: str) -> List[Dict]:
    """手动提取角色数据"""
    print("开始手动提取角色...")
    
    # 清理字符串
    content = role_str.strip()
    if content.startswith('"[') and content.endswith(']"'):
        content = content[2:-2]
    elif content.startswith('[') and content.endswith(']'):
        content = content[1:-1]
    elif content.startswith('"') and content.endswith('"'):
        content = content[1:-1]
    
    # 使用正则表达式匹配JSON对象
    pattern = r'\{(?:[^{}]|(?R))*\}'  # 匹配嵌套的花括号
    matches = re.findall(pattern, content)
    
    roles = []
    for match in matches:
        try:
            role_data = json.loads(match)
            roles.append(role_data)
        except json.JSONDecodeError as e:
            print(f"⚠️  角色解析失败: {str(e)[:50]}...")
    
    print(f"手动提取完成，获得 {len(roles)} 个角色")
    return roles

def display_game_roles(roles: List[Dict]):
    """显示游戏角色信息"""
    if not roles:
        print("没有可显示的角色数据")
        return
    
    print("\n" + "="*80)
    print("游戏代练角色详细信息")
    print("="*80)
    
    # 基本统计
    total_roles = len(roles)
    prices = [role.get('price', 0) for role in roles]
    total_price = sum(prices)
    avg_price = total_price / total_roles if total_roles > 0 else 0
    
    print(f"\n📊 统计概览:")
    print(f"   总角色数: {total_roles}")
    print(f"   总价值: {total_price:,}")
    print(f"   平均价格: {avg_price:,.0f}")
    print(f"   最高价格: {max(prices):,}")
    print(f"   最低价格: {min(prices):,}")
    
    # 平台分布
    platforms = {}
    channels = {}
    for role in roles:
        plat = role.get('platformID', 'unknown')
        chan = role.get('channelID', 'unknown')
        platforms[plat] = platforms.get(plat, 0) + 1
        channels[chan] = channels.get(chan, 0) + 1
    
    print(f"\n🌐 平台分布:")
    for plat, count in sorted(platforms.items(), key=lambda x: x[1], reverse=True):
        print(f"   {plat}: {count}个")
    
    print(f"\n📱 渠道分布:")
    for chan, count in sorted(channels.items(), key=lambda x: x[1], reverse=True):
        print(f"   {chan}: {count}个")
    
    # 详细角色信息（显示前10个）
    print(f"\n📋 角色详情 (显示前10个):")
    print("-" * 80)
    
    for i, role in enumerate(roles[:10], 1):
        print(f"\n🎯 角色 #{i}")
        print(f"   平台: {role.get('platformID', 'N/A')} | 渠道: {role.get('channelID', 'N/A')}")
        print(f"   分区: {role.get('partitionID', 'N/A')} | 角色ID: {role.get('roleID', 'N/A')}")
        
        # 游戏属性
        summary = role.get('gameSummary', {})
        if summary:
            print(f"   战力: {summary.get('CombatPower', 0):,} | "
                  f"等级: {summary.get('Level', 0)}级 | "
                  f"家园: {summary.get('HouselandLevel', 0)}级")
        
        # 交易信息
        print(f"   价格: {role.get('price', 0):,} | "
              f"收藏: {role.get('favAmount', 0)} | "
              f"可议价: {'是' if role.get('allowBargain', False) else '否'}")
        
        # 商品信息
        print(f"   状态: {role.get('commodityStatus', 'N/A')} | "
              f"编号: {role.get('commoditySN', 'N/A')}")
        
        if i < min(10, len(roles)):
            print("   " + "-" * 40)

# 主程序
def main():
    # 原始复杂JSON数据
    complex_json = '''{"ret": 0, "rsp": {"response":{"data":"{\\"ret\\":0,\\"msg\\":\\"\\",\\"data\\":{\\"roleList\\":\\"[{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"246\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"67619986511757\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":210687,\\\\\\"CustomXId\\\\\\":20102,\\\\\\"HeadId\\\\\\":1019,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":74237,\\\\\\"Level\\\\\\":94,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1200000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260118034250518-26-7NNp1Id9f\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":25,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"198\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"54425837185673\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":208184,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1016,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":39412,\\\\\\"Level\\\\\\":92,\\\\\\"PlayerNation\\\\\\":3},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1800000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260116163049475-94-NsGCeO2eJ\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":113,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"655\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"180045052893518\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":207435,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":35,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":56526,\\\\\\"Level\\\\\\":92,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]}]}\\\\\\",\\\\\\"price\\\\\\":1350000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260128093922935-95-XWICYnDWx\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":87,\\\\\\"allowBargain\\\\\\":false,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"613\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"168500173413411\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":206918,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1009,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":71501,\\\\\\"Level\\\\\\":93,\\\\\\"PlayerNation\\\\\\":3},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1488800,\\\\\\"commoditySN\\\\\\":\\\\\\"20260217103541564-83-5Kv2XLzaF\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":15,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"700\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"192414566765525\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":204828,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":46,\\\\\\"HouselandLevel\\\\\\":29,\\\\\\"HouselandPoint\\\\\\":23765,\\\\\\"Level\\\\\\":93,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":888800,\\\\\\"commoditySN\\\\\\":\\\\\\"20260211193454304-86-Wfu56RCys\\\\\\",\\\\\\"commodityStatus\\\\\\":300,\\\\\\"favAmount\\\\\\":40,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"587\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"161353340481140\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":204200,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1010,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":45189,\\\\\\"Level\\\\\\":90,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":2800000,\\\\\\"commoditySN\\\\\\":\\\\\\"20240804141008787-8-YCd48jKFmW\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":234,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"647\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"177846030539789\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":203298,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1005,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":31162,\\\\\\"Level\\\\\\":91,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1099900,\\\\\\"commoditySN\\\\\\":\\\\\\"20260219233927879-11-Gg9sfe4np\\\\\\",\\\\\\"commodityStatus\\\\\\":300,\\\\\\"favAmount\\\\\\":2,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"611\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"167950416905313\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":202475,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1009,\\\\\\"HouselandLevel\\\\\\":31,\\\\\\"HouselandPoint\\\\\\":22045,\\\\\\"Level\\\\\\":91,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":500000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260126005130157-98-yqD47jeVj\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":43,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"373\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"102529509267213\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":201800,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1002,\\\\\\"HouselandLevel\\\\\\":30,\\\\\\"HouselandPoint\\\\\\":24213,\\\\\\"Level\\\\\\":88,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":820000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260204011008324-25-OffQ1YsoN\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":140,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"208\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"57174618222858\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":201003,\\\\\\"CustomXId\\\\\\":20102,\\\\\\"HeadId\\\\\\":1009,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":94228,\\\\\\"Level\\\\\\":90,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":3300000,\\\\\\"commoditySN\\\\\\":\\\\\\"20251105200504820-86-ll2JBCz00\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":475,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"325\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"89335359825821\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":200608,\\\\\\"CustomXId\\\\\\":20194,\\\\\\"HeadId\\\\\\":1018,\\\\\\"HouselandLevel\\\\\\":30,\\\\\\"HouselandPoint\\\\\\":19058,\\\\\\"Level\\\\\\":90,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]}]}\\\\\\",\\\\\\"price\\\\\\":500000,\\\\\\"commoditySN\\\\\\":\\\\\\"20251221111008046-56-X4sSvPlQ5\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":123,\\\\\\"allowBargain\\\\\\":false,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"723\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"198736763199599\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":200085,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":75,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":19172,\\\\\\"Level\\\\\\":96,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":700000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260216130818821-97-b00H8v0uq\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":17,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"196\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"53876080819465\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":198572,\\\\\\"CustomXId\\\\\\":20103,\\\\\\"HeadId\\\\\\":25,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":35183,\\\\\\"Level\\\\\\":91,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":800000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260208144602396-28-EScHCHIJt\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":38,\\\\\\"allowBargain\\\\\\":false,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]}]\\"}}}}}}'''
    
    print("🎮 强大的游戏数据解析器")
    print("=" * 50)
    
    # 解析数据
    roles = parse_complex_game_data(complex_json)
    
    # 显示结果
    display_game_roles(roles)
    
    print(f"\n✅ 解析完成! 共处理 {len(roles)} 个游戏代练角色")

if __name__ == "__main__":
    main()