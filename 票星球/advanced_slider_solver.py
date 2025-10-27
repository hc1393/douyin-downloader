import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import os

class AdvancedSliderSolver:
    """
    高级滑块验证码识别类
    使用多种图像处理技术提高识别准确率
    """
    
    def __init__(self):
        pass
    
    def detect_contour_center(self, contour):
        """
        计算轮廓的中心点
        :param contour: 轮廓点集
        :return: 中心点坐标 (x, y)
        """
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            return cx, cy
        return 0, 0
    
    def preprocess_image(self, image_path, method='canny'):
        """
        图像预处理
        :param image_path: 图像路径
        :param method: 边缘检测方法 ('canny', 'sobel', 'laplacian')
        :return: 处理后的图像
        """
        # 检查文件是否存在
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"图像文件不存在: {image_path}")
        
        # 读取图像
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"无法读取图像文件: {image_path}，请检查文件格式是否正确")
        
        # 转换为灰度图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # 高斯模糊
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # 根据选择的方法进行边缘检测
        if method == 'canny':
            edges = cv2.Canny(blurred, 50, 150)
        elif method == 'sobel':
            sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
            edges = np.sqrt(sobelx**2 + sobely**2)
            edges = np.uint8(edges)
        elif method == 'laplacian':
            edges = cv2.Laplacian(blurred, cv2.CV_64F)
            edges = np.uint8(np.absolute(edges))
        else:
            edges = cv2.Canny(blurred, 50, 150)
        
        return img, gray, edges
    
    def find_contours_with_feature(self, edges, min_area=100, max_area=5000, 
                                   aspect_ratio_range=(0.2, 5.0)):
        """
        根据特征查找轮廓
        :param edges: 边缘图像
        :param min_area: 最小面积
        :param max_area: 最大面积
        :param aspect_ratio_range: 宽高比范围
        :return: 符合条件的轮廓列表
        """
        # 查找轮廓
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # 筛选符合条件的轮廓
        filtered_contours = []
        for contour in contours:
            # 计算轮廓面积
            area = cv2.contourArea(contour)
            
            # 面积筛选
            if area < min_area or area > max_area:
                continue
            
            # 计算边界框
            x, y, w, h = cv2.boundingRect(contour)
            
            # 宽高比筛选
            aspect_ratio = float(w) / h if h != 0 else 0
            if aspect_ratio < aspect_ratio_range[0] or aspect_ratio > aspect_ratio_range[1]:
                continue
            
            filtered_contours.append((contour, (x, y, w, h), area))
        
        # 按面积排序
        filtered_contours.sort(key=lambda x: x[2], reverse=True)
        
        return filtered_contours
    
    def detect_gap_by_template_matching(self, background_path, template_path):
        """
        通过模板匹配检测缺口
        :param background_path: 背景图像路径
        :param template_path: 缺口模板图像路径
        :return: 缺口位置
        """
        # 检查文件是否存在
        if not os.path.exists(background_path):
            raise FileNotFoundError(f"背景图像文件不存在: {background_path}")
        
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"模板图像文件不存在: {template_path}")
        
        # 读取图像
        background = cv2.imread(background_path, 0)
        template = cv2.imread(template_path, 0)
        
        if background is None:
            raise FileNotFoundError(f"无法读取背景图像文件: {background_path}，请检查文件格式是否正确")
        
        if template is None:
            raise FileNotFoundError(f"无法读取模板图像文件: {template_path}，请检查文件格式是否正确")
        
        # 模板匹配
        res = cv2.matchTemplate(background, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        # 获取匹配位置
        top_left = max_loc
        h, w = template.shape[:2]
        bottom_right = (top_left[0] + w, top_left[1] + h)
        
        return top_left, bottom_right, max_val
    
    def detect_gap_by_feature_analysis(self, background_path):
        """
        通过特征分析检测缺口
        :param background_path: 背景图像路径
        :return: 缺口位置
        """
        # 检查文件是否存在
        if not os.path.exists(background_path):
            raise FileNotFoundError(f"背景图像文件不存在: {background_path}")
        
        # 图像预处理
        img, gray, edges = self.preprocess_image(background_path, method='canny')
        
        # 形态学操作
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
        
        # 查找轮廓
        contours_info = self.find_contours_with_feature(
            edges, min_area=50, max_area=2000, aspect_ratio_range=(0.3, 3.0)
        )
        
        # 寻找最可能的缺口轮廓
        gap_position = None
        max_score = 0
        
        for contour, bbox, area in contours_info:
            x, y, w, h = bbox
            
            # 计算特征分数（可以根据实际情况调整权重）
            # 1. 位置分数（缺口通常在上半部分）
            position_score = 1.0 if y < img.shape[0] * 0.6 else 0.5
            
            # 2. 形状分数（缺口通常比较规则）
            extent = float(area) / (w * h) if w * h != 0 else 0
            shape_score = 1.0 - abs(extent - 0.6)  # 假设缺口填充率为0.6左右
            
            # 3. 尺寸分数（缺口大小适中）
            size_score = 1.0 if 30 < w < 200 and 30 < h < 200 else 0.5
            
            # 总分
            total_score = position_score * shape_score * size_score
            
            if total_score > max_score:
                max_score = total_score
                gap_position = (x + w//2, y + h//2)  # 返回中心点
        
        return gap_position, max_score, contours_info
    
    def detect_slider_block(self, background_path):
        """
        检测滑块位置
        :param background_path: 背景图像路径（带滑块）
        :return: 滑块位置
        """
        # 检查文件是否存在
        if not os.path.exists(background_path):
            raise FileNotFoundError(f"背景图像文件不存在: {background_path}")
        
        # 图像预处理
        img, gray, edges = self.preprocess_image(background_path, method='canny')
        
        # 查找轮廓
        contours_info = self.find_contours_with_feature(
            edges, min_area=100, max_area=3000, aspect_ratio_range=(0.5, 2.0)
        )
        
        # 滑块通常在图像最左侧
        slider_position = None
        min_x = float('inf')
        
        for contour, bbox, area in contours_info:
            x, y, w, h = bbox
            
            # 寻找最左侧的轮廓
            if x < min_x:
                min_x = x
                slider_position = (x + w//2, y + h//2)  # 返回中心点
        
        return slider_position, contours_info
    
    def calculate_slider_distance(self, background_path, method='feature'):
        """
        计算滑块需要移动的距离
        :param background_path: 背景图像路径
        :param method: 检测方法 ('feature', 'template')
        :return: 滑块需要移动的距离
        """
        # 检查文件是否存在
        if not os.path.exists(background_path):
            raise FileNotFoundError(f"背景图像文件不存在: {background_path}")
        
        if method == 'template':
            # 需要提供模板图像路径
            template_path = "gap_template.png"
            try:
                # 检查模板文件是否存在
                if not os.path.exists(template_path):
                    raise FileNotFoundError(f"模板图像文件不存在: {template_path}")
                
                top_left, bottom_right, score = self.detect_gap_by_template_matching(
                    background_path, template_path
                )
                gap_x = top_left[0]
                return gap_x, {'method': 'template', 'score': score}
            except Exception as e:
                print(f"模板匹配失败: {e}")
                method = 'feature'  # 回退到特征分析
        
        if method == 'feature':
            # 特征分析方法
            gap_position, gap_score, _ = self.detect_gap_by_feature_analysis(background_path)
            slider_position, _ = self.detect_slider_block(background_path)
            
            if gap_position and slider_position:
                distance = gap_position[0] - slider_position[0]
                return distance, {
                    'method': 'feature', 
                    'gap_position': gap_position, 
                    'slider_position': slider_position,
                    'score': gap_score
                }
            elif gap_position:
                # 只检测到缺口位置，假设滑块在最左侧
                distance = gap_position[0]
                return distance, {
                    'method': 'feature_only_gap', 
                    'gap_position': gap_position,
                    'score': gap_score
                }
        
        # 默认返回值
        return 0, {'method': 'default', 'score': 0}
    
    def visualize_result(self, background_path, result_info):
        """
        可视化检测结果
        :param background_path: 背景图像路径
        :param result_info: 计算结果信息
        """
        # 检查文件是否存在
        if not os.path.exists(background_path):
            raise FileNotFoundError(f"背景图像文件不存在: {background_path}")
        
        # 读取图像
        img = cv2.imread(background_path)
        if img is None:
            raise FileNotFoundError(f"无法读取背景图像文件: {background_path}，请检查文件格式是否正确")
        
        # 根据不同方法绘制结果
        method = result_info.get('method', 'default')
        
        if method == 'template':
            # 模板匹配结果已在detect_gap_by_template_matching中处理
            pass
        elif method in ['feature', 'feature_only_gap']:
            # 绘制特征分析结果
            gap_pos = result_info.get('gap_position')
            slider_pos = result_info.get('slider_position')
            
            if gap_pos:
                # 绘制缺口位置
                cv2.circle(img, gap_pos, 10, (0, 0, 255), 2)
                cv2.putText(img, f'Gap: {gap_pos}', (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
            if slider_pos:
                # 绘制滑块位置
                cv2.circle(img, slider_pos, 10, (0, 255, 0), 2)
                cv2.putText(img, f'Slider: {slider_pos}', (10, 60), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # 显示距离信息
        distance = result_info.get('distance', 0)
        score = result_info.get('score', 0)
        cv2.putText(img, f'Distance: {distance}px', (10, 90), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv2.putText(img, f'Score: {score:.2f}', (10, 120), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        
        # 显示图像
        plt.figure(figsize=(15, 10))
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(f'Slider Captcha Detection Result (Method: {method})')
        plt.axis('off')
        plt.tight_layout()
        plt.show()

def main():
    """
    主函数，演示如何使用AdvancedSliderSolver类
    """
    # 创建高级滑块验证码识别对象
    solver = AdvancedSliderSolver()
    
    # 示例用法（需要替换为实际的图像路径）
    background_path = "captcha_background.png"  # 背景图像路径
    
    try:
        # 计算滑块需要移动的距离
        distance, info = solver.calculate_slider_distance(background_path, method='feature')
        
        # 添加距离信息到结果
        info['distance'] = distance
        
        print(f"检测方法: {info.get('method')}")
        print(f"滑块需要移动的距离: {distance} 像素")
        print(f"置信度分数: {info.get('score', 0):.2f}")
        
        if 'gap_position' in info:
            print(f"缺口位置: {info['gap_position']}")
        if 'slider_position' in info:
            print(f"滑块位置: {info['slider_position']}")
        
        # 可视化检测结果
        solver.visualize_result(background_path, info)
        
    except FileNotFoundError as e:
        print(f"错误: {e}")
        print("请确保提供了正确的图像文件路径")
    except Exception as e:
        print(f"处理过程中发生错误: {e}")

if __name__ == "__main__":
    main()