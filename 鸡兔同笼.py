def compu(animal, foot):
    chicken = (4 * animal - foot) / 2
    rabbit = animal - chicken
    if chicken >=0 and rabbit >= 0 and chicken == int(chicken) and rabbit == int(rabbit):
        print("鸡有{}只，兔有{}只".format(int(chicken), int(rabbit)))
    else:
        print("{}只动物{}条腿的情况无解".format(animal, foot))


animal = int(input('请输入动物的数量：'))
foot = int(input('请输入脚的数量：'))
compu(animal, foot)