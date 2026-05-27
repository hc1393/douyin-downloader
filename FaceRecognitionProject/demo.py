#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
人脸识别系统演示脚本
展示基本功能使用方法
"""

import cv2
import numpy as np
import os
from core.face_detector import FaceDetector
from core.face_recognizer import FaceRecognizer


def demo_face_detection():
    """演示人脸检测功能"""
    print("=== 人脸检测演示 ===")
    
    # 创建检测器
    detector = FaceDetector()
    
    # 读取测试图像（如果没有摄像头）
    test_image_path = "test_image.jpg"
    if os.path.exists(test_image_path):
        image = cv2.imread(test_image_path)
    else:
        # 创建一个简单的人脸测试图像
        image = create_test_face_image()
    
    # 检测人脸
    faces = detector.detect_faces(image)
    print(f"检测到 {len(faces)} 个人脸")
    
    # 在图像上绘制检测框
    result_image = detector.draw_faces(image, faces)
    
    # 显示结果
    cv2.imshow("人脸检测结果", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def create_test_face_image():
    """创建测试人脸图像"""
    # 创建黑色背景
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    
    # 绘制简单的人脸轮廓
    # 脸部（椭圆）
    cv2.ellipse(img, (320, 200), (80, 100), 0, 0, 360, (100, 100, 100), -1)
    
    # 眼睛
    cv2.circle(img, (290, 180), 10, (255, 255, 255), -1)
    cv2.circle(img, (350, 180), 10, (255, 255, 255), -1)
    
    # 鼻子
    cv2.line(img, (320, 200), (320, 230), (150, 150, 150), 3)
    
    # 嘴巴
    cv2.ellipse(img, (320, 250), (20, 10), 0, 0, 180, (150, 150, 150), 2)
    
    return img


def demo_face_recognition():
    """演示人脸识别功能"""
    print("=== 人脸识别演示 ===")
    
    # 创建识别器
    recognizer = FaceRecognizer()
    
    try:
        # 检查是否有训练数据
        if not recognizer.is_trained():
            print("没有训练好的模型，跳过识别演示")
            print("请先运行主程序添加人脸数据并训练模型")
            return
            
        # 获取已注册的姓名
        names = recognizer.get_registered_names()
        print(f"已注册人员: {names}")
        
        # 演示预测（使用测试图像）
        test_image = create_test_face_image()
        name, confidence = recognizer.predict(test_image)
        print(f"识别结果: {name} (置信度: {confidence:.1f}%)")
        
    except Exception as e:
        print(f"识别演示出错: {e}")


def demo_camera_capture():
    """演示摄像头捕获功能"""
    print("=== 摄像头演示 ===")
    
    try:
        # 导入摄像头管理器
        from utils.camera_manager import CameraManager
        
        camera = CameraManager()
        
        if camera.open_camera():
            print("摄像头打开成功")
            print(f"分辨率: {camera.get_resolution()}")
            
            # 捕获几帧
            for i in range(5):
                frame = camera.read_frame()
                if frame is not None:
                    print(f"第{i+1}帧捕获成功")
                    # 可以在这里处理帧数据
                    
            camera.release()
            print("摄像头演示完成")
        else:
            print("无法打开摄像头")
            
    except ImportError:
        print("摄像头管理器导入失败")
    except Exception as e:
        print(f"摄像头演示出错: {e}")


def main():
    """主演示函数"""
    print("人脸识别系统功能演示")
    print("=" * 30)
    
    while True:
        print("\n请选择演示功能:")
        print("1. 人脸检测演示")
        print("2. 人脸识别演示")
        print("3. 摄像头演示")
        print("4. 全部演示")
        print("0. 退出")
        
        choice = input("请输入选择 (0-4): ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            demo_face_detection()
        elif choice == '2':
            demo_face_recognition()
        elif choice == '3':
            demo_camera_capture()
        elif choice == '4':
            demo_face_detection()
            demo_face_recognition()
            demo_camera_capture()
        else:
            print("无效选择，请重新输入")
    
    print("演示结束")


if __name__ == "__main__":
    main()