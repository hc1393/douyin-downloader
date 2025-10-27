import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QFileDialog, QSpinBox, QGroupBox,
                             QComboBox, QTextEdit, QSplitter, QMessageBox)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import os
from advanced_slider_solver import AdvancedSliderSolver

class SliderSolverGUI(QMainWindow):
    """
    滑块验证码识别图形界面
    """
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("滑块验证码识别工具")
        self.setGeometry(100, 100, 1200, 800)
        
        # 初始化求解器
        self.solver = AdvancedSliderSolver()
        
        # 初始化UI
        self.init_ui()
        
        # 存储图像数据
        self.background_image = None
        self.background_path = None
        
    def init_ui(self):
        """
        初始化用户界面
        """
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建主布局
        main_layout = QHBoxLayout(central_widget)
        
        # 左侧控制面板
        control_panel = self.create_control_panel()
        main_layout.addWidget(control_panel, 1)
        
        # 右侧图像显示区域
        image_display = self.create_image_display()
        main_layout.addWidget(image_display, 3)
        
    def create_control_panel(self):
        """
        创建控制面板
        """
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # 文件操作组
        file_group = QGroupBox("文件操作")
        file_layout = QVBoxLayout(file_group)
        
        self.load_btn = QPushButton("加载背景图像")
        self.load_btn.clicked.connect(self.load_background_image)
        file_layout.addWidget(self.load_btn)
        
        self.bg_path_label = QLabel("未选择图像文件")
        self.bg_path_label.setWordWrap(True)
        file_layout.addWidget(self.bg_path_label)
        
        layout.addWidget(file_group)
        
        # 参数设置组
        param_group = QGroupBox("参数设置")
        param_layout = QVBoxLayout(param_group)
        
        # 检测方法选择
        method_layout = QHBoxLayout()
        method_layout.addWidget(QLabel("检测方法:"))
        self.method_combo = QComboBox()
        self.method_combo.addItems(["特征分析", "模板匹配"])
        self.method_combo.setCurrentText("特征分析")
        method_layout.addWidget(self.method_combo)
        param_layout.addLayout(method_layout)
        
        # 最小面积设置
        min_area_layout = QHBoxLayout()
        min_area_layout.addWidget(QLabel("最小面积:"))
        self.min_area_spin = QSpinBox()
        self.min_area_spin.setRange(10, 1000)
        self.min_area_spin.setValue(50)
        min_area_layout.addWidget(self.min_area_spin)
        param_layout.addLayout(min_area_layout)
        
        # 最大面积设置
        max_area_layout = QHBoxLayout()
        max_area_layout.addWidget(QLabel("最大面积:"))
        self.max_area_spin = QSpinBox()
        self.max_area_spin.setRange(100, 10000)
        self.max_area_spin.setValue(2000)
        max_area_layout.addWidget(self.max_area_spin)
        param_layout.addLayout(max_area_layout)
        
        layout.addWidget(param_group)
        
        # 操作按钮组
        action_group = QGroupBox("操作")
        action_layout = QVBoxLayout(action_group)
        
        self.detect_btn = QPushButton("检测滑块距离")
        self.detect_btn.clicked.connect(self.detect_slider_distance)
        self.detect_btn.setEnabled(False)
        action_layout.addWidget(self.detect_btn)
        
        self.clear_btn = QPushButton("清空结果")
        self.clear_btn.clicked.connect(self.clear_results)
        action_layout.addWidget(self.clear_btn)
        
        layout.addWidget(action_group)
        
        # 结果显示组
        result_group = QGroupBox("识别结果")
        result_layout = QVBoxLayout(result_group)
        
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setMaximumHeight(150)
        result_layout.addWidget(self.result_text)
        
        layout.addWidget(result_group)
        
        # 添加伸展因子
        layout.addStretch()
        
        return panel
    
    def create_image_display(self):
        """
        创建图像显示区域
        """
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # 创建分割器
        splitter = QSplitter(Qt.Vertical)
        
        # 原始图像显示
        self.original_image_label = QLabel("原始图像")
        self.original_image_label.setAlignment(Qt.AlignCenter)
        self.original_image_label.setMinimumHeight(200)
        self.original_image_label.setStyleSheet("background-color: #f0f0f0;")
        splitter.addWidget(self.original_image_label)
        
        # 处理后图像显示
        self.processed_image_label = QLabel("处理结果")
        self.processed_image_label.setAlignment(Qt.AlignCenter)
        self.processed_image_label.setMinimumHeight(200)
        self.processed_image_label.setStyleSheet("background-color: #f0f0f0;")
        splitter.addWidget(self.processed_image_label)
        
        layout.addWidget(splitter)
        
        return widget
    
    def load_background_image(self):
        """
        加载背景图像
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择背景图像", "", "图像文件 (*.png *.jpg *.jpeg *.bmp *.tiff)"
        )
        
        if file_path:
            try:
                # 检查文件是否存在
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"图像文件不存在: {file_path}")
                
                # 读取图像
                self.background_image = cv2.imread(file_path)
                if self.background_image is None:
                    raise Exception(f"无法读取图像文件: {file_path}，请检查文件格式是否正确")
                
                self.background_path = file_path
                self.bg_path_label.setText(file_path)
                
                # 显示原始图像
                self.display_image(self.background_image, self.original_image_label)
                
                # 启用检测按钮
                self.detect_btn.setEnabled(True)
                
                self.result_text.append(f"已加载图像: {file_path}")
                
            except Exception as e:
                QMessageBox.critical(self, "错误", f"加载图像失败: {str(e)}")
    
    def display_image(self, image, label):
        """
        在标签中显示图像
        :param image: OpenCV图像
        :param label: QLabel控件
        """
        if image is None:
            return
        
        # 转换颜色空间
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # 创建QImage
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        q_img = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        
        # 缩放图像以适应标签
        pixmap = QPixmap.fromImage(q_img)
        label.setPixmap(pixmap.scaled(
            label.width(), label.height(), 
            Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))
    
    def detect_slider_distance(self):
        """
        检测滑块距离
        """
        if self.background_image is None or self.background_path is None:
            QMessageBox.warning(self, "警告", "请先加载背景图像")
            return
        
        # 检查文件是否存在
        if not os.path.exists(self.background_path):
            QMessageBox.critical(self, "错误", f"背景图像文件不存在: {self.background_path}")
            return
        
        try:
            # 获取参数
            method = "feature" if self.method_combo.currentText() == "特征分析" else "template"
            min_area = self.min_area_spin.value()
            max_area = self.max_area_spin.value()
            
            # 记录开始检测
            self.result_text.append("开始检测滑块距离...")
            
            # 执行检测
            distance, info = self.solver.calculate_slider_distance(
                self.background_path, method=method
            )
            
            # 添加距离信息到结果
            info['distance'] = distance
            
            # 显示结果
            self.show_detection_result(distance, info)
            
            # 显示处理后的图像
            self.show_processed_image(distance, info)
            
        except Exception as e:
            QMessageBox.critical(self, "错误", f"检测过程中发生错误: {str(e)}")
            self.result_text.append(f"检测失败: {str(e)}")
    
    def show_detection_result(self, distance, info):
        """
        显示检测结果
        """
        method = info.get('method', 'unknown')
        score = info.get('score', 0)
        
        result_text = f"""
