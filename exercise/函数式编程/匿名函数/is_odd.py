# -*- coding: utf-8 -*-
L = list(filter(lambda n: n % 2 == 0, range(1, 20)))

print(L)


def is_odd():
    return lambda n: n % 2 == 0
print(is_odd)

L = list(filter(is_odd(), range(1, 20)))

print(L)
