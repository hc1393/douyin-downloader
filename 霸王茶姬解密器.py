#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import json
import urllib.parse
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

class BaWangChaJiDecryptor:
    def __init__(self):
        # 霸王茶姬的AES密钥配置
        self.aes_configs = {
            49006: {
                "key": "rbhesOXwy9PIt/ex",
                "iv": "LUDNoZxPB8NRjSY/3FFlBg==",
                "version": "1.0.0"
            },
            11185: {
                "key": "O0aKS9jrZ8rWJPkZ/DgLeQ==",
                "iv": "kX7bfYttP5B7m+GYpX4zEw==",
                "version": "1.0.0"
            },
            11234: {
                "key": "Rc9tOVbZeqtHdPXZplRMjQ==",
                "iv": "pRGevab4vAXFx4hi50W71A==",
                "version": "1.0.0"
            },
            32090: {
                "key": "L3motzLgk04no7l9yfjC+A==",
                "iv": "rWJYADRHpXU0iCrt44mRsA==",
                "version": "1.0.0"
            }
        }
        
        # 自定义Base64字符表
        self.custom_base64_chars = "zIwxnNSGhrFaXiEp9lVOA/=+Kydtem4WZvs3BULRbuP75Y6g2TDcjoQ8JCk1fMqH0"
        self.standard_base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    
    def custom_base64_decode(self, data):
        """自定义Base64解码"""
        try:
            # 将自定义字符映射到标准Base64字符
            translation_table = str.maketrans(self.custom_base64_chars, self.standard_base64_chars)
            standard_data = data.translate(translation_table)
            
            # 添加必要的填充
            missing_padding = len(standard_data) % 4
            if missing_padding:
                standard_data += '=' * (4 - missing_padding)
            
            return base64.b64decode(standard_data)
        except Exception as e:
            print(f"自定义Base64解码失败: {e}")
            return None
    
    def aes_decrypt(self, encrypted_data, key, iv):
        """AES解密"""
        try:
            # 解码密钥和IV
            key_bytes = base64.b64decode(key)
            iv_bytes = base64.b64decode(iv)
            
            # 创建AES解密器
            cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
            
            # 解密数据
            decrypted = cipher.decrypt(encrypted_data)
            
            # 去除填充
            try:
                decrypted = unpad(decrypted, AES.block_size)
            except:
                # 如果自动去填充失败，尝试手动处理
                pass
            
            return decrypted.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"AES解密失败: {e}")
            return None
    
    def decrypt_json_data(self, encrypted_data, store_id=49006):
        """解密JSON数据"""
        print(f"=== 解密store_id: {store_id} 的数据 ===")
        
        if store_id not in self.aes_configs:
            print(f"未找到store_id {store_id} 的配置")
            return None
        
        config = self.aes_configs[store_id]
        print(f"使用密钥: {config['key']}")
        print(f"使用IV: {config['iv']}")
        
        results = {}
        
        for key, value in encrypted_data.items():
            print(f"\n--- 解密字段: {key} ---")
            print(f"原始数据长度: {len(value)}")
            
            # 1. 尝试标准Base64解码
            try:
                decoded = base64.b64decode(value)
                print(f"标准Base64解码成功，长度: {len(decoded)}")
                
                # 2. AES解密
                decrypted = self.aes_decrypt(decoded, config['key'], config['iv'])
                if decrypted:
                    print(f"AES解密结果: {decrypted[:200]}...")
                    results[key] = decrypted
                    
                    # 尝试解析为JSON
                    try:
                        json_data = json.loads(decrypted)
                        print(f"JSON解析成功: {json_data}")
                        results[f"{key}_json"] = json_data
                    except:
                        pass
                else:
                    print("AES解密失败")
                    
            except Exception as e:
                print(f"标准Base64解码失败: {e}")
                
                # 3. 尝试自定义Base64解码
                custom_decoded = self.custom_base64_decode(value)
                if custom_decoded:
                    print(f"自定义Base64解码成功，长度: {len(custom_decoded)}")
                    
                    # AES解密
                    decrypted = self.aes_decrypt(custom_decoded, config['key'], config['iv'])
                    if decrypted:
                        print(f"AES解密结果: {decrypted[:200]}...")
                        results[key] = decrypted
                    else:
                        print("AES解密失败")
                else:
                    print("自定义Base64解码也失败")
        
        return results
    
    def decrypt_cookie(self, cookie_value):
        """解密cookie数据"""
        print(f"\n=== 解密Cookie数据 ===")
        print(f"原始cookie: {cookie_value}")
        
        parts = cookie_value.split('=')
        print(f"分割成 {len(parts)} 个部分")
        
        results = []
        
        for i, part in enumerate(parts):
            print(f"\n--- 解密Cookie部分 {i} ---")
            print(f"内容: {part}")
            
            # 尝试标准Base64解码
            try:
                decoded = base64.b64decode(part)
                print(f"标准Base64解码成功，长度: {len(decoded)}")
                print(f"解码内容(hex): {decoded[:50].hex()}...")
                results.append(decoded)
            except Exception as e:
                print(f"标准Base64解码失败: {e}")
                
                # 尝试自定义Base64解码
                custom_decoded = self.custom_base64_decode(part)
                if custom_decoded:
                    print(f"自定义Base64解码成功，长度: {len(custom_decoded)}")
                    results.append(custom_decoded)
                else:
                    print("所有解码方法都失败")
        
        return results

