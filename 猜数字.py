import random

print("==========猜数字==========")
tar = random.randint(1, 10)
n = 0 # 用户输入的数字

while n != tar:
    try:
        n = int(input("请输入1到10的数字："))
    except:
        print("输入的不是数字，请输入正确的数字格式")
    else:
        if n > tar:
            print("猜大了")
        elif n < tar:
            print("猜小了")
        else:
            print("猜对了")
            break

print("游戏结束")
