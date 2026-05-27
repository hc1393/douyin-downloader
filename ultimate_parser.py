import json
import re

def ultimate_json_extractor(json_string):
    """终极JSON提取器 - 使用暴力方法提取所有可能的JSON数据"""
    
    print("🔍 启动终极JSON提取器...")
    print(f"原始字符串长度: {len(json_string)}")
    
    # 方法1: 直接查找包含角色数据的部分
    print("\n方法1: 搜索关键词定位")
    
    # 查找包含关键字段的区域
    keywords = ['roleList', 'platformID', 'channelID', 'CombatPower', 'price']
    
    # 提取包含这些关键词的文本段落
    segments = []
    for keyword in keywords:
        pattern = rf'"[^"]*{keyword}[^"]*"'
        matches = re.finditer(pattern, json_string)
        for match in matches:
            start = max(0, match.start() - 100)
            end = min(len(json_string), match.end() + 100)
            segment = json_string[start:end]
            segments.append(segment)
    
    print(f"找到 {len(segments)} 个相关片段")
    
    # 方法2: 暴力尝试不同的清理方法
    print("\n方法2: 暴力清理和尝试")
    
    # 收集所有可能的清理版本
    variants = [
        json_string,  # 原始
        json_string.replace('\\', ''),  # 移除所有反斜杠
        json_string.replace('\\\\', '\\'),  # 双反斜杠变单反斜杠
        json_string.replace('\\"', '"'),   # 转义引号变正常引号
    ]
    
    # 添加更多清理变体
    temp = json_string
    for _ in range(5):  # 多轮清理
        temp = temp.replace('\\\\\\\\', '\\\\')
        temp = temp.replace('\\\\\\"', '\\"')
        variants.append(temp)
    
    # 移除外层引号的变体
    for variant in variants[:]:
        if variant.startswith('"') and variant.endswith('"'):
            variants.append(variant[1:-1])
    
    print(f"生成 {len(variants)} 个清理变体")
    
    # 方法3: 正则表达式直接提取JSON对象
    print("\n方法3: 正则表达式提取")
    
    # 匹配可能的JSON数组或对象
    patterns = [
        r'\[\s*\{[^}]*"platformID"[^}]*\}[^\]]*\]',  # 数组格式
        r'\{[^}]*"platformID"[^}]*\}',  # 对象格式
        r'"roleList"\s*:\s*"[^"]*\{[^}]*"platformID"[^}]*\}[^"]*"',  # 嵌套字符串中的JSON
    ]
    
    extracted_objects = []
    
    for pattern in patterns:
        matches = re.finditer(pattern, json_string)
        for match in matches:
            extracted_objects.append(match.group())
    
    print(f"正则表达式提取到 {len(extracted_objects)} 个候选对象")
    
    # 尝试解析所有候选数据
    print("\n开始尝试解析所有候选数据...")
    
    all_roles = []
    
    # 尝试解析变体
    for i, variant in enumerate(variants):
        try:
            data = json.loads(variant)
            roles = extract_roles_from_data(data)
            if roles:
                print(f"✅ 变体 {i+1} 解析成功: {len(roles)} 个角色")
                all_roles.extend(roles)
        except Exception as e:
            pass  # 忽略解析错误
    
    # 尝试解析提取的对象
    for i, obj_str in enumerate(extracted_objects):
        # 清理提取的字符串
        cleaned = obj_str.strip()
        if cleaned.startswith('"') and cleaned.endswith('"'):
            cleaned = cleaned[1:-1]
        
        try:
            # 尝试作为完整JSON解析
            data = json.loads(cleaned)
            roles = extract_roles_from_data(data)
            if roles:
                print(f"✅ 提取对象 {i+1} 解析成功: {len(roles)} 个角色")
                all_roles.extend(roles)
        except:
            # 如果失败，尝试作为角色列表解析
            try:
                if cleaned.startswith('[') and cleaned.endswith(']'):
                    roles = json.loads(cleaned)
                    if isinstance(roles, list) and len(roles) > 0:
                        print(f"✅ 提取对象 {i+1} 直接解析为列表: {len(roles)} 个角色")
                        all_roles.extend(roles)
            except:
                pass
    
    # 去重（基于roleID）
    unique_roles = []
    seen_ids = set()
    
    for role in all_roles:
        role_id = role.get('roleID', '')
        if role_id and role_id not in seen_ids:
            unique_roles.append(role)
            seen_ids.add(role_id)
    
    print(f"\n🎉 最终结果: 找到 {len(unique_roles)} 个唯一角色")
    return unique_roles

