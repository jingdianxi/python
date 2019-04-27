# 猜单词游戏
import random
# 建立单词库
words = ["apple", "banana", "cat", "dog", "echo", "fruit", "program", "tiger", "king", "queen"]
# 随机选取单词
word = words[random.randint(0, len(words) - 1)]
# 允许猜错次数
times = 5
print("您有" + times.__str__() + "次机会")
# 显示结果
wordList = list("-" * len(word))
print("".join(wordList))
# 游戏开始
while True:
    # 当允许猜错次数耗尽时，游戏结束
    if times == 0:
        print("游戏结束，正确答案：" + word)
        break
    # 等待用户输入
    char = input("请输入一个字母：")
    # 判断用户输入内容格式正确
    if not char.isalpha() or len(char) != 1:
        print("请不要输入非字母或多个字母")
        continue
    # 判断用户输入的字母是否存在于目标单词中
    if char in word:
        print("正确")
        # 若用户输入的字母存在于目标单词中，则更新显示结果
        for i in range(len(word)):
            if char == word[i]:
                wordList[i] = char
    else:
        # 若用户输入的字母不存在于目标单词中，则允许猜错次数减少1
        times -= 1
        print("您有" + times.__str__() + "次机会")
    # 显示结果
    print("".join(wordList))
    # 当全部字母被猜中时，游戏胜利
    if "-" not in wordList:
        print("游戏胜利")
        break
