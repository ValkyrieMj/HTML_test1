import numpy as np
import struct
import matplotlib.pyplot as plt
import heapq
from collections import Counter



def max_list(lt):
    temp = 0
    for i in lt:
        if lt.count(i) > temp:
            max_str = i
            temp = lt.count(i)
    return max_str



if __name__ == '__main__':
    a = [2.0, 2.0, 2.0, 1.0, 5.0]
    re1 = map(a.index, heapq.nsmallest(3, a))  # 求最大的三个索引    nsmallest与nlargest相反，求最小
    re2 = heapq.nsmallest(3, a)  # 求最大的三个元素
    print(list(re1))  # 因为re1由map()生成的不是list，直接print不出来，添加list()就行了
    print(re2)
    b = max_list(a)
    print(b)


