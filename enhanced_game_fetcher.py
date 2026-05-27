import requests
import json
import time
from typing import Dict, Any, Optional
import urllib3

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class EnhancedGameRoleFetcher:
    """增强版游戏代练角色数据获取器"""
    
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://capiv2.xinyue.qq.com/cgi-bin/vip_qzproxy.fcgi"
        # 设置会话参数
        self.session.verify = False  # 忽略SSL证书验证
        
    def get_enhanced_headers(self) -> Dict[str, str]:
        """获取增强的请求头"""
        return {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "content-type": "text/plain;charset=UTF-8",
            "origin": "https://xinyue.qq.com",
            "pragma": "no-cache",
            "referer": "https://xinyue.qq.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
            "priority": "u=1, i",
            "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site"
        }
    
    def build_dynamic_request(self, game_id: str = "1396", page_size: int = 15) -> Dict[str, Any]:
        """构建动态请求体"""
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
                "business": f"o3wdptyOmvHJ3iQlV2MRrhjmmqrw_{timestamp}_{int(time.time()*1000)}",
                "sign": self.generate_sign(timestamp),
                "req": json.dumps({
                    "gameID": game_id,
                    "pageSize": page_size,
                    "sSort": "combatPower=desc",
                    "pageIndex": 1
                }, separators=(',', ':'))
            }
        }
    
    def generate_sign(self, timestamp: int) -> str:
        """生成签名（简化版）"""
        # 实际应用中这里应该根据具体算法生成签名
        # 这里使用固定的签名作为示例
        return "84f0293e09aab79beef73b154acef65d"
    
    def fetch_with_retry(self, max_retries: int = 3) -> Dict[str, Any]:
        """带重试机制的请求获取"""
        for attempt in range(max_retries):
            try:
                print(f"\n🔄 第 {attempt + 1} 次尝试获取数据...")
                
                # 构建请求
                params = {
                    "cmd": "jjsonrouter", 
                    "_t": int(time.time() * 1000)
                }
                headers = self.get_enhanced_headers()
                body = self.build_dynamic_request()
                
                print("🚀 发送请求...")
                print(f"URL: {self.base_url}")
                print(f"参数: {params}")
                
                # 发送请求
                response = self.session.post(
                    url=self.base_url,
                    params=params,
                    headers=headers,
                    json=body,
                    timeout=30,
                    verify=False
                )
                
                print(f"状态码: {response.status_code}")
                
                # 检查响应
                if response.status_code == 200:
                    try:
                        result = response.json()
                        ret_code = result.get('ret', 0)
                        
                        if ret_code == 0:
                            print("✅ 请求成功!")
                            return result
                        else:
                            print(f"⚠️  返回码异常: {ret_code}")
                            error_msg = self.get_error_message(ret_code)
                            print(f"错误描述: {error_msg}")
                            
                    except json.JSONDecodeError:
                        print("❌ 响应不是有效的JSON")
                        print(f"响应内容: {response.text[:200]}")
                        
                else:
                    print(f"❌ HTTP错误: {response.status_code}")
                    
            except requests.exceptions.RequestException as e:
                print(f"❌ 请求异常: {str(e)}")
            except Exception as e:
                print(f"❌ 未知错误: {str(e)}")
            
            # 重试间隔
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # 指数退避
                print(f"等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
        
        return {"error": "所有重试都失败了", "attempts": max_retries}
    
    def get_error_message(self, ret_code: int) -> str:
        """获取错误码对应的描述"""
        error_messages = {
            24010005: "认证失败或访问权限不足",
            24010001: "参数错误",
            24010002: "系统内部错误",
            24010003: "服务不可用",
            0: "成功"
        }
        return error_messages.get(ret_code, f"未知错误码: {ret_code}")
    
    def analyze_response_structure(self, data: Dict[str, Any]):
        """分析响应结构"""
        print("\n" + "="*80)
        print("📊 响应结构分析")
        print("="*80)
        
        if "error" in data:
            print(f"❌ 错误: {data['error']}")
            return
        
        # 基本信息
        print(f"返回码: {data.get('ret', 'N/A')}")
        print(f"消息: {data.get('msg', 'N/A')}")
        
        # 响应体分析
        if "rsp" in data:
            rsp = data["rsp"]
            print(f"\n响应体结构:")
            for key in rsp.keys():
                print(f"  - {key}")
                
            if "response" in rsp:
                response = rsp["response"]
                print(f"\nresponse字段:")
                for key, value in response.items():
                    if isinstance(value, str) and len(value) > 100:
                        print(f"  {key}: [字符串长度 {len(value)}]")
                    else:
                        print(f"  {key}: {value}")
        
        # 完整JSON展示
        print(f"\n完整响应JSON:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    
    def save_raw_response(self, data: Dict[str, Any], filename: str = "raw_response.json"):
        """保存原始响应到文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"💾 原始响应已保存到: {filename}")
        except Exception as e:
            print(f"❌ 保存文件失败: {e}")

def main():
    """主函数"""
    print("🎮 增强版游戏代练角色数据获取器")
    print("=" * 60)
    
    # 创建增强版获取器
    fetcher = EnhancedGameRoleFetcher()
    
    # 获取数据（带重试）
    result = fetcher.fetch_with_retry(max_retries=3)
    
    # 分析响应结构
    fetcher.analyze_response_structure(result)
    
    # 保存原始响应
    fetcher.save_raw_response(result)
    
    print(f"\n✨ 任务完成!")

if __name__ == "__main__":
    main()