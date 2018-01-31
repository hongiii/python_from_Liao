# -*- coding: utf-8 -*-
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax^2 + bx + c = 0
# 的两个解。
# 提示：计算平方根可以调用math.sqrt()函数：
import math


def quadratic(a, b, c):
    L = [a, b, c]
    for i in L:
        if not isinstance(i, int):
            raise TypeError("bad operand type")
    num1 = math.pow(b, 2) - 4 * a * c
    if num1 < 0:
        return
    elif num1 == 0:
        res = (-b)/(2*a)
        return res
    else:
        num2 = math.sqrt(num1)
        res1 = (-b + num2)/(2*a)
        res2 = (-b - num2)/(2*a)
        return res1, res2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