def extract_roles_from_data(data):
    """从数据结构中提取角色列表"""
    if isinstance(data, list):
        # 直接是角色列表
        return [item for item in data if isinstance(item, dict) and 'platformID' in item]
    
    elif isinstance(data, dict):
        # 在字典中查找
        roles = []
        
        # 直接查找roleList
        if 'roleList' in data:
            role_data = data['roleList']
            if isinstance(role_data, list):
                return [item for item in role_data if isinstance(item, dict)]
            elif isinstance(role_data, str):
                try:
                    parsed = json.loads(role_data)
                    if isinstance(parsed, list):
                        return [item for item in parsed if isinstance(item, dict)]
                except:
                    pass
        
        # 递归搜索所有值
        for value in data.values():
            found = extract_roles_from_data(value)
            if found:
                roles.extend(found)
        
        return roles
    
    return []

def display_results(roles):
    """显示解析结果"""
    if not roles:
        print("❌ 未能解析到任何角色数据")
        return
    
    print("\n" + "="*80)
    print("🎯 解析成功的游戏代练角色")
    print("="*80)
    
    # 基本统计
    total_roles = len(roles)
    prices = [role.get('price', 0) for role in roles]
    total_value = sum(prices)
    
    print(f"\n📊 基本统计:")
    print(f"   • 总角色数: {total_roles}")
    print(f"   • 总价值: {total_value:,}")
    print(f"   • 平均价格: {total_value/total_roles:,.0f}" if total_roles > 0 else "")
    print(f"   • 最高价格: {max(prices):,}")
    print(f"   • 最低价格: {min(prices):,}")
    
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
        print(f"   • {plat}: {count}个")
    
    print(f"\n📱 渠道分布:")
    for chan, count in sorted(channels.items(), key=lambda x: x[1], reverse=True):
        print(f"   • {chan}: {count}个")
    
    # 详细信息展示（前15个）
    print(f"\n📋 角色详情 (显示前15个):")
    print("-" * 80)
    
    for i, role in enumerate(roles[:15], 1):
        print(f"\n#{i:2d} 🔥 高战力角色")
        print(f"    平台: {role.get('platformID', 'N/A')} | 渠道: {role.get('channelID', 'N/A')}")
        print(f"    分区: {role.get('partitionID', 'N/A')} | 角色ID: {role.get('roleID', 'N/A')}")
        
        # 游戏属性
        summary = role.get('gameSummary', {})
        if summary:
            combat = summary.get('CombatPower', 0)
            level = summary.get('Level', 0)
            home_level = summary.get('HouselandLevel', 0)
            print(f"    战力: {combat:,} | 等级: {level}级 | 家园: {home_level}级")
        
        # 交易信息
        price = role.get('price', 0)
        fav_count = role.get('favAmount', 0)
        bargain = '可议价' if role.get('allowBargain', False) else '不可议价'
        print(f"    价格: {price:,} | 收藏: {fav_count} | {bargain}")
        
        # 商品状态
        status = role.get('commodityStatus', 'N/A')
        sn = role.get('commoditySN', 'N/A')
        print(f"    状态: {status} | 编号: {sn}")
        
        # 标签信息
        tags_str = role.get('gameTags', '{}')
        try:
            tags_data = json.loads(tags_str) if isinstance(tags_str, str) else tags_str
            tags = tags_data.get('allTags', [])
            tag_names = [tag.get('name', '') for tag in tags if tag.get('name')]
            if tag_names:
                print(f"    标签: {', '.join(tag_names[:3])}")  # 只显示前3个标签
        except:
            pass
        
        if i < min(15, len(roles)):
            print("    " + "─" * 50)
    
    if len(roles) > 15:
        print(f"\n... 还有 {len(roles) - 15} 个角色未显示")
    
    # 价格排行榜
    print(f"\n🏆 价格排行榜 (前10):")
    print("-" * 60)
    sorted_roles = sorted(roles, key=lambda x: x.get('price', 0), reverse=True)[:10]
    
    for i, role in enumerate(sorted_roles, 1):
        summary = role.get('gameSummary', {})
        combat = summary.get('CombatPower', 0)
        price = role.get('price', 0)
        partition = role.get('partitionID', 'N/A')
        print(f"{i:2d}. 💰{price:>8,} | ⚔{combat:>7,}战力 | 分区{partition}")

