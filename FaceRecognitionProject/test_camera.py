#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
摄像头测试脚本
用于测试摄像头连接和基本功能
"""

import cv2
import sys

def test_camera():
    """测试摄像头连接"""
    print("正在测试摄像头连接...")
    
    # 尝试打开摄像头
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ 无法打开摄像头")
        print("请检查:")
        print("1. 摄像头是否连接正常")
        print("2. 是否被其他程序占用")
        print("3. 驱动程序是否正常")
        return False
    
    print("✅ 摄像头连接成功")
    
    # 获取摄像头信息
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    print(f"摄像头分辨率: {width}x{height}")
    print(f"帧率: {fps} FPS")
    
    # 测试读取几帧
    print("正在测试视频流...")
    for i in range(10):
        ret, frame = cap.read()
        if not ret:
            print(f"❌ 第{i+1}帧读取失败")
            break
        print(f"✅ 第{i+1}帧读取成功 - 尺寸: {frame.shape}")
    
    # 释放资源
    cap.release()
    print("✅ 摄像头测试完成")
    return True

def test_opencv():
    """测试OpenCV安装"""
    print("正在测试OpenCV...")
    try:
        print(f"OpenCV版本: {cv2.__version__}")
        
        # 测试人脸识别相关模块
        if hasattr(cv2, 'face'):
            print("✅ OpenCV contrib模块可用")
        else:
            print("⚠️  OpenCV contrib模块不可用，某些功能可能受限")
            
        # 测试Haar级联文件
        cascade_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        classifier = cv2.CascadeClassifier(cascade_file)
        if classifier.empty():
            print("❌ Haar级联文件加载失败")
            return False
        else:
            print("✅ Haar级联文件加载成功")
            
        return True
    except Exception as e:
        print(f"❌ OpenCV测试失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("人脸识别系统 - 环境测试")
    print("=" * 50)
    
    # 测试OpenCV
    if not test_opencv():
        print("\n❌ OpenCV环境存在问题，请检查安装")
        sys.exit(1)
    
    print()
    
    # 测试摄像头
    if not test_camera():
        print("\n❌ 摄像头测试失败")
        sys.exit(1)
    
    print("\n🎉 所有测试通过！系统环境准备就绪")
    print("可以运行 main.py 启动人脸识别系统")

if __name__ == "__main__":
    main()