def main():
    decryptor = BaWangChaJiDecryptor()
    
    # 您提供的加密JSON数据
    encrypted_json = {
        "OOxO0": "VUI2S3gyTTZ2RHRQb3ZWTkZRJVhrIV4lZVdnQ3xlRV1GUSV2LXUPQwEVMDleDB8XIjt0cilFL04ady4XLhEfBG0oeigXWwlUGT42PSkONw8GC1gZEAcYVTwWRDEEOA4aIhRkDgp4JVUxAhkEFxoTHCcQBCg2cBVwJDczHT4kZB8mDAcqFV4mZCR9GQVcOwId",
        "OOxoO": "TU9HZTg3QXJJZFVlOEo2SToyMGE5MDJhYjhmY2JmZDIyZmJjM2ZiNDA2MWJlMmEzN2NkZTk3MTY0NzRmZjJiYzU3ZjZmMWUxYjMxYzUzYzFj",
        "OO0xO": "U2pjc3dWM3BnWWVDUlZBQTozNjg0MGY3ZmU0ZDlmNTA2YzQ4OTlkMmVmNTdmMTJiY2QyN2I4Y2VkOWEwOWYxMjMxY2MzZWIxM2I1NTNhM2EyMDMxZmVjYzBkOTU5NWRhMzJjNjkwN2Y1M2FhMGI2NjgzZDgxNDc2ZTkwNjZhNjUzMzgxNzNiOTc0ZjI3YzdhMDE0MzFhNTI4ZmViZGVkMTNjMWJmMWEzYmU3YmJjOTZiM2M3MzMzZWJjYzRiYjlhYjhkOTllOGVlNzM2ODY0ZDJmMGNhZDMzMDI0YTk0ZWQzYjJhODVmMThjNzIyNmI4ZDZkODU3YTc5ZjVjMGI4YzhkZTQxYWQ3M2I4M2FmNThmYmU5YzliYzUyNWIxYWQwNWViZjQzNDA3NzUzYmNlNmI1OTYwMWYyNjE5M2EwNjcyMWE0NjUwODljMDQzYzNiM2IzMzM2MWY0Yjc2MzI2Y2QwMDY1ZDcwZGI5NDA5YTU3ZDJiMGVlMzM0NzE3MjcyZDBiNTMwMTliMzFhOGI3Y2Y4YjQwNjc1ZDRmOTVjZTk5NjI0NjJiOWZkNjhmMzQ0OGE3NmI2NmU5ZjRmY2Y2ODhjZjI3MDYzZmY0MzIyOWM5MTM1NjIyNGYxYWNlNjFjOWEyZDRlNTMyYzdlZWExNjI"
    }
    
    # 您提供的cookie数据
    cookie_value = "C50qzxuDRD0D2DRhxjxx0xiqYjYeWKG7iFFQDwhOBDCueqi=i73TuUKQDUAmMG7AxGCD8LKGFD7vP=DBwGpoD/fKuKQxleDARzPM9LDDxGWtCDtdD9DW5Gg74YYDUxGjGDzqi8uxqhEKSyE5TDD5887+5DGI1A=v5x2e4RBi4ZAw4Q2eDSp7WDQeDt2mPgAqaKGoKX00AQ0ffjF4L3GxTtQxh9PeDnPmKB6LxQxkIRtlf6RG09IOutnj64D"
    
    # 尝试不同的store_id进行解密
    store_ids = [49006, 11185, 11234, 32090]
    
    for store_id in store_ids:
        print(f"\n{'='*60}")
        print(f"尝试使用 store_id: {store_id}")
        print(f"{'='*60}")
        
        json_results = decryptor.decrypt_json_data(encrypted_json, store_id)
        if json_results:
            print(f"\n成功解密JSON数据:")
            for key, value in json_results.items():
                print(f"{key}: {value}")
            break
    
    # 解密cookie
    cookie_results = decryptor.decrypt_cookie(cookie_value)
    
    print(f"\n{'='*60}")
    print("解密完成")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
