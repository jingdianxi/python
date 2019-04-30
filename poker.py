# 纸牌游戏
from random import shuffle


# 建立纸牌类
class Poker:
    def __init__(self, suit, point):
        self.suit = suit
        self.point = point

    __suits = ["黑桃", "红心", "方块", "梅花"]
    __points = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __repr__(self):
        return self.__suits[self.suit] + self.__points[self.point]


# 准备整副纸牌
pokerList = []
for i in range(4):
    for j in range(13):
        pokerList.append(Poker(i, j))
# 洗牌（列表元素随机乱序）
shuffle(pokerList)
# 抓牌
pokers = []
for i in range(5):
    pokers.append(pokerList[i])
# 显示发牌结果
for i in pokers:
    print(i, end=" ")
print()

# 统计花色，以集合保存
suitSet = set()
# 统计点数，以字典保存
pointDict = {}
# 遍历发牌结果
for i in pokers:
    # 花色
    suitSet.add(i.suit)
    # 点数
    if not pointDict:
        # 当字典为空时，增加键值对，键为点数，值为1
        pointDict[i.point] = 1
    elif i.point not in pointDict.keys():
        # 当字典中无指定键时，增加键值对，键为点数，值为1
        pointDict[i.point] = 1
    else:
        # 当字典中有指定键时，对应值增加1
        pointDict[i.point] += 1
# 判定牌型
if len(pointDict) == 2:
    # 四条或葫芦
    if 4 in pointDict.values():
        print("四条")
    else:
        print("葫芦")
elif len(pointDict) == 3:
    # 三条或两对
    if 3 in pointDict.values():
        print("三条")
    else:
        print("两对")
elif len(pointDict) == 4:
    print("一对")
else:
    # 按点数升序排列
    for i in range(4):
        for j in range(i + 1, 5):
            if pokers[i].point > pokers[j].point:
                pokers[i], pokers[j] = pokers[j], pokers[i]
    if (pokers[1].point - pokers[0].point == 1 and pokers[2].point - pokers[1].point == 1 and pokers[3].point - pokers[2].point == 1 and pokers[4].point - pokers[3].point == 1) or (pokers[0].point == 0 and pokers[1].point == 9 and pokers[2].point == 10 and pokers[3].point == 11 and pokers[4].point == 12):
        if len(suitSet) == 1:
            print("同花顺")
        else:
            print("顺子")
    else:
        if len(suitSet) == 1:
            print("同花")
        else:
            print("无对")
