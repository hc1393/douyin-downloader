#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io

# 设置输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""
分析cookie-tracker.js文件中的加密相关代码
识别哪些是实际使用的，哪些是冗余的
"""

def analyze_cookie_tracker():
    print("=== Cookie Tracker 加密代码分析 ===\n")
    
    print("1. 文件结构分析:")
    print("   - 这是一个混淆的JavaScript文件")
    print("   - 主要功能是cookie追踪和指纹收集")
    print("   - 包含多种加密算法和反调试检测\n")
    
    print("2. 加密相关功能识别:")
    
    # 从代码中提取的加密相关功能
    crypto_functions = {
        "AES加密": {
            "位置": "第1036行",
            "代码": "const {encrypt: {encrypt: ui, decrypt: Qa, encode: Gv, decode: Vp, base64UrlEncode: dE, getRandomString: Up}, hash: {x64hash128: io}} = gv",
            "用途": "指纹数据加密",
            "使用状态": "[使用中] 实际使用"
        },
        
        "RSA加密": {
            "位置": "第1084行",
            "代码": "type: 'RSA'",
            "用途": "公钥加密",
            "使用状态": "[使用中] 实际使用"
        },
        
        "Base64编码": {
            "位置": "第590行",
            "代码": "typeof btoa === lr(334) ? '__' + btoa('@#$%^&') + '__' : '__QCMkJV4m__'",
            "用途": "数据编码",
            "使用状态": "[使用中] 实际使用"
        },
        
        "哈希函数": {
            "位置": "第1046行",
            "代码": "const u = io(t)",
            "用途": "指纹哈希计算",
            "使用状态": "[使用中] 实际使用"
        },
        
        "随机字符串生成": {
            "位置": "第1209行",
            "代码": "const u = Up()",
            "用途": "生成加密IV",
            "使用状态": "[使用中] 实际使用"
        }
    }
    
    for func_name, details in crypto_functions.items():
        print(f"   {func_name}:")
        print(f"     - 位置: {details['位置']}")
        print(f"     - 用途: {details['用途']}")
        print(f"     - 状态: {details['使用状态']}")
        print()
    
    print("3. 冗余代码识别:")
    
    redundant_code = {
        "混淆的字符串数组": {
            "位置": "第1020行",
            "描述": "包含大量混淆的字符串常量",
            "状态": "❌ 冗余代码",
            "原因": "这些是代码混淆产生的字符串表，不是实际的加密逻辑"
        },
        
        "未使用的变量": {
            "位置": "多处",
            "描述": "大量以_0x开头的变量",
            "状态": "❌ 冗余代码", 
            "原因": "这些是混淆器生成的临时变量，实际运行时会被替换"
        },
        
        "调试检测函数": {
            "位置": "第17-206行",
            "描述": "多个反调试检测函数",
            "状态": "⚠️ 部分冗余",
            "原因": "部分检测函数可能不会被调用"
        }
    }
    
    for code_type, details in redundant_code.items():
        print(f"   {code_type}:")
        print(f"     - 位置: {details['位置']}")
        print(f"     - 描述: {details['描述']}")
        print(f"     - 状态: {details['状态']}")
        print(f"     - 原因: {details['原因']}")
        print()
    
    print("4. 核心加密流程:")
    print("   📊 指纹收集 → 🔐 AES加密 → 📤 数据发送")
    print("   📊 指纹收集 → 🔐 RSA加密 → 📤 公钥传输")
    print("   📊 数据编码 → 🔐 Base64 → 📤 网络传输")
    print()
    
    print("5. 建议:")
    print("   ✅ 保留的加密功能:")
    print("      - AES加密/解密 (ui, Qa)")
    print("      - RSA加密 (公钥加密)")
    print("      - Base64编码 (dE)")
    print("      - 哈希计算 (io)")
    print("      - 随机字符串生成 (Up)")
    print()
    print("   ❌ 可以移除的冗余代码:")
    print("      - 混淆字符串数组")
    print("      - 未使用的混淆变量")
    print("      - 部分反调试检测函数")
    print()
    print("   🔧 优化建议:")
    print("      - 去混淆后保留核心加密逻辑")
    print("      - 移除未使用的检测函数")
    print("      - 简化字符串常量表")

if __name__ == "__main__":
    analyze_cookie_tracker()
