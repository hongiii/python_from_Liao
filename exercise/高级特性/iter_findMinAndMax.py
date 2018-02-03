# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if len(L) is 0:
        return (None, None)
    mind = maxd = L[0]
    for i in L:
        if i < mind:
            mind = i
        elif i > maxd:
            maxd = i
    return (mind, maxd)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
