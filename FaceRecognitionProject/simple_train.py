#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化的人脸识别训练脚本
"""

import cv2
import numpy as np
import os
import pickle

def create_simple_dataset():
    """创建简单的人脸数据集"""
    print("创建简单人脸数据集...")
    
    # 确保目录存在
    dataset_dir = "simple_dataset"
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)
    
    people = ["Alice", "Bob", "Charlie"]
    
    face_samples = []
    labels = []
    label_names = {}
    
    for label_id, person_name in enumerate(people):
        label_names[label_id] = person_name
        person_dir = os.path.join(dataset_dir, person_name)
        if not os.path.exists(person_dir):
            os.makedirs(person_dir)
        
        print(f"创建 {person_name} 的数据...")
        
        # 为每个人创建10个样本
        for i in range(10):
            # 创建简单的人脸图像
            face_img = create_simple_face(person_name, i)
            
            # 保存图像
            filename = f"face_{i}.jpg"
            filepath = os.path.join(person_dir, filename)
            
            # 直接保存彩色图像
            success = cv2.imwrite(filepath, face_img)
            if success:
                print(f"  保存: {filename}")
                # 转换为灰度图用于训练
                gray_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
                face_samples.append(gray_img)
                labels.append(label_id)
            else:
                print(f"  ❌ 保存失败: {filename}")
    
    # 保存训练数据
    train_data = {
        'faces': face_samples,
        'labels': labels,
        'label_names': label_names
    }
    
    with open(os.path.join(dataset_dir, 'train_data.pkl'), 'wb') as f:
        pickle.dump(train_data, f)
    
    print(f"✅ 数据集创建完成，共 {len(face_samples)} 个样本")
    return train_data

def create_simple_face(name, index):
    """创建简单的人脸图像"""
    # 创建200x200的彩色图像
    img = np.zeros((200, 200, 3), dtype=np.uint8)
    
    # 基于姓名和索引生成不同的颜色
    base_hue = (hash(name) % 360)
    variation = (index * 30) % 100
    
    # 背景色
    bg_color = ((base_hue + variation) % 180 + 50, 50, 200)
    img[:] = bg_color
    
    # 脸部（圆形）
    center = (100, 100)
    radius = 70
    face_color = (100 + variation, 150 + variation//2, 200)
    cv2.circle(img, center, radius, face_color, -1)
    
    # 眼睛
    eye_y = 85
    eye_radius = 10
    eye_color = (255, 255, 255)
    cv2.circle(img, (80, eye_y), eye_radius, eye_color, -1)  # 左眼
    cv2.circle(img, (120, eye_y), eye_radius, eye_color, -1)  # 右眼
    
    # 瞳孔
    pupil_radius = 4
    pupil_color = (0, 0, 0)
    cv2.circle(img, (80, eye_y), pupil_radius, pupil_color, -1)
    cv2.circle(img, (120, eye_y), pupil_radius, pupil_color, -1)
    
    # 鼻子
    nose_points = np.array([[100, 110], [95, 130], [105, 130]], np.int32)
    cv2.fillPoly(img, [nose_points], (150, 100, 50))
    
    # 嘴巴
    mouth_center = (100, 150)
    mouth_axes = (25, 12)
    cv2.ellipse(img, mouth_center, mouth_axes, 0, 0, 180, (50, 50, 100), 2)
    
    return img

def train_simple_model():
    """训练简化模型"""
    print("\n训练简化人脸识别模型...")
    
    # 加载数据
    dataset_dir = "simple_dataset"
    data_file = os.path.join(dataset_dir, 'train_data.pkl')
    
    if not os.path.exists(data_file):
        print("❌ 训练数据不存在，请先创建数据集")
        return False
    
    with open(data_file, 'rb') as f:
        train_data = pickle.load(f)
    
    face_samples = train_data['faces']
    labels = train_data['labels']
    label_names = train_data['label_names']
    
    print(f"加载了 {len(face_samples)} 个训练样本")
    print(f"标签映射: {label_names}")
    
    # 转换为numpy数组
    faces_array = np.array(face_samples)
    labels_array = np.array(labels)
    
    # 创建并训练LBPH模型
    try:
        model = cv2.face.LBPHFaceRecognizer_create()
        model.train(faces_array, labels_array)
        
        # 保存模型
        model.save(os.path.join(dataset_dir, 'face_model.yml'))
        
        # 保存标签映射
        with open(os.path.join(dataset_dir, 'labels.pkl'), 'wb') as f:
            pickle.dump(label_names, f)
        
        print("✅ 模型训练完成并已保存")
        return True
        
    except Exception as e:
        print(f"❌ 训练失败: {e}")
        return False

def test_simple_model():
    """测试简化模型"""
    print("\n测试模型识别能力...")
    
    dataset_dir = "simple_dataset"
    model_path = os.path.join(dataset_dir, 'face_model.yml')
    labels_path = os.path.join(dataset_dir, 'labels.pkl')
    
    if not os.path.exists(model_path) or not os.path.exists(labels_path):
        print("❌ 模型文件不存在")
        return
    
    # 加载模型
    model = cv2.face.LBPHFaceRecognizer_create()
    model.read(model_path)
    
    with open(labels_path, 'rb') as f:
        label_names = pickle.load(f)
    
    # 创建测试图像
    test_img = create_simple_face("Alice", 5)  # 使用训练集中的人物
    test_gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    
    # 预测
    label, confidence = model.predict(test_gray)
    predicted_name = label_names.get(label, "未知")
    
    print(f"测试图像识别结果:")
    print(f"  预测姓名: {predicted_name}")
    print(f"  置信度: {confidence}")
    print(f"  标签ID: {label}")

def main():
    """主函数"""
    print("简化人脸识别训练系统")
    print("=" * 30)
    
    # 创建数据集
    train_data = create_simple_dataset()
    
    # 训练模型
    if train_simple_model():
        # 测试模型
        test_simple_model()
        print("\n🎉 训练完成！")
    else:
        print("\n❌ 训练失败")

if __name__ == "__main__":
    main()