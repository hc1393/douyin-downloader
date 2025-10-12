import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 设置Matplotlib后端以解决PyCharm的兼容性问题
matplotlib.use('agg')  # 使用非交互式Agg后端

# 三维网格参数
X_RES = 100  # X轴网格数
Y_RES = 50  # Y轴网格数
GRID_SIZE = 10.0  # 网格覆盖范围 (米)

# Gerstner波参数
NUM_WAVES = 5  # 叠加波数量
AMPLITUDES = [0.4, 0.3, 0.2]  # 各波振幅 (米)
WAVE_LENGTHS = [6.0, 4.0, 8.0]  # 波长 (米)
SPEEDS = [1.0, 0.8, 1.2]  # 波速 (米/秒)
DIRECTIONS = np.linspace(0, 2 * np.pi, NUM_WAVES)  # 传播方向 (弧度)

# 初始化三维网格
x = np.linspace(-GRID_SIZE / 2, GRID_SIZE / 2, X_RES)
y = np.linspace(-GRID_SIZE / 2, GRID_SIZE / 2, Y_RES)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)


def gerstner_wave(x, y, t, k, a, theta, speed):
    """计算单个Gerstner波对顶点位置的影响"""
    phase = k * (x * np.cos(theta) + y * np.sin(theta)) - speed * t
    dx = a * np.cos(theta) * np.cos(phase)
    dy = a * np.sin(theta) * np.cos(phase)
    dz = a * np.sin(phase)
    return dx, dy, dz


def update(frame):
    """动态更新海面高度"""
    global X, Y, Z
    t = frame * 0.1  # 时间因子

    new_X = X.copy()
    new_Y = Y.copy()
    new_Z = np.zeros_like(Z)

    for i in range(NUM_WAVES):
        a = AMPLITUDES[i % len(AMPLITUDES)]
        length = WAVE_LENGTHS[i % len(WAVE_LENGTHS)]
        k = 2 * np.pi / length  # 波数
        speed = SPEEDS[i % len(SPEEDS)]
        theta = DIRECTIONS[i]

        dx, dy, dz = gerstner_wave(new_X, new_Y, t, k, a, theta, speed)
        new_X += dx
        new_Y += dy
        new_Z += dz

    ax.clear()
    ax.plot_surface(new_X, new_Y, new_Z, cmap='ocean', rstride=1, cstride=1)
    ax.set_zlim(-1, 1)
    ax.set_title(f'3D Gerstner Waves (t={t:.1f}s)')
    return ax,

# 创建动画ffmpeg
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ani = FuncAnimation(fig, update, frames=100, interval=50)
# 替代方案：保存为视频文件
ani.save('ocean_waves.gif', writer='pillow', dpi=80, fps=20)
print("动画已保存为GIF文件：ocean_waves.gif")



