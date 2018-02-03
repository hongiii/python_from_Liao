# -*- coding: utf-8 -*-
from functools import reduce


def normalize(name):
    name = str.lower(name)
    return name.capitalize()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


DIGITS = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
          "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}


def str2float(s):
    length = len(s)

    def finddot(s):
        for i in range(length):
            if s[i] is ".":
                return i
    def char2int(s):
        return DIGITS[s]
    def integerpart(x, y):
        return 10 * x + y
    def add(x, y):
        return x + y
    i = finddot(s)
    intp = reduce(integerpart, map(char2int, s[0: i]))
    decp = reduce(integerpart, map(char2int, s[-length + i + 1:]))
    return reduce(add, [intp, pow(0.1, length - i - 1) * decp])

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

# 使用split相当于借助内置函数将浮点数划分成两部分，以上是手动划分。
