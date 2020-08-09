for cock in range(1, 20):
    for chick in range(3, 100, 3):
        hen = 100 - cock - chick
        if cock * 5 + hen * 3 + chick // 3 == 100 and hen > 0:
            print('公鸡',cock,'只，母鸡',hen,'只','小鸡',chick,'只')