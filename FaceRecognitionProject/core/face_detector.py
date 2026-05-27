#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
人脸检测器
"""

import cv2
import numpy as np
import os


class FaceDetector:
    """人脸检测类"""
    
    def __init__(self):
        self.scale_factor = 1.3
        self.min_neighbors = 5
        self.min_size = (30, 30)
        
        # 加载Haar级联分类器
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        if os.path.exists(cascade_path):
            self.face_cascade = cv2.CascadeClassifier(cascade_path)
        else:
            raise FileNotFoundError("找不到Haar级联文件")
            
    def detect_faces(self, image):
        """
        检测图像中的人脸
        
        Args:
            image: 输入图像(BGR格式)
            
        Returns:
            faces: 人脸矩形列表 [(x, y, w, h), ...]
        """
        # 转换为灰度图
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # 直方图均衡化增强对比度
        gray = cv2.equalizeHist(gray)
        
        # 检测人脸
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=self.scale_factor,
            minNeighbors=self.min_neighbors,
            minSize=self.min_size,
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        return faces
        
    def detect_faces_with_eyes(self, image):
        """
        检测带眼睛验证的人脸
        
        Args:
            image: 输入图像
            
        Returns:
            verified_faces: 经过眼睛验证的人脸列表
        """
        faces = self.detect_faces(image)
        verified_faces = []
        
        # 加载眼睛检测器
        eye_cascade_path = cv2.data.haarcascades + 'haarcascade_eye.xml'
        eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        for (x, y, w, h) in faces:
            # 在人脸区域内检测眼睛
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            
            # 如果检测到至少一只眼睛，则认为是有效人脸
            if len(eyes) >= 1:
                verified_faces.append((x, y, w, h))
                
        return verified_faces
        
    def draw_faces(self, image, faces, color=(0, 255, 0), thickness=2):
        """
        在图像上绘制人脸框
        
        Args:
            image: 输入图像
            faces: 人脸矩形列表
            color: 边框颜色
            thickness: 边框粗细
            
        Returns:
            带有人脸框的图像
        """
        result = image.copy()
        for (x, y, w, h) in faces:
            cv2.rectangle(result, (x, y), (x+w, y+h), color, thickness)
        return result
        
    def extract_faces(self, image, faces):
        """
        提取人脸区域
        
        Args:
            image: 输入图像
            faces: 人脸矩形列表
            
        Returns:
            face_images: 人脸图像列表
        """
        face_images = []
        for (x, y, w, h) in faces:
            face_img = image[y:y+h, x:x+w]
            face_images.append(face_img)
        return face_images
        
    def preprocess_face(self, face_image, size=(200, 200)):
        """
        预处理人脸图像
        
        Args:
            face_image: 人脸图像
            size: 目标尺寸
            
        Returns:
            processed_face: 处理后的人脸图像
        """
        # 调整大小
        resized = cv2.resize(face_image, size)
        
        # 转换为灰度图
        if len(resized.shape) == 3:
            gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        else:
            gray = resized
            
        # 直方图均衡化
        equalized = cv2.equalizeHist(gray)
        
        return equalized