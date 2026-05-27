#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
人脸识别器
"""

import cv2
import numpy as np
import os
import pickle
from typing import List, Tuple, Optional


class FaceRecognizer:
    """人脸识别类"""
    
    def __init__(self, data_dir="face_data"):
        self.data_dir = data_dir
        self.model = cv2.face.LBPHFaceRecognizer_create()
        self.face_samples = []
        self.labels = []
        self.label_names = {}
        self.trained = False
        
        # 创建数据目录
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            
        # 加载已有的模型和数据
        self.load_model()
        
    def register_face(self, name: str, image):
        """
        注册新人脸
        
        Args:
            name: 人员姓名
            image: 包含人脸的图像
        """
        # 创建个人目录
        person_dir = os.path.join(self.data_dir, name)
        if not os.path.exists(person_dir):
            os.makedirs(person_dir)
            
        # 检测人脸
        detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) == 0:
            raise ValueError("未检测到人脸")
            
        # 保存多张不同角度的人脸图片
        for i, (x, y, w, h) in enumerate(faces[:5]):  # 最多保存5张
            face_roi = gray[y:y+h, x:x+w]
            # 调整大小
            face_roi = cv2.resize(face_roi, (200, 200))
            # 保存图像
            filename = os.path.join(person_dir, f"face_{i}.jpg")
            cv2.imwrite(filename, face_roi)
            
    def collect_training_data(self):
        """收集训练数据"""
        self.face_samples = []
        self.labels = []
        self.label_names = {}
        
        label_id = 0
        
        # 遍历所有人的目录
        for person_name in os.listdir(self.data_dir):
            person_dir = os.path.join(self.data_dir, person_name)
            if not os.path.isdir(person_dir):
                continue
                
            self.label_names[label_id] = person_name
            
            # 读取该人所有的人脸图像
            for filename in os.listdir(person_dir):
                if filename.endswith(('.jpg', '.png', '.jpeg')):
                    filepath = os.path.join(person_dir, filename)
                    image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
                    
                    if image is not None:
                        self.face_samples.append(image)
                        self.labels.append(label_id)
                        
            label_id += 1
            
    def train(self):
        """训练人脸识别模型"""
        if not os.path.exists(self.data_dir) or not os.listdir(self.data_dir):
            raise ValueError("没有找到训练数据，请先添加人脸数据")
            
        self.collect_training_data()
        
        if len(self.face_samples) == 0:
            raise ValueError("没有有效的训练样本")
            
        # 转换为numpy数组
        faces_array = np.array(self.face_samples)
        labels_array = np.array(self.labels)
        
        # 训练模型
        self.model.train(faces_array, labels_array)
        self.trained = True
        
        # 保存模型和标签映射
        self.save_model()
        
    def predict(self, face_image) -> Tuple[Optional[str], float]:
        """
        预测人脸身份
        
        Args:
            face_image: 人脸图像
            
        Returns:
            (姓名, 置信度)
        """
        if not self.trained:
            return None, 0.0
            
        # 预处理图像
        if len(face_image.shape) == 3:
            gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
        else:
            gray = face_image
            
        # 调整大小
        gray = cv2.resize(gray, (200, 200))
        
        # 预测
        label, confidence = self.model.predict(gray)
        
        # 将置信度转换为百分比 (LBPH返回的距离值，越小越好)
        confidence_percent = max(0, 100 - confidence)
        
        # 获取姓名
        name = self.label_names.get(label, "未知")
        
        return name, confidence_percent
        
    def save_model(self):
        """保存模型和数据"""
        # 保存模型
        model_path = os.path.join(self.data_dir, "face_model.yml")
        self.model.save(model_path)
        
        # 保存标签映射
        labels_path = os.path.join(self.data_dir, "labels.pkl")
        with open(labels_path, 'wb') as f:
            pickle.dump(self.label_names, f)
            
    def load_model(self):
        """加载模型和数据"""
        model_path = os.path.join(self.data_dir, "face_model.yml")
        labels_path = os.path.join(self.data_dir, "labels.pkl")
        
        if os.path.exists(model_path) and os.path.exists(labels_path):
            try:
                self.model.read(model_path)
                with open(labels_path, 'rb') as f:
                    self.label_names = pickle.load(f)
                self.trained = True
            except Exception as e:
                print(f"加载模型失败: {e}")
                
    def is_trained(self) -> bool:
        """检查模型是否已训练"""
        return self.trained
        
    def get_registered_names(self) -> List[str]:
        """获取已注册的姓名列表"""
        return list(self.label_names.values())
        
    def delete_person(self, name: str) -> bool:
        """
        删除指定人员的数据
        
        Args:
            name: 要删除的人员姓名
            
        Returns:
            是否删除成功
        """
        person_dir = os.path.join(self.data_dir, name)
        if os.path.exists(person_dir):
            import shutil
            shutil.rmtree(person_dir)
            return True
        return False