def main():
    # 复杂的JSON数据
    complex_json = '''{"ret": 0, "rsp": {"response":{"data":"{\\"ret\\":0,\\"msg\\":\\"\\",\\"data\\":{\\"roleList\\":\\"[{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"246\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"67619986511757\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":210687,\\\\\\"CustomXId\\\\\\":20102,\\\\\\"HeadId\\\\\\":1019,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":74237,\\\\\\"Level\\\\\\":94,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1200000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260118034250518-26-7NNp1Id9f\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":25,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"198\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"54425837185673\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":208184,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1016,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":39412,\\\\\\"Level\\\\\\":92,\\\\\\"PlayerNation\\\\\\":3},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1800000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260116163049475-94-NsGCeO2eJ\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":113,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"655\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"180045052893518\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":207435,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":35,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":56526,\\\\\\"Level\\\\\\":92,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]}]}\\\\\\",\\\\\\"price\\\\\\":1350000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260128093922935-95-XWICYnDWx\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":87,\\\\\\"allowBargain\\\\\\":false,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"613\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"168500173413411\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":206918,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1009,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":71501,\\\\\\"Level\\\\\\":93,\\\\\\"PlayerNation\\\\\\":3},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1488800,\\\\\\"commoditySN\\\\\\":\\\\\\"20260217103541564-83-5Kv2XLzaF\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":15,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"700\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"192414566765525\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":204828,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":46,\\\\\\"HouselandLevel\\\\\\":29,\\\\\\"HouselandPoint\\\\\\":23765,\\\\\\"Level\\\\\\":93,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":888800,\\\\\\"commoditySN\\\\\\":\\\\\\"20260211193454304-86-Wfu56RCys\\\\\\",\\\\\\"commodityStatus\\\\\\":300,\\\\\\"favAmount\\\\\\":40,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"587\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"161353340481140\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":204200,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1010,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":45189,\\\\\\"Level\\\\\\":90,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":2800000,\\\\\\"commoditySN\\\\\\":\\\\\\"20240804141008787-8-YCd48jKFmW\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":234,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"647\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"177846030539789\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":203298,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1005,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":31162,\\\\\\"Level\\\\\\":91,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1099900,\\\\\\"commoditySN\\\\\\":\\\\\\"20260219233927879-11-Gg9sfe4np\\\\\\",\\\\\\"commodityStatus\\\\\\":300,\\\\\\"favAmount\\\\\\":2,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"611\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"167950416905313\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":202475,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1009,\\\\\\"HouselandLevel\\\\\\":31,\\\\\\"HouselandPoint\\\\\\":22045,\\\\\\"Level\\\\\\":91,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":500000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260126005130157-98-yqD47jeVj\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":43,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"373\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"102529509267213\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":201800,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1002,\\\\\\"HouselandLevel\\\\\\":30,\\\\\\"HouselandPoint\\\\\\":24213,\\\\\\"Level\\\\\\":88,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":820000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260204011008324-25-OffQ1YsoN\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":140,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"208\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"57174618222858\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":201003,\\\\\\"CustomXId\\\\\\":20102,\\\\\\"HeadId\\\\\\":1009,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":94228,\\\\\\"Level\\\\\\":90,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":3300000,\\\\\\"commoditySN\\\\\\":\\\\\\"20251105200504820-86-ll2JBCz00\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":475,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"325\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"89335359825821\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":200608,\\\\\\"CustomXId\\\\\\":20194,\\\\\\"HeadId\\\\\\":1018,\\\\\\"HouselandLevel\\\\\\":30,\\\\\\"HouselandPoint\\\\\\":19058,\\\\\\"Level\\\\\\":90,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]}]}\\\\\\",\\\\\\"price\\\\\\":500000,\\\\\\"commoditySN\\\\\\":\\\\\\"20251221111008046-56-X4sSvPlQ5\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":123,\\\\\\"allowBargain\\\\\\":false,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"723\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"198736763199599\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":200085,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":75,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":19172,\\\\\\"Level\\\\\\":96,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":700000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260216130818821-97-b00H8v0uq\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":17,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"196\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"53876080819465\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":198572,\\\\\\"CustomXId\\\\\\":20103,\\\\\\"HeadId\\\\\\":25,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":35183,\\\\\\"Level\\\\\\":91,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":800000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260208144602396-28-EScHCHIJt\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":38,\\\\\\"allowBargain\\\\\\":false,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]}]\\"}}}}}}'''
    
    print("🚀 启动终极游戏数据解析器")
    print("=" * 60)
    
    # 执行解析
    roles = ultimate_json_extractor(complex_json)
    
    # 显示结果
    display_results(roles)
    
    print(f"\n✨ 解析任务完成! 成功提取 {len(roles)} 个游戏代练角色")

if __name__ == "__main__":
    main()