检测完成:
- 检测方法: {method}
- 滑块需要移动的距离: {distance} 像素
- 置信度分数: {score:.2f}
"""
        
        if 'gap_position' in info:
            gap_pos = info['gap_position']
            result_text += f"- 缺口位置: ({gap_pos[0]}, {gap_pos[1]})\n"
        
        if 'slider_position' in info:
            slider_pos = info['slider_position']
            result_text += f"- 滑块位置: ({slider_pos[0]}, {slider_pos[1]})\n"
        
        self.result_text.append(result_text.strip())
    
    def show_processed_image(self, distance, info):
        """
        显示处理后的图像
        """
        if self.background_image is None:
            return
        
        # 检查文件是否存在
        if not os.path.exists(self.background_path):
            QMessageBox.critical(self, "错误", f"背景图像文件不存在: {self.background_path}")
            return
        
        # 复制原始图像
        processed_img = self.background_image.copy()
        
        # 根据不同方法绘制结果
        method = info.get('method', 'default')
        
        if method in ['feature', 'feature_only_gap']:
            # 绘制特征分析结果
            gap_pos = info.get('gap_position')
            slider_pos = info.get('slider_position')
            
            if gap_pos:
                # 绘制缺口位置
                cv2.circle(processed_img, gap_pos, 15, (0, 0, 255), 3)
                cv2.putText(processed_img, f'Gap: {gap_pos}', (15, 40), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            if slider_pos:
                # 绘制滑块位置
                cv2.circle(processed_img, slider_pos, 15, (0, 255, 0), 3)
                cv2.putText(processed_img, f'Slider: {slider_pos}', (15, 80), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # 显示距离信息
        cv2.putText(processed_img, f'Distance: {distance}px', (15, 120), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
        # 显示处理后的图像
        self.display_image(processed_img, self.processed_image_label)
    
    def clear_results(self):
        """
        清空结果
        """
        self.result_text.clear()
        self.processed_image_label.clear()
        self.processed_image_label.setText("处理结果")

def main():
    """
    主函数
    """
    app = QApplication(sys.argv)
    window = SliderSolverGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()