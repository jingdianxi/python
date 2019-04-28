# 龟兔赛跑
from random import randint
import time

"""
比赛规则：
1. 乌龟
快走(Fast plod)，50%概率，向右3格
跌跤(Slip)，20%概率，向左6格
慢走(Slow plod)，30%概率，向右1格
2. 兔子
睡觉(Sleep)，20%，不动
大跳(Big hop)，20%，向右9格
大跌(Big slip)，10%，向左12格
小跳(Small hop)，30%，向右1格
小跌(Small slip)，20%，向左2格
"""

# 比赛双方位于起点
tPos = 0
hPos = 0

# 比赛开始
print("Go!")

# 比赛过程以循环实现，当有选手到达终点时，循环结束
while tPos < 70 and hPos < 70:
    # 赛道，长度70
    track = "_" * 70
    # 生成随机整数，范围1到10
    n = randint(1, 10)
    # 根据随机数改变乌龟的位置
    if 1 <= n <= 5:
        tPos += 3
    elif 6 <= n <= 8:
        tPos -= 6
    else:
        tPos += 1
    # 将乌龟的位置限制在赛道上
    if tPos < 0:
        tPos = 0
    # 根据随机数改变兔子的位置
    if n == 1 or n == 2:
        hPos = hPos
    elif n == 3 or n == 4:
        hPos += 9
    elif n == 5:
        hPos -= 12
    elif 6 <= n <= 8:
        hPos += 1
    else:
        hPos -= 2
    # 将兔子的位置限制在赛道上
    if hPos < 0:
        hPos = 0
    # 显示赛况
    if tPos == hPos:
        # 双方位置相同
        track = track[:tPos] + "咬" + track[tPos + 1:]
    else:
        # 乌龟的位置
        track = track[:tPos] + "龟" + track[tPos + 1:]
        # 兔子的位置
        track = track[:hPos] + "兔" + track[hPos + 1:]
    print(track)
    # 设置定时器
    time.sleep(0.5)

# 循环结束，公布比赛结果
if tPos >= 70:
    print("乌龟胜")
else:
    print("兔子胜")
