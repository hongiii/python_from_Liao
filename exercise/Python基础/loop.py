# -*- codingt: utf-8 -*-
# 1~100累加
sum = 0
for x in range(101):
    sum += x
print(sum)

# 计算100以内奇数之和
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

# 利用循环依次对list中的每个名字打印出"Hello, xxx!"
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("Hello, %s!" % name)
