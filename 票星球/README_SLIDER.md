# 滑块验证码识别模块

## 简介

本项目包含三个主要模块，用于识别和解决滑块验证码问题：

1. `slider_captcha_solver.py` - 基础滑块验证码识别模块
2. `advanced_slider_solver.py` - 高级滑块验证码识别模块
3. `slider_gui.py` - 带图形界面的滑块验证码识别工具

## 功能特点

- 支持多种图像处理技术（Canny边缘检测、Sobel算子、Laplacian算子等）
- 多种检测方法（特征分析、模板匹配）
- 可视化检测结果
- 图形用户界面（GUI）
- 可调节的参数设置

## 安装依赖

```bash
pip install opencv-python
pip install numpy
pip install matplotlib
pip install PyQt5
```

## 使用方法

### 1. 基础模块使用

```python
from slider_captcha_solver import SliderCaptchaSolver

# 创建识别对象
solver = SliderCaptchaSolver()

# 计算滑块距离
distance, gap_x, slider_x = solver.calculate_slider_distance("background.png")

print(f"滑块需要移动的距离: {distance} 像素")
```

### 2. 高级模块使用

```python
from advanced_slider_solver import AdvancedSliderSolver

# 创建识别对象
solver = AdvancedSliderSolver()

# 计算滑块距离
distance, info = solver.calculate_slider_distance("background.png", method='feature')

print(f"滑块需要移动的距离: {distance} 像素")
print(f"检测方法: {info['method']}")
print(f"置信度分数: {info['score']}")
```

### 3. 图形界面工具

```bash
python slider_gui.py
```

运行后将打开图形界面，可以通过界面加载图像、调整参数并查看识别结果。

## 参数说明

### 图像处理参数

- `min_area`: 轮廓最小面积（默认50）
- `max_area`: 轮廓最大面积（默认2000）
- `aspect_ratio_range`: 轮廓宽高比范围（默认0.3-3.0）

### 检测方法

1. **特征分析 (feature)**: 通过分析图像特征识别缺口和滑块
2. **模板匹配 (template)**: 通过模板匹配识别缺口位置

## 识别原理

### 特征分析方法

1. 图像预处理：灰度化、高斯模糊、边缘检测
2. 轮廓检测：使用OpenCV查找图像轮廓
3. 特征筛选：根据面积、宽高比等特征筛选可能的缺口和滑块
4. 位置计算：计算缺口和滑块的相对位置，得出移动距离

### 模板匹配方法

1. 需要提供缺口的模板图像
2. 使用OpenCV的模板匹配功能在背景图像中查找缺口位置
3. 直接计算滑块到缺口的距离

## 使用建议

1. 对于不同的验证码样式，可能需要调整参数以获得最佳效果
2. 特征分析方法适用性更广，模板匹配方法在有模板图像时更精确
3. 可以通过可视化结果调试参数
4. 在实际应用中，建议结合多种方法提高识别准确率

## 注意事项

1. 需要提供清晰的验证码图像
2. 模板匹配方法需要提供准确的模板图像
3. 对于复杂或变形的验证码，可能需要进一步优化算法
4. 本工具仅用于学习和研究目的，请遵守相关法律法规

## 扩展开发

可以根据需要扩展以下功能：

1. 添加更多图像处理算法
2. 支持更多类型的验证码
3. 提高识别准确率和速度
4. 添加批量处理功能
5. 集成到自动化测试工具中