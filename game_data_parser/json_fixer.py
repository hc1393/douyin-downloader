import json
import re

def fix_and_parse_json(json_str):
    """修复并解析复杂的嵌套JSON字符串"""
    print("开始修复JSON字符串...")
    
    # 步骤1: 移除外层引号
    if json_str.startswith("'") and json_str.endswith("'"):
        json_str = json_str[1:-1]
    if json_str.startswith('"') and json_str.endswith('"'):
        json_str = json_str[1:-1]
    
    print(f"步骤1 - 移除外层引号后长度: {len(json_str)}")
    
    # 步骤2: 逐步替换转义字符
    # 先处理最内层的转义
    json_str = json_str.replace('\\\\\\\\', '\\\\')
    json_str = json_str.replace('\\\\\\"', '\\"')
    json_str = json_str.replace('\\\\\\', '\\')
    
    print(f"步骤2 - 处理转义字符后长度: {len(json_str)}")
    
    # 步骤3: 尝试解析外层JSON
    try:
        outer_data = json.loads(json_str)
        print("外层JSON解析成功")
        
        # 获取内层data
        rsp_data = outer_data.get('rsp', {}).get('response', {}).get('data', '')
        if not rsp_data:
            print("未找到内层data字段")
            return None
            
        print(f"找到内层data字段，长度: {len(rsp_data)}")
        
        # 步骤4: 解析内层JSON
        try:
            inner_data = json.loads(rsp_data)
            print("内层JSON解析成功")
            
            # 获取角色列表
            role_list_str = inner_data.get('data', {}).get('roleList', '')
            if not role_list_str:
                print("未找到角色列表")
                return None
                
            print(f"找到角色列表字符串，长度: {len(role_list_str)}")
            
            # 步骤5: 解析角色列表
            try:
                role_list = json.loads(role_list_str)
                print(f"成功解析 {len(role_list)} 个角色")
                return role_list
            except json.JSONDecodeError as e:
                print(f"角色列表解析失败: {e}")
                # 尝试手动修复
                return manual_parse_role_list(role_list_str)
                
        except json.JSONDecodeError as e:
            print(f"内层JSON解析失败: {e}")
            return None
            
    except json.JSONDecodeError as e:
        print(f"外层JSON解析失败: {e}")
        print("尝试手动提取有效JSON...")
        return extract_json_manually(json_str)

def extract_json_manually(text):
    """手动提取JSON内容"""
    # 查找第一个完整的JSON对象
    brace_count = 0
    start_pos = -1
    end_pos = -1
    
    for i, char in enumerate(text):
        if char == '{':
            if brace_count == 0:
                start_pos = i
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0 and start_pos != -1:
                end_pos = i
                break
    
    if start_pos != -1 and end_pos != -1:
        json_part = text[start_pos:end_pos+1]
        print(f"手动提取的JSON长度: {len(json_part)}")
        try:
            data = json.loads(json_part)
            # 递归查找角色数据
            return find_role_data(data)
        except:
            pass
    
    return None

def find_role_data(data):
    """在数据结构中查找角色列表"""
    if isinstance(data, dict):
        # 检查是否有roleList
        if 'roleList' in data:
            try:
                return json.loads(data['roleList'])
            except:
                return manual_parse_role_list(data['roleList'])
        
        # 递归搜索子字典
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                result = find_role_data(value)
                if result:
                    return result
                    
    elif isinstance(data, list):
        # 在列表中搜索
        for item in data:
            if isinstance(item, (dict, list)):
                result = find_role_data(item)
                if result:
                    return result
    
    return None

def manual_parse_role_list(role_str):
    """手动解析角色列表字符串"""
    print("开始手动解析角色列表...")
    
    # 移除首尾的引号和方括号
    content = role_str.strip()
    if content.startswith('"[') and content.endswith(']"'):
        content = content[2:-2]
    elif content.startswith('[') and content.endswith(']'):
        content = content[1:-1]
    elif content.startswith('"') and content.endswith('"'):
        content = content[1:-1]
    
    print(f"清理后内容长度: {len(content)}")
    
    # 使用正则表达式匹配JSON对象
    # 匹配形如 {"key": "value", ...} 的对象
    pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
    matches = re.findall(pattern, content)
    
    roles = []
    for match in matches:
        try:
            role_data = json.loads(match)
            roles.append(role_data)
        except json.JSONDecodeError:
            print(f"无法解析角色: {match[:100]}...")
    
    print(f"手动解析得到 {len(roles)} 个角色")
    return roles

def display_parsed_data(roles):
    """显示解析后的数据"""
    if not roles:
        print("没有解析到任何角色数据")
        return
        
    print("=" * 80)
    print("解析成功的角色数据")
    print("=" * 80)
    
    print(f"\n总共解析到 {len(roles)} 个角色：\n")
    
    for i, role in enumerate(roles[:5], 1):  # 只显示前5个
        print(f"--- 角色 {i} ---")
        print(f"平台ID: {role.get('platformID', 'N/A')}")
        print(f"渠道ID: {role.get('channelID', 'N/A')}")
        print(f"分区ID: {role.get('partitionID', 'N/A')}")
        print(f"价格: {role.get('price', 0):,}")
        
        game_summary = role.get('gameSummary', {})
        if game_summary:
            print(f"战力: {game_summary.get('CombatPower', 0):,}")
            print(f"等级: {game_summary.get('Level', 0)}级")
        
        print("-" * 40)
    
    if len(roles) > 5:
        print(f"... 还有 {len(roles) - 5} 个角色未显示")

# 测试数据
test_json = '''{"ret": 0, "rsp": {"response":{"data":"{\\"ret\\":0,\\"msg\\":\\"\\",\\"data\\":{\\"roleList\\":\\"[{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"246\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"67619986511757\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":210687,\\\\\\"CustomXId\\\\\\":20102,\\\\\\"HeadId\\\\\\":1019,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":74237,\\\\\\"Level\\\\\\":94,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1200000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260118034250518-26-7NNp1Id9f\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":25,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"198\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"54425837185673\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":208184,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1016,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":39412,\\\\\\"Level\\\\\\":92,\\\\\\"PlayerNation\\\\\\":3},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1800000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260116163049475-94-NsGCeO2eJ\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":113,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]}]\\",\\"total\\":14,\\"pageSize\\":10,\\"pageNum\\":1,\\"pages\\":2,\\"hasNextPage\\":true,\\"hasPrePage\\":false}"}}}}'''

if __name__ == "__main__":
    print("JSON修复和解析工具")
    print("=" * 50)
    
    roles = fix_and_parse_json(test_json)
    display_parsed_data(roles)