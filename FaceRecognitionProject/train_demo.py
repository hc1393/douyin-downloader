#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模型训练演示脚本
创建测试数据并训练人脸识别模型
"""

import cv2
import numpy as np
import os
from core.face_recognizer import FaceRecognizer
from core.face_detector import FaceDetector

def create_synthetic_face_data():
    """创建合成的人脸测试数据"""
    print("正在创建合成人脸数据...")
    
    # 创建测试人员目录
    test_people = ["张三", "李四", "王五"]
    
    detector = FaceDetector()
    
    for person_name in test_people:
        person_dir = os.path.join("face_data", person_name)
        if not os.path.exists(person_dir):
            os.makedirs(person_dir)
        
        print(f"创建 {person_name} 的人脸数据...")
        
        # 为每个人创建5张不同的人脸图片
        for i in range(5):
            # 创建基础人脸图像
            face_img = create_synthetic_face(person_name, i)
            
            # 预处理
            processed_face = detector.preprocess_face(face_img)
            
            # 保存
            filename = f"face_{i}.jpg"
            filepath = os.path.join(person_dir, filename)
            success = cv2.imwrite(filepath, processed_face)
            if success:
                print(f"  保存: {filename}")
            else:
                print(f"  ❌ 保存失败: {filename}")
    
    print("✅ 合成人脸数据创建完成")

def create_synthetic_face(name, index):
    """创建合成的人脸图像"""
    # 创建画布
    img = np.ones((200, 200, 3), dtype=np.uint8) * 100  # 灰色背景
    
    # 根据姓名和索引创建不同的特征
    base_color = hash(name) % 100 + 100  # 基础肤色
    variation = index * 20  # 每张图片的变化
    
    # 脸部椭圆
    center_x, center_y = 100, 100
    axes = (70, 90)
    
    # 不同的肤色
    face_color = (base_color + variation, base_color + variation - 10, base_color + variation - 20)
    cv2.ellipse(img, (center_x, center_y), axes, 0, 0, 360, face_color, -1)
    
    # 眼睛（根据索引调整位置）
    eye_offset = index * 2 - 5
    cv2.circle(img, (80 + eye_offset, 85), 8, (255, 255, 255), -1)  # 左眼
    cv2.circle(img, (120 - eye_offset, 85), 8, (255, 255, 255), -1)  # 右眼
    cv2.circle(img, (80 + eye_offset, 85), 3, (0, 0, 0), -1)  # 瞳孔
    cv2.circle(img, (120 - eye_offset, 85), 3, (0, 0, 0), -1)  # 瞳孔
    
    # 鼻子
    nose_x = 100 + (index % 3 - 1) * 3
    cv2.line(img, (nose_x, 100), (nose_x, 120), (base_color-30, base_color-40, base_color-50), 2)
    
    # 嘴巴（根据索引调整形状）
    mouth_width = 25 + (index % 3) * 5
    if index % 2 == 0:
        # 微笑
        cv2.ellipse(img, (100, 140), (mouth_width, 10), 0, 0, 180, (base_color-50, base_color-60, base_color-70), 2)
    else:
        # 平直
        cv2.line(img, (100-mouth_width, 140), (100+mouth_width, 140), (base_color-50, base_color-60, base_color-70), 2)
    
    # 添加一些随机噪声增加多样性
    noise = np.random.randint(-10, 10, img.shape, dtype=np.int16)
    img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    
    return img

def train_model():
    """训练人脸识别模型"""
    print("\n开始训练人脸识别模型...")
    
    try:
        # 创建识别器
        recognizer = FaceRecognizer()
        
        # 训练模型
        recognizer.train()
        
        print("✅ 模型训练完成!")
        
        # 显示注册的人员
        names = recognizer.get_registered_names()
        print(f"已注册人员: {names}")
        
        return True
        
    except Exception as e:
        print(f"❌ 训练失败: {e}")
        return False

def test_recognition():
    """测试识别功能"""
    print("\n测试人脸识别功能...")
    
    try:
        recognizer = FaceRecognizer()
        
        if not recognizer.is_trained():
            print("模型未训练，请先训练模型")
            return
            
        # 创建测试图像
        test_img = create_synthetic_face("张三", 0)
        
        # 进行识别
        name, confidence = recognizer.predict(test_img)
        print(f"识别结果: {name} (置信度: {confidence:.1f}%)")
        
        # 测试其他人员
        test_img2 = create_synthetic_face("李四", 2)
        name2, confidence2 = recognizer.predict(test_img2)
        print(f"识别结果: {name2} (置信度: {confidence2:.1f}%)")
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")

def main():
    """主函数"""
    print("人脸识别模型训练演示")
    print("=" * 30)
    
    # 创建测试数据
    create_synthetic_face_data()
    
    # 训练模型
    if train_model():
        # 测试识别
        test_recognition()
        
        print("\n🎉 训练和测试完成!")
        print("现在可以在主程序中使用人脸识别功能了")
    else:
        print("\n❌ 训练失败，请检查错误信息")

if __name__ == "__main__":
    main()