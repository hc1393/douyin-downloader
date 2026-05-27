#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
摄像头管理器
"""

import cv2
import numpy as np
from typing import Optional


class CameraManager:
    """摄像头管理类"""
    
    def __init__(self):
        self.cap = None
        self.is_open = False
        
    def open_camera(self, camera_index: int = 0) -> bool:
        """
        打开摄像头
        
        Args:
            camera_index: 摄像头索引
            
        Returns:
            是否成功打开
        """
        try:
            self.cap = cv2.VideoCapture(camera_index)
            if self.cap.isOpened():
                # 设置摄像头参数
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                self.cap.set(cv2.CAP_PROP_FPS, 30)
                self.is_open = True
                return True
            else:
                return False
        except Exception as e:
            print(f"打开摄像头失败: {e}")
            return False
            
    def read_frame(self) -> Optional[np.ndarray]:
        """
        读取一帧图像
        
        Returns:
            图像帧，如果失败返回None
        """
        if not self.is_open or self.cap is None:
            return None
            
        try:
            ret, frame = self.cap.read()
            if ret:
                return frame
            else:
                return None
        except Exception as e:
            print(f"读取帧失败: {e}")
            return None
            
    def is_opened(self) -> bool:
        """检查摄像头是否已打开"""
        return self.is_open and self.cap is not None and self.cap.isOpened()
        
    def release(self):
        """释放摄像头资源"""
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        self.is_open = False
        
    def set_resolution(self, width: int, height: int):
        """设置分辨率"""
        if self.cap is not None:
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
            
    def set_fps(self, fps: int):
        """设置帧率"""
        if self.cap is not None:
            self.cap.set(cv2.CAP_PROP_FPS, fps)
            
    def get_resolution(self) -> tuple:
        """获取当前分辨率"""
        if self.cap is not None:
            width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            return (width, height)
        return (0, 0)
        
    def __del__(self):
        """析构函数"""
        self.release()