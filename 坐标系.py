import numpy as np #导入数值计算模块
import matplotlib.pyplot as plt #导入绘图模块
import mpl_toolkits.axisartist as axisartist #导入坐标轴加工模块

fig=plt.figure() #新建画布
ax=axisartist.Subplot(fig,1,1,1) #使用axisartist.Subplot方法创建一个绘图区对象ax
fig.add_axes(ax) #将绘图区对象添加到画布中

ax.axis[:].set_visible(False) #隐藏原来的实线矩形

ax.axis["x"] = ax.new_floating_axis(0, 0)  # 添加x轴
ax.axis["y"] = ax.new_floating_axis(1, 0)  # 添加y轴
ax.axis["x"].set_axis_direction('bottom')  # x轴刻度位置
ax.axis["y"].set_axis_direction('left')  # y轴刻度位置

ax.set_xticks(range(-4, 5)) #设置x坐标轴刻度
ax.set_yticks([-4, -3, -2, -1, 1, 2, 3, 4]) #设置y坐标轴刻度
ax.axis["x"].set_axisline_style("->", size=1.0)  #给x坐标轴加箭头
ax.axis["y"].set_axisline_style("->", size=1.0) #给y坐标轴加箭头
ax.annotate(s='x', xy=(0,0), xytext=(5.0,-0.4)) #x轴上标注字母
ax.annotate(s='y', xy=(0,1.0), xytext=(0.2,5.0)) #y轴上标注字母

plt.xlim(-5,5) #设置x坐标轴范围
plt.ylim(-5,5) #设置y坐标轴范围
plt.show() #显示坐标轴
