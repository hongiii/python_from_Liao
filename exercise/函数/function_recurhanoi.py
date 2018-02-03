# -*- coding: utf-8 -*-
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')

# 汉诺塔问题是经典的分治问题，把n个盘子从A借助B挪到C，将问题分解为n-1个盘子从A借助B挪到C，还剩一个盘子，A直接挪到C上。
# 将n-1个盘子从A挪到B（借助C），剩下的一个直接从A移到C上，再将n-1个盘子从B挪到C（借助A）
