import cv2
import numpy as np
from matplotlib import pyplot as plt

class SliderCaptchaSolver:
    """
    图像滑块验证码识别类
    用于识别滑块验证码中滑块需要移动的距离
    """
    
    def __init__(self):
        pass
    
    def preprocess_image(self, img_path):
        """
        预处理图像
        :param img_path: 图像路径
        :return: 预处理后的图像
        """
        # 读取图像
        img = cv2.imread(img_path)
        if img is None:
            raise FileNotFoundError(f"无法读取图像文件: {img_path}")
        
        # 转换为灰度图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # 高斯模糊去除噪声
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # 边缘检测
        edges = cv2.Canny(blurred, 50, 150)
        
        return img, gray, edges
    
    def find_slider_template(self, img_path):
        """
        查找滑块模板位置
        :param img_path: 包含滑块的图像路径
        :return: 滑块位置坐标
        """
        img, gray, edges = self.preprocess_image(img_path)
        
        # 使用模板匹配查找滑块
        # 这里需要一个滑块模板图像
        # 在实际使用中，您需要提供一个滑块的模板图片
        # template = cv2.imread('slider_template.png', 0)
        # w, h = template.shape[::-1]
        # res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # return max_loc, (max_loc[0] + w, max_loc[1] + h)
        
        # 临时返回默认值，实际使用时需要提供模板
        return (0, 0), (50, 50)
    
    def detect_gap_position(self, background_path, slider_path=None):
        """
        检测缺口位置
        :param background_path: 背景图像路径
        :param slider_path: 滑块图像路径（可选）
        :return: 缺口位置的x坐标
        """
        # 读取背景图像
        bg_img = cv2.imread(background_path)
        if bg_img is None:
            raise FileNotFoundError(f"无法读取背景图像文件: {background_path}")
        
        # 转换为灰度图像
        bg_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
        
        # 图像预处理
        # 1. 高斯模糊
        bg_blur = cv2.GaussianBlur(bg_gray, (5, 5), 0)
        
        # 2. 边缘检测
        bg_edges = cv2.Canny(bg_blur, 50, 150)
        
        # 3. 形态学操作，闭运算连接边缘
        kernel = np.ones((5, 5), np.uint8)
        bg_closed = cv2.morphologyEx(bg_edges, cv2.MORPH_CLOSE, kernel)
        
        # 查找轮廓
        contours, _ = cv2.findContours(bg_closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # 寻找缺口轮廓（根据实际验证码特点调整参数）
        gap_x = 0
        for contour in contours:
            # 计算轮廓的边界框
            x, y, w, h = cv2.boundingRect(contour)
            
            # 根据缺口的特点进行筛选（需要根据实际情况调整）
            # 例如：缺口通常在图像的上半部分，宽度较小等
            if 20 < w < 100 and 20 < h < 100 and y < bg_img.shape[0] / 2:
                gap_x = x
                break
        
        return gap_x
    
    def calculate_slider_distance(self, background_path, slider_path=None):
        """
        计算滑块需要移动的距离
        :param background_path: 背景图像路径
        :param slider_path: 滑块图像路径（可选）
        :return: 滑块需要移动的距离
        """
        # 获取缺口位置
        gap_x = self.detect_gap_position(background_path, slider_path)
        
        # 如果提供了滑块图像，则计算滑块位置
        slider_x = 0
        if slider_path:
            try:
                slider_pos, _ = self.find_slider_template(slider_path)
                slider_x = slider_pos[0]
            except:
                # 如果找不到滑块，则使用默认值0
                pass
        
        # 计算需要移动的距离
        distance = gap_x - slider_x
        
        return distance, gap_x, slider_x
    
    def visualize_detection(self, background_path, distance):
        """
        可视化检测结果
        :param background_path: 背景图像路径
        :param distance: 计算出的距离
        """
        # 读取图像
        img = cv2.imread(background_path)
        
        # 在图像上绘制检测结果
        if distance > 0:
            # 绘制一条垂直线表示缺口位置
            cv2.line(img, (distance, 0), (distance, img.shape[0]), (0, 255, 0), 2)
            # 添加文字说明
            cv2.putText(img, f'Distance: {distance}px', (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # 显示图像
        plt.figure(figsize=(12, 8))
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title('Slider Captcha Detection Result')
        plt.axis('off')
        plt.show()

def main():
    """
    主函数，演示如何使用SliderCaptchaSolver类
    """
    # 创建滑块验证码识别对象
    solver = SliderCaptchaSolver()
    
    # 示例用法（需要替换为实际的图像路径）
    background_path = "background.png"  # 背景图像路径
    slider_path = "slider.png"          # 滑块图像路径（可选）
    
    try:
        # 计算滑块需要移动的距离
        distance, gap_x, slider_x = solver.calculate_slider_distance(background_path, slider_path)
        
        print(f"缺口位置: {gap_x}")
        print(f"滑块位置: {slider_x}")
        print(f"需要移动的距离: {distance} 像素")
        
        # 可视化检测结果
        solver.visualize_detection(background_path, distance)
        
    except FileNotFoundError as e:
        print(f"错误: {e}")
        print("请确保提供了正确的图像文件路径")
    except Exception as e:
        print(f"处理过程中发生错误: {e}")

if __name__ == "__main__":
    main()