import requests
import json
import time
from typing import Dict, Any

class GameRoleFetcher:
    """游戏代练角色数据获取器"""
    
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://capiv2.xinyue.qq.com/cgi-bin/vip_qzproxy.fcgi"
        
    def get_headers(self) -> Dict[str, str]:
        """获取请求头"""
        return {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "content-type": "text/plain",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site"
        }
    
    def build_request_body(self) -> Dict[str, Any]:
        """构建请求体"""
        # 当前时间戳
        timestamp = int(time.time())
        
        return {
            "request": {
                "device": "unknown",
                "openid": "o3wdptyOmvHJ3iQlV2MRrhjmmqrw",
                "acct_type": "wx",
                "appid": "wx5a3bbeac0d87c75a",
                "access_token": "101_K1f_cKRAbVAZ8ey4iUP3Y-7tspqCWZ4gsbtdy4nxEWj3Gp4GE4oKmiwG4AGMCLkJzAbrVD4WYEHZUZ307O5F5xX_IsVu59TSviAlcWGAVII",
                "timestamp": timestamp,
                "cmd": "QueryRoleSummary",
                "business": f"o3wdptyOmvHJ3iQlV2MRrhjmmqrw_{timestamp}",
                "sign": "84f0293e09aab79beef73b154acef65d",
                "req": "{\"gameID\":\"1396\",\"pageSize\":15,\"sSort\":\"combatPower=desc\"}"
            }
        }
    
    def fetch_game_roles(self) -> Dict[str, Any]:
        """获取游戏代练角色数据"""
        try:
            # 构建请求参数
            params = {"cmd": "jjsonrouter", "_t": int(time.time() * 1000)}
            headers = self.get_headers()
            body = self.build_request_body()
            
            print("🚀 发送游戏代练角色查询请求...")
            print(f"请求URL: {self.base_url}")
            print(f"请求参数: {params}")
            print(f"请求体: {json.dumps(body, indent=2, ensure_ascii=False)}")
            
            # 发送POST请求
            response = self.session.post(
                url=self.base_url,
                params=params,
                headers=headers,
                json=body,  # 使用json参数自动处理序列化
                timeout=30
            )
            
            print(f"响应状态码: {response.status_code}")
            print(f"响应头: {dict(response.headers)}")
            
            # 检查响应状态
            response.raise_for_status()
            
            # 解析响应
            try:
                result = response.json()
                print("✅ 请求成功!")
                return result
            except json.JSONDecodeError:
                print("❌ 响应不是有效的JSON格式")
                print(f"响应内容: {response.text[:500]}...")
                return {"error": "Invalid JSON response", "raw_content": response.text}
                
        except requests.exceptions.RequestException as e:
            print(f"❌ 请求失败: {str(e)}")
            return {"error": str(e)}
        except Exception as e:
            print(f"❌ 未知错误: {str(e)}")
            return {"error": str(e)}
    
    def parse_and_display_results(self, data: Dict[str, Any]):
        """解析并显示结果"""
        if "error" in data:
            print(f"\n❌ 错误信息: {data['error']}")
            return
        
        print("\n" + "="*80)
        print("🎮 游戏代练角色查询结果")
        print("="*80)
        
        # 检查响应结构
        if "ret" in data:
            print(f"返回码: {data['ret']}")
        
        if "rsp" in data and "response" in data["rsp"]:
            response_data = data["rsp"]["response"]
            print(f"响应数据: {json.dumps(response_data, indent=2, ensure_ascii=False)}")
            
            # 如果有data字段，进一步解析
            if "data" in response_data:
                try:
                    inner_data = json.loads(response_data["data"])
                    print(f"\n-inner data: {json.dumps(inner_data, indent=2, ensure_ascii=False)}")
                    
                    # 解析角色列表
                    if "roleList" in inner_data:
                        role_list_str = inner_data["roleList"]
                        try:
                            roles = json.loads(role_list_str)
                            self.display_roles(roles)
                        except json.JSONDecodeError:
                            print("角色列表解析失败")
                            
                except json.JSONDecodeError:
                    print("内层数据解析失败")
        else:
            print("未找到预期的响应结构")
            print(f"完整响应: {json.dumps(data, indent=2, ensure_ascii=False)}")
    
    def display_roles(self, roles: list):
        """显示角色信息"""
        if not roles:
            print("未找到角色数据")
            return
            
        print(f"\n📋 找到 {len(roles)} 个游戏代练角色:")
        print("-" * 80)
        
        for i, role in enumerate(roles[:10], 1):  # 显示前10个
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
            
            if i < min(10, len(roles)):
                print("   " + "-" * 40)
        
        if len(roles) > 10:
            print(f"\n... 还有 {len(roles) - 10} 个角色未显示")

def main():
    """主函数"""
    print("🎮 游戏代练角色数据获取工具")
    print("=" * 50)
    
    # 创建获取器实例
    fetcher = GameRoleFetcher()
    
    # 获取数据
    result = fetcher.fetch_game_roles()
    
    # 解析并显示结果
    fetcher.parse_and_display_results(result)
    
    print(f"\n✨ 任务完成!")

if __name__ == "__main__":
    main()