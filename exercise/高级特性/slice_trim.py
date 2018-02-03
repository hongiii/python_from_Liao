# -*- coding: utf-8 -*-
# def trim(s):
#     if not isinstance(s, str):
#         raise TypeError("input is not string")
#     length = len(s)
#     beg = 0
#     end = length
#     L = list(range(length))
#     for i in L:
#         if s[i] != ' ':
#             break
#         else:
#             beg += 1
#     for i in L:
#         if s[length - i - 1] != ' ':
#             break
#         else:
#             end -= 1
#     return s[beg: end]


def trim(s):
    if not isinstance(s, str):
        raise TypeError("input is not string")
    while s[0:1] is ' ':
        s = s[1:]
    while s[-1:] is ' ':
        s = s[0:-1]
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
