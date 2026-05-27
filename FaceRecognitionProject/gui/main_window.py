#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
主窗口界面
"""

import cv2
import numpy as np
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QFileDialog, QMessageBox,
                             QTabWidget, QTextEdit, QGroupBox, QFormLayout,
                             QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap

from core.face_detector import FaceDetector
from core.face_recognizer import FaceRecognizer
from utils.camera_manager import CameraManager


class MainWindow(QMainWindow):
    """主窗口类"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("人脸识别系统 v1.0")
        self.setGeometry(100, 100, 1200, 800)
        
        # 初始化组件
        self.face_detector = FaceDetector()
        self.face_recognizer = FaceRecognizer()
        self.camera_manager = CameraManager()
        
        # UI组件
        self.video_label = None
        self.info_text = None
        self.name_input = None
        self.confidence_label = None
        
        self.setup_ui()
        self.setup_camera()
        
    def setup_ui(self):
        """设置用户界面"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QHBoxLayout(central_widget)
        
        # 左侧视频显示区域
        left_panel = self.create_video_panel()
        main_layout.addWidget(left_panel, 2)
        
        # 右侧面板
        right_panel = self.create_control_panel()
        main_layout.addWidget(right_panel, 1)
        
    def create_video_panel(self):
        """创建视频显示面板"""
        panel = QGroupBox("实时视频")
        layout = QVBoxLayout(panel)
        
        # 视频显示标签
        self.video_label = QLabel()
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setMinimumSize(640, 480)
        self.video_label.setStyleSheet("""
            QLabel {
                background-color: black;
                border: 2px solid #cccccc;
                border-radius: 5px;
            }
        """)
        self.video_label.setText("点击'开始摄像头'启动视频流")
        layout.addWidget(self.video_label)
        
        return panel
        
    def create_control_panel(self):
        """创建控制面板"""
        panel = QTabWidget()
        
        # 识别标签页
        recognition_tab = self.create_recognition_tab()
        panel.addTab(recognition_tab, "人脸识别")
        
        # 训练标签页
        training_tab = self.create_training_tab()
        panel.addTab(training_tab, "模型训练")
        
        # 设置标签页
        settings_tab = self.create_settings_tab()
        panel.addTab(settings_tab, "系统设置")
        
        return panel
        
    def create_recognition_tab(self):
        """创建识别标签页"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # 控制按钮
        button_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("开始摄像头")
        self.start_btn.clicked.connect(self.toggle_camera)
        button_layout.addWidget(self.start_btn)
        
        self.capture_btn = QPushButton("捕获人脸")
        self.capture_btn.clicked.connect(self.capture_face)
        self.capture_btn.setEnabled(False)
        button_layout.addWidget(self.capture_btn)
        
        layout.addLayout(button_layout)
        
        # 识别结果显示
        result_group = QGroupBox("识别结果")
        result_layout = QFormLayout(result_group)
        
        self.name_label = QLabel("未知")
        self.confidence_label = QLabel("0%")
        
        result_layout.addRow("姓名:", self.name_label)
        result_layout.addRow("置信度:", self.confidence_label)
        
        layout.addWidget(result_group)
        
        # 日志显示
        log_group = QGroupBox("系统日志")
        log_layout = QVBoxLayout(log_group)
        
        self.info_text = QTextEdit()
        self.info_text.setMaximumHeight(200)
        self.info_text.setReadOnly(True)
        log_layout.addWidget(self.info_text)
        
        layout.addWidget(log_group)
        
        return tab
        
    def create_training_tab(self):
        """创建训练标签页"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # 添加人脸组
        add_group = QGroupBox("添加新人脸")
        add_layout = QFormLayout(add_group)
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("请输入姓名")
        add_layout.addRow("姓名:", self.name_input)
        
        self.add_face_btn = QPushButton("开始录入")
        self.add_face_btn.clicked.connect(self.start_face_registration)
        add_layout.addRow(self.add_face_btn)
        
        layout.addWidget(add_group)
        
        # 训练按钮
        train_btn = QPushButton("训练模型")
        train_btn.clicked.connect(self.train_model)
        train_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(train_btn)
        
        # 训练状态
        self.training_status = QTextEdit()
        self.training_status.setMaximumHeight(150)
        self.training_status.setReadOnly(True)
        layout.addWidget(self.training_status)
        
        layout.addStretch()
        return tab
        
    def create_settings_tab(self):
        """创建设置标签页"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # 检测设置
        detect_group = QGroupBox("检测参数")
        detect_layout = QFormLayout(detect_group)
        
        self.scale_factor = QDoubleSpinBox()
        self.scale_factor.setRange(1.1, 2.0)
        self.scale_factor.setSingleStep(0.1)
        self.scale_factor.setValue(1.3)
        detect_layout.addRow("缩放因子:", self.scale_factor)
        
        self.min_neighbors = QSpinBox()
        self.min_neighbors.setRange(1, 10)
        self.min_neighbors.setValue(5)
        detect_layout.addRow("最小邻居:", self.min_neighbors)
        
        layout.addWidget(detect_group)
        
        # 摄像头设置
        camera_group = QGroupBox("摄像头设置")
        camera_layout = QFormLayout(camera_group)
        
        self.camera_index = QSpinBox()
        self.camera_index.setRange(0, 5)
        camera_layout.addRow("摄像头索引:", self.camera_index)
        
        self.fps_setting = QSpinBox()
        self.fps_setting.setRange(1, 60)
        self.fps_setting.setValue(30)
        camera_layout.addRow("帧率:", self.fps_setting)
        
        layout.addWidget(camera_group)
        
        # 应用设置按钮
        apply_btn = QPushButton("应用设置")
        apply_btn.clicked.connect(self.apply_settings)
        layout.addWidget(apply_btn)
        
        layout.addStretch()
        return tab
        
    def setup_camera(self):
        """设置摄像头"""
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.current_frame = None
        
    def toggle_camera(self):
        """切换摄像头开关"""
        if not self.camera_manager.is_opened():
            if self.camera_manager.open_camera(self.camera_index.value()):
                self.timer.start(33)  # ~30 FPS
                self.start_btn.setText("停止摄像头")
                self.capture_btn.setEnabled(True)
                self.log_message("摄像头已启动")
            else:
                QMessageBox.critical(self, "错误", "无法打开摄像头")
        else:
            self.stop_camera()
            
    def stop_camera(self):
        """停止摄像头"""
        self.timer.stop()
        self.camera_manager.release()
        self.start_btn.setText("开始摄像头")
        self.capture_btn.setEnabled(False)
        self.video_label.setText("点击'开始摄像头'启动视频流")
        self.log_message("摄像头已停止")
        
    def update_frame(self):
        """更新视频帧"""
        frame = self.camera_manager.read_frame()
        if frame is not None:
            self.current_frame = frame.copy()
            
            # 人脸检测
            faces = self.face_detector.detect_faces(frame)
            
            # 在原图上绘制检测框
            display_frame = frame.copy()
            for (x, y, w, h) in faces:
                cv2.rectangle(display_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                # 如果有训练好的模型，进行识别
                if self.face_recognizer.is_trained():
                    face_roi = frame[y:y+h, x:x+w]
                    name, confidence = self.face_recognizer.predict(face_roi)
                    if name and confidence > 50:  # 置信度阈值
                        cv2.putText(display_frame, f"{name} ({confidence:.1f}%)", 
                                  (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                        self.name_label.setText(name)
                        self.confidence_label.setText(f"{confidence:.1f}%")
            
            # 显示图像
            self.display_image(display_frame)
            
    def display_image(self, frame):
        """在标签上显示图像"""
        # 转换颜色空间
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # 转换为Qt图像
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        
        # 缩放图像以适应标签
        pixmap = QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(self.video_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.video_label.setPixmap(scaled_pixmap)
        
    def capture_face(self):
        """捕获当前帧的人脸"""
        if self.current_frame is not None:
            faces = self.face_detector.detect_faces(self.current_frame)
            if len(faces) > 0:
                # 取第一个检测到的人脸
                x, y, w, h = faces[0]
                face_roi = self.current_frame[y:y+h, x:x+w]
                
                # 保存图像
                filename, _ = QFileDialog.getSaveFileName(
                    self, "保存人脸图像", "", "Images (*.png *.jpg *.bmp)"
                )
                if filename:
                    cv2.imwrite(filename, face_roi)
                    self.log_message(f"人脸图像已保存: {filename}")
            else:
                QMessageBox.warning(self, "警告", "未检测到人脸")
                
    def start_face_registration(self):
        """开始人脸注册流程"""
        name = self.name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "警告", "请输入姓名")
            return
            
        if not self.camera_manager.is_opened():
            QMessageBox.warning(self, "警告", "请先启动摄像头")
            return
            
        self.log_message(f"开始录入 {name} 的人脸数据...")
        self.face_recognizer.register_face(name, self.current_frame)
        self.log_message(f"{name} 的人脸数据录入完成")
        self.name_input.clear()
        
    def train_model(self):
        """训练人脸识别模型"""
        self.training_status.append("开始训练模型...")
        try:
            self.face_recognizer.train()
            self.training_status.append("模型训练完成!")
        except Exception as e:
            self.training_status.append(f"训练失败: {str(e)}")
            
    def apply_settings(self):
        """应用设置"""
        # 更新检测参数
        self.face_detector.scale_factor = self.scale_factor.value()
        self.face_detector.min_neighbors = self.min_neighbors.value()
        
        self.log_message("设置已应用")
        
    def log_message(self, message):
        """记录日志消息"""
        if self.info_text:
            self.info_text.append(message)
            
    def closeEvent(self, event):
        """窗口关闭事件"""
        self.stop_camera()
        event.accept()