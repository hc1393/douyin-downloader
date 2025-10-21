#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import json
import urllib.parse
import binascii
import re

def try_base64_decode(data):
    """尝试Base64解码"""
    try:
        # 添加必要的填充
        missing_padding = len(data) % 4
        if missing_padding:
            data += '=' * (4 - missing_padding)
        
        decoded = base64.b64decode(data)
        return decoded
    except Exception as e:
        print(f"Base64解码失败: {e}")
        return None

def analyze_binary_data(data, name):
    """分析二进制数据"""
    print(f"\n=== 分析 {name} ===")
    print(f"长度: {len(data)} 字节")
    print(f"前20字节(hex): {data[:20].hex()}")
    print(f"前20字节(ascii): {repr(data[:20])}")
    
    # 尝试UTF-8解码
    try:
        utf8_decoded = data.decode('utf-8')
        print(f"UTF-8解码: {utf8_decoded[:100]}...")
    except:
        print("UTF-8解码失败")
    
    # 尝试URL解码
    try:
        url_decoded = urllib.parse.unquote(data.decode('latin-1'))
        if url_decoded != data.decode('latin-1'):
            print(f"URL解码: {url_decoded[:100]}...")
    except:
        pass
    
    # 检查是否包含JSON
    try:
        json_data = json.loads(data.decode('utf-8'))
        print(f"JSON数据: {json_data}")
    except:
        pass
    
    # 检查是否包含可读文本
    readable_chars = sum(1 for b in data if 32 <= b <= 126)
    readable_ratio = readable_chars / len(data)
    print(f"可读字符比例: {readable_ratio:.2%}")
    
    if readable_ratio > 0.7:
        print(f"可能包含文本数据")

def analyze_encrypted_json():
    """分析加密的JSON数据"""
    
    encrypted_data = {
        "OOxO0": "VUI2S3gyTTZ2RHRQb3ZWTkZRJVhrIV4lZVdnQ3xlRV1GUSV2LXUPQwEVMDleDB8XIjt0cilFL04ady4XLhEfBG0oeigXWwlUGT42PSkONw8GC1gZEAcYVTwWRDEEOA4aIhRkDgp4JVUxAhkEFxoTHCcQBCg2cBVwJDczHT4kZB8mDAcqFV4mZCR9GQVcOwId",
        "OOxoO": "TU9HZTg3QXJJZFVlOEo2SToyMGE5MDJhYjhmY2JmZDIyZmJjM2ZiNDA2MWJlMmEzN2NkZTk3MTY0NzRmZjJiYzU3ZjZmMWUxYjMxYzUzYzFj",
        "OO0xO": "U2pjc3dWM3BnWWVDUlZBQTozNjg0MGY3ZmU0ZDlmNTA2YzQ4OTlkMmVmNTdmMTJiY2QyN2I4Y2VkOWEwOWYxMjMxY2MzZWIxM2I1NTNhM2EyMDMxZmVjYzBkOTU5NWRhMzJjNjkwN2Y1M2FhMGI2NjgzZDgxNDc2ZTkwNjZhNjUzMzgxNzNiOTc0ZjI3YzdhMDE0MzFhNTI4ZmViZGVkMTNjMWJmMWEzYmU3YmJjOTZiM2M3MzMzZWJjYzRiYjlhYjhkOTllOGVlNzM2ODY0ZDJmMGNhZDMzMDI0YTk0ZWQzYjJhODVmMThjNzIyNmI4ZDZkODU3YTc5ZjVjMGI4YzhkZTQxYWQ3M2I4M2FmNThmYmU5YzliYzUyNWIxYWQwNWViZjQzNDA3NzUzYmNlNmI1OTYwMWYyNjE5M2EwNjcyMWE0NjUwODljMDQzYzNiM2IzMzM2MWY0Yjc2MzI2Y2QwMDY1ZDcwZGI5NDA5YTU3ZDJiMGVlMzM0NzE3MjcyZDBiNTMwMTliMzFhOGI3Y2Y4YjQwNjc1ZDRmOTVjZTk5NjI0NjJiOWZkNjhmMzQ0OGE3NmI2NmU5ZjRmY2Y2ODhjZjI3MDYzZmY0MzIyOWM5MTM1NjIyNGYxYWNlNjFjOWEyZDRlNTMyYzdlZWExNjI"
    }
    
    print("=== 分析加密的JSON数据 ===")
    
    for key, value in encrypted_data.items():
        print(f"\n字段: {key}")
        print(f"原始长度: {len(value)}")
        
        decoded = try_base64_decode(value)
        if decoded:
            analyze_binary_data(decoded, key)

def analyze_cookie():
    """分析cookie数据"""
    
    cookie_value = "C50qzxuDRD0D2DRhxjxx0xiqYjYeWKG7iFFQDwhOBDCueqi=i73TuUKQDUAmMG7AxGCD8LKGFD7vP=DBwGpoD/fKuKQxleDARzPM9LDDxGWtCDtdD9DW5Gg74YYDUxGjGDzqi8uxqhEKSyE5TDD5887+5DGI1A=v5x2e4RBi4ZAw4Q2eDSp7WDQeDt2mPgAqaKGoKX00AQ0ffjF4L3GxTtQxh9PeDnPmKB6LxQxkIRtlf6RG09IOutnj64D"
    
    print("\n=== 分析 ssxmod_itna3 Cookie ===")
    print(f"原始cookie: {cookie_value}")
    
    parts = cookie_value.split('=')
    print(f"分割成 {len(parts)} 个部分")
    
    for i, part in enumerate(parts):
        print(f"\n--- 部分 {i} ---")
        print(f"内容: {part}")
        print(f"长度: {len(part)}")
        
        decoded = try_base64_decode(part)
        if decoded:
            analyze_binary_data(decoded, f"Cookie部分{i}")

def main():
    analyze_encrypted_json()
    analyze_cookie()
    
    print("\n=== 总结 ===")
    print("1. 所有数据都是Base64编码的二进制数据")
    print("2. 解码后的数据不是纯文本，可能是加密数据")
    print("3. 需要找到正确的解密密钥或算法")
    print("4. 建议检查相关的JavaScript文件中的解密函数")

if __name__ == "__main__":
    main()
