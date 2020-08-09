from mpl_toolkits.axisartist.axislines import SubplotZero
import numpy as np
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

# figure(窗口名, (宽, 高))
fig = plt.figure('数轴', (10, 4))

ax = SubplotZero(fig, 1, 1, 1)
fig.add_subplot(ax)

# 数轴初始化
ax.axis["xzero"].set_visible(True)
# 设置数轴文字
# ax.axis["xzero"].label.set_text('数轴')
# 设置文字颜色
# ax.axis["xzero"].label.set_color('green')

# 坐标箭头
ax.axis["xzero"].set_axisline_style("-|>")
# 隐藏坐标系
ax.axis["top",'left','right','bottom'].set_visible(False)
# 在中间显示
ax.set_ylim(-1, 10)
# 设置刻度
ax.set_xlim(-9, 9)

# 描点
x = 2
y = 0
plt.scatter(x, y, s=150, edgecolors='b', c='w')

# 线
t = np.arange(2.0, 10.0, 0.01)
s = (t - 2) ** 0.1
ax.plot(t, s)

plt.show()
