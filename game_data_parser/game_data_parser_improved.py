import json
import re
from typing import Dict, List, Any, Tuple

class GameDataParser:
    """游戏代练角色数据解析器"""
    
    def __init__(self):
        self.role_list = []
        self.stats = {}
        
    def clean_json_string(self, json_str: str) -> str:
        """清理JSON字符串，移除多余字符"""
        # 移除开头和结尾的引号
        if json_str.startswith("'") and json_str.endswith("'"):
            json_str = json_str[1:-1]
        if json_str.startswith('"') and json_str.endswith('"'):
            json_str = json_str[1:-1]
            
        # 替换转义字符
        json_str = json_str.replace('\\"', '"')
        json_str = json_str.replace('\\\\', '\\')
        
        return json_str
    
    def parse_nested_json(self, json_str: str) -> Dict:
        """递归解析嵌套的JSON结构"""
        try:
            # 尝试直接解析
            return json.loads(json_str)
        except json.JSONDecodeError:
            # 如果失败，尝试清理后再解析
            cleaned_str = self.clean_json_string(json_str)
            try:
                return json.loads(cleaned_str)
            except json.JSONDecodeError as e:
                print(f"JSON解析错误: {e}")
                print(f"原始字符串长度: {len(json_str)}")
                print(f"清理后字符串长度: {len(cleaned_str)}")
                # 尝试提取有效的JSON部分
                return self.extract_valid_json(json_str)
    
    def extract_valid_json(self, text: str) -> Dict:
        """从文本中提取有效的JSON部分"""
        # 查找第一个 { 和最后一个 } 之间的内容
        start = text.find('{')
        end = text.rfind('}')
        
        if start != -1 and end != -1 and end > start:
            json_part = text[start:end+1]
            try:
                return json.loads(json_part)
            except:
                pass
        
        # 如果还是失败，返回空字典
        return {}
    
    def parse_role_list(self, role_list_str: str) -> List[Dict]:
        """解析角色列表字符串"""
        try:
            # 直接解析
            return json.loads(role_list_str)
        except json.JSONDecodeError:
            try:
                # 清理后解析
                cleaned = self.clean_json_string(role_list_str)
                return json.loads(cleaned)
            except json.JSONDecodeError:
                # 手动解析数组格式
                return self.parse_manual_array(role_list_str)
    
    def parse_manual_array(self, array_str: str) -> List[Dict]:
        """手动解析数组格式的字符串"""
        roles = []
        # 移除外层的方括号和引号
        content = array_str.strip()
        if content.startswith('"[') and content.endswith(']"'):
            content = content[2:-2]
        elif content.startswith('[') and content.endswith(']'):
            content = content[1:-1]
            
        # 分割对象（简单的分割方法）
        objects = []
        brace_count = 0
        current_obj = ""
        
        for char in content:
            if char == '{':
                brace_count += 1
                current_obj += char
            elif char == '}':
                brace_count -= 1
                current_obj += char
                if brace_count == 0:
                    objects.append(current_obj)
                    current_obj = ""
            elif brace_count > 0:
                current_obj += char
                
        # 解析每个对象
        for obj_str in objects:
            try:
                role_data = json.loads(obj_str)
                roles.append(role_data)
            except:
                print(f"无法解析角色对象: {obj_str[:100]}...")
                
        return roles
    
    def parse_game_data(self, json_str: str) -> bool:
        """主解析函数"""
        try:
            print("开始解析游戏数据...")
            
            # 解析外层JSON
            outer_data = self.parse_nested_json(json_str)
            if not outer_data:
                print("外层JSON解析失败")
                return False
            
            # 获取内层data字段
            rsp_data = outer_data.get('rsp', {}).get('response', {}).get('data', '')
            if not rsp_data:
                print("未找到内层data字段")
                return False
            
            # 解析内层JSON
            inner_data = self.parse_nested_json(rsp_data)
            if not inner_data:
                print("内层JSON解析失败")
                return False
            
            # 获取角色列表
            role_list_str = inner_data.get('data', {}).get('roleList', '[]')
            if not role_list_str or role_list_str == '[]':
                print("角色列表为空")
                return False
            
            # 解析角色列表
            self.role_list = self.parse_role_list(role_list_str)
            
            if not self.role_list:
                print("角色列表解析失败")
                return False
                
            print(f"成功解析 {len(self.role_list)} 个角色")
            return True
            
        except Exception as e:
            print(f"解析过程中发生错误: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    def calculate_statistics(self):
        """计算统计数据"""
        if not self.role_list:
            return
            
        self.stats = {
            'total_roles': len(self.role_list),
            'total_price': 0,
            'platform_stats': {},
            'channel_stats': {},
            'price_range': [],
            'avg_price': 0,
            'max_price': 0,
            'min_price': 0
        }
        
        for role in self.role_list:
            try:
                price = role.get('price', 0)
                self.stats['total_price'] += price
                self.stats['price_range'].append(price)
                
                platform = role.get('platformID', 'unknown')
                channel = role.get('channelID', 'unknown')
                
                self.stats['platform_stats'][platform] = self.stats['platform_stats'].get(platform, 0) + 1
                self.stats['channel_stats'][channel] = self.stats['channel_stats'].get(channel, 0) + 1
            except Exception as e:
                print(f"统计角色数据时出错: {e}")
        
        if self.stats['price_range']:
            self.stats['avg_price'] = self.stats['total_price'] / len(self.stats['price_range'])
            self.stats['max_price'] = max(self.stats['price_range'])
            self.stats['min_price'] = min(self.stats['price_range'])
    
    def display_role_details(self):
        """显示角色详细信息"""
        print("=" * 80)
        print("游戏代练角色信息解析结果")
        print("=" * 80)
        
        print(f"\n总共找到 {len(self.role_list)} 个游戏代练角色：\n")
        
        for i, role in enumerate(self.role_list, 1):
            print(f"--- 角色 {i} ---")
            
            # 基本信息
            print(f"平台ID: {role.get('platformID', 'N/A')}")
            print(f"渠道ID: {role.get('channelID', 'N/A')}")
            print(f"分区ID: {role.get('partitionID', 'N/A')}")
            print(f"角色ID: {role.get('roleID', 'N/A')}")
            print(f"玩家名称: {role.get('playerName', '未命名')}")
            
            # 游戏属性
            game_summary = role.get('gameSummary', {})
            if game_summary:
                print(f"战力: {game_summary.get('CombatPower', 0):,}")
                print(f"等级: {game_summary.get('Level', 0)}级")
                print(f"家园等级: {game_summary.get('HouselandLevel', 0)}级")
                print(f"家园积分: {game_summary.get('HouselandPoint', 0):,}")
                print(f"国家: {game_summary.get('PlayerNation', 'N/A')}")
                print(f"头像ID: {game_summary.get('HeadId', 'N/A')}")
                print(f"自定义ID: {game_summary.get('CustomXId', 'N/A')}")
            
            # 标签信息
            game_tags_str = role.get('gameTags', '{}')
            try:
                game_tags = json.loads(game_tags_str) if isinstance(game_tags_str, str) else game_tags_str
                tags = game_tags.get('allTags', [])
                tag_names = [tag.get('name', '') for tag in tags if tag.get('name')]
                print(f"标签: {', '.join(tag_names) if tag_names else '无'}")
            except Exception:
                print("标签: 解析失败")
            
            # 交易信息
            price = role.get('price', 0)
            print(f"价格: {price:,}")
            print(f"收藏数: {role.get('favAmount', 0)}")
            print(f"是否可议价: {'是' if role.get('allowBargain', False) else '否'}")
            print(f"议价状态: {role.get('bargainStatus', 'N/A')}")
            print(f"商品状态: {role.get('commodityStatus', 'N/A')}")
            print(f"商品编号: {role.get('commoditySN', 'N/A')}")
            
            print("-" * 50)
    
    def display_statistics(self):
        """显示统计信息"""
        if not self.stats:
            print("暂无统计数据")
            return
            
        print("\n" + "=" * 80)
        print("统计信息")
        print("=" * 80)
        
        print(f"总角色数: {self.stats['total_roles']}")
        print(f"总价: {self.stats['total_price']:,}")
        print(f"平均价: {self.stats['avg_price']:,.0f}")
        print(f"最高价: {self.stats['max_price']:,}")
        print(f"最低价: {self.stats['min_price']:,}")
        
        print("\n平台分布:")
        for platform, count in sorted(self.stats['platform_stats'].items(), key=lambda x: x[1], reverse=True):
            print(f"  {platform}: {count}个")
            
        print("\n渠道分布:")
        for channel, count in sorted(self.stats['channel_stats'].items(), key=lambda x: x[1], reverse=True):
            print(f"  {channel}: {count}个")
            
        # 按价格排序显示前10名
        print("\n价格排名前10的角色:")
        sorted_roles = sorted(enumerate(self.role_list), key=lambda x: x[1].get('price', 0), reverse=True)[:10]
        for i, (index, role) in enumerate(sorted_roles, 1):
            game_summary = role.get('gameSummary', {})
            combat_power = game_summary.get('CombatPower', 0)
            price = role.get('price', 0)
            partition = role.get('partitionID', 'N/A')
            print(f"{i:2d}. 战力{combat_power:>7,} | 价格{price:>8,} | 分区{partition}")

def main():
    # 测试数据
    json_data = '''{"ret": 0, "rsp": {"response":{"data":"{\\"ret\\":0,\\"msg\\":\\"\\",\\"data\\":{\\"roleList\\":\\"[{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"246\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"67619986511757\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":210687,\\\\\\"CustomXId\\\\\\":20102,\\\\\\"HeadId\\\\\\":1019,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":74237,\\\\\\"Level\\\\\\":94,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1200000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260118034250518-26-7NNp1Id9f\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":25,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"198\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"54425837185673\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":208184,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1016,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":39412,\\\\\\"Level\\\\\\":92,\\\\\\"PlayerNation\\\\\\":3},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1800000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260116163049475-94-NsGCeO2eJ\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":113,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"655\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"180045052893518\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":207435,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":35,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":56526,\\\\\\"Level\\\\\\":92,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]}]}\\\\\\",\\\\\\"price\\\\\\":1350000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260128093922935-95-XWICYnDWx\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":87,\\\\\\"allowBargain\\\\\\":false,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"613\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"168500173413411\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":206918,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1009,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":71501,\\\\\\"Level\\\\\\":93,\\\\\\"PlayerNation\\\\\\":3},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1488800,\\\\\\"commoditySN\\\\\\":\\\\\\"20260217103541564-83-5Kv2XLzaF\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":15,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"700\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"192414566765525\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":204828,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":46,\\\\\\"HouselandLevel\\\\\\":29,\\\\\\"HouselandPoint\\\\\\":23765,\\\\\\"Level\\\\\\":93,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":888800,\\\\\\"commoditySN\\\\\\":\\\\\\"20260211193454304-86-Wfu56RCys\\\\\\",\\\\\\"commodityStatus\\\\\\":300,\\\\\\"favAmount\\\\\\":40,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"587\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"161353340481140\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":204200,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1010,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":45189,\\\\\\"Level\\\\\\":90,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":2800000,\\\\\\"commoditySN\\\\\\":\\\\\\"20240804141008787-8-YCd48jKFmW\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":234,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"647\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"177846030539789\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":203298,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1005,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":31162,\\\\\\"Level\\\\\\":91,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":1099900,\\\\\\"commoditySN\\\\\\":\\\\\\"20260219233927879-11-Gg9sfe4np\\\\\\",\\\\\\"commodityStatus\\\\\\":300,\\\\\\"favAmount\\\\\\":2,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"611\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"167950416905313\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":202475,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1009,\\\\\\"HouselandLevel\\\\\\":31,\\\\\\"HouselandPoint\\\\\\":22045,\\\\\\"Level\\\\\\":91,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":500000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260126005130157-98-yqD47jeVj\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":43,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"373\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"102529509267213\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":201800,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":1002,\\\\\\"HouselandLevel\\\\\\":30,\\\\\\"HouselandPoint\\\\\\":24213,\\\\\\"Level\\\\\\":88,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":820000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260204011008324-25-OffQ1YsoN\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":140,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"208\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"57174618222858\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":201003,\\\\\\"CustomXId\\\\\\":20102,\\\\\\"HeadId\\\\\\":1009,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":94228,\\\\\\"Level\\\\\\":90,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰è³é¼ \\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":3300000,\\\\\\"commoditySN\\\\\\":\\\\\\"20251105200504820-86-ll2JBCz00\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":475,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"ios\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"325\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"89335359825821\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":200608,\\\\\\"CustomXId\\\\\\":20194,\\\\\\"HeadId\\\\\\":1018,\\\\\\"HouselandLevel\\\\\\":30,\\\\\\"HouselandPoint\\\\\\":19058,\\\\\\"Level\\\\\\":90,\\\\\\"PlayerNation\\\\\\":1},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]}]}\\\\\\",\\\\\\"price\\\\\\":500000,\\\\\\"commoditySN\\\\\\":\\\\\\"20251221111008046-56-X4sSvPlQ5\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":123,\\\\\\"allowBargain\\\\\\":false,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"qq\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"723\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"198736763199599\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":200085,\\\\\\"CustomXId\\\\\\":20105,\\\\\\"HeadId\\\\\\":75,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":19172,\\\\\\"Level\\\\\\":96,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"çžå…½æ¶‚åå›\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":700000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260216130818821-97-b00H8v0uq\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":17,\\\\\\"allowBargain\\\\\\":true,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]},{\\\\\\"platformID\\\\\\":\\\\\\"and\\\\\\",\\\\\\"channelID\\\\\\":\\\\\\"wx\\\\\\",\\\\\\"partitionID\\\\\\":\\\\\\"196\\\\\\",\\\\\\"roleID\\\\\\":\\\\\\"53876080819465\\\\\\",\\\\\\"playerName\\\\\\":\\\\\\"\\\\\\",\\\\\\"gameSummary\\\\\\":{\\\\\\"CombatPower\\\\\\":198572,\\\\\\"CustomXId\\\\\\":20103,\\\\\\"HeadId\\\\\\":25,\\\\\\"HouselandLevel\\\\\\":32,\\\\\\"HouselandPoint\\\\\\":35183,\\\\\\"Level\\\\\\":91,\\\\\\"PlayerNation\\\\\\":2},\\\\\\"gameTags\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"allTags\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"qczb\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å…çºè…å‡\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[6]},{\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"shenshou\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"name\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"å ç‰æ”ç¿¼éŸ\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"dimension\\\\\\\\\\\\\\":[0]}]}\\\\\\",\\\\\\"price\\\\\\":800000,\\\\\\"commoditySN\\\\\\":\\\\\\"20260208144602396-28-EScHCHIJt\\\\\\",\\\\\\"commodityStatus\\\\\\":400,\\\\\\"favAmount\\\\\\":38,\\\\\\"allowBargain\\\\\\":false,\\\\\\"bargainStatus\\\\\\":0,\\\\\\"playerTags\\\\\\":[]}]\\"}}}}}}'''
    
    # 创建解析器实例
    parser = GameDataParser()
    
    # 解析数据
    if parser.parse_game_data(json_data):
        # 计算统计信息
        parser.calculate_statistics()
        
        # 显示详细信息和统计
        parser.display_role_details()
        parser.display_statistics()
    else:
        print("数据解析失败")

if __name__ == "__main__":
    main()