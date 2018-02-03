## Python笔记（一）
### Python简介
- 是一种解释型语言，代码在执行时一行一行翻译成CPU能理解的机器码。
- 包含内置库，和大量的第三方库。
- 适合开发网络应，包括网站、后台服务等；还有许多日常需要的小工具，包括系统管理员需要的脚本任务等；另外还可以把其他语言开发的程序再包装起来，方便使用。

### 第一个Python程序
#### Python的交互模式和直接运行`.py`文件的区别
- 直接输入`python`进入交互模式，相当于启动了Python解释器，输入一行执行一行。
- 直接运行`.py`文件相当于启动了Python解释器，然后一次性把.py文件的源代码执行了，无法以交互的方式输入源代码。

#### 输入输出
`input()`和`print()`是最基本的输入和输出。
示例:
```python
name = input("please input your name: ")
print("hello, ", name)
```
### Python基础
Python使用缩进来组织代码块，一般使用4个空格的缩进。

#### 数据类型和变量
Python能直接处理的数据类型有：
- 整型
没有大小限制
- 浮点数
没有大小限制，超出一定范围直接表示为`inf`
- 字符串
`r''`表示`''`内部的字符串默认不转义，`'''...'''`的格式可以表示多行内容：
```python
print('\t\n')
print(r'\t\n')
print('''line1
line2
line3''')
```
运行结果：
@import "/pic/1.png"

- 布尔值
`True`和`False`，布尔值常用在条件判断中，可以用`and`、`or`和`not`运算。
- 空值
用`None`表示。
- 变量
可以把任意数据类型赋值给变量，一个变量可以反复赋值，而且是不同类型的变量：
```Python
a = 123
print(a)
a = "good night"
print(a)
```
<b> 理解变量在内存中的表示 </b>
```Python
a = '123'
```
以上代码，Python解释器做了两件事：
1. 在内存中创建了一个`'123'`的字符串
2. 在内存中创建了一个变量`a`，并把它指向`'123'`
也可以将变量`a`赋值给`b`，这个操作实际上是将变量`b`指向变量`a`所指向的数据。

- 常量
在Python中通常用全部大写的变量名表示常量。如
```bash
PI = 3.1415926
```

#### 字符串和编码
##### 编码
- ASCII
- Unicode
- UTF-8
在计算机内存中，统一使用`Unicode`编码，当需要保存到硬盘或者需要传输的时候，就转换为`UTF-8`编码。
##### 字符串
在Python 3版本中，字符串以`Unicode`编码，也就是支持多语言。`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符。
###### 格式化
在Python中，采用的格式化方式和C语言一致，用`%`实现：
```python
print(("hi, %s has %d apples.") % ('Mary', 12))
```
`%s`表示用字符串替换，`%d`表示用整数替换，有多少`%?`占位符，后面就跟几个变量，顺序要对应好。如果只有一个占位符，括号可省略。
常见的占位符有：
占位符 | 替换内容
- | -
%d | 整数
%f | 浮点数
%s | 字符串
%x | 十六进制整数

#### 使用list和tuple
list和tuple是Python内置的有序集合，一个可变，一个不可变，根据需要来选择使用。
##### 使用list
Python内置的一种数据类型是列表：list。它是一种有序的集合，可以随时添加和删除元素。
```python
# -*- coding: utf-8 -*-
classmates = ["Michael", "Bob", "Tracy"]
print(classmates)
print(len(classmates))
print(classmates[0], classmates[1], classmates[2])
print(classmates[-1], classmates[-2], classmates[-3])
# 追加元素到末尾
classmates.append("Adam")
# 将元素插入到指定位置
classmates.insert(1, "Jack")
# 删除list末尾元素
classmates.pop()
# 删除指定位置的元素
classmates.pop(1)
# 把个别元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
# list中的数组元素也可以不同，list元素可以是另一个list，如
L = [1, 2, '3']
M = [1, 2, [1, 2, '3']]
```
##### 使用tuple
另一种有序列表叫元组：tuple。它和list非常类似，但是tuple一旦初始化就不能修改（指向）。
```Python
tup = (1, 2, 3)
print(tup)
print(tup[0], tup[-1])
# 定义一个空tuple
tup = ()
# 定义一个只有1个元素的tuple，加','消除歧义
tup = (1, )
```

#### 条件判断
条件判断可以计算机自己做选择，Python的if...elif...else很灵活，且条件判断从上到下进行匹配，当满足条件时执行对应的块内语句，后续的elif和else都将不再执行。
```python
birth = input("input your birthdate: ")
birth = int(birth)
if birth < 2000:
    print("you are an adult")
else:
    print("you are young and treasure it.")
```

#### 循环
循环是让计算机重复任务的有效方法，循环有三种形式：
- for
- while
- do...while

提前结束循环：
- continue：提前结束本轮循环，进入下一次循环
- break：结束循环

补充：`range()`函数可以生成一个整数序列，再通过`list()`函数可以转换为list，比如`range(5)`生成的序列是0开始小于5的数。

#### 使用dict和set
##### dict
Python内置了字典dict的支持，使用key-value存储，具有极快的查找速度。
```Python
d = {"Micheal": 95, "Bob": 43, "Tracy": 85}
print(d["Micheal"])
# 通过key将数据放入dict
d["Adam"] = 67
print(d["Adam"])
# 多次对一个key放入value，后面的值会把前面的冲掉：
d["Jack"] = 90
print(d["Jack"])
d["Jack"] = 80
print(d["Jack"])
# 查找key是否存在，有两种方法，in判断和get函数
if "Tom" in d:
    print(d["Tom"])
else:
    print("don't exist.")
# 如果key不存在，返回None，或者自己指定value，比如下面第二行指定返回-1
print(d.get("Tom"))
print(d.get("Tom", -1))
# 删除一个key
d.pop("Bob")
print(d)
```
##### set
set和dict类似，也是一组key的集合，但不存储value，且set中没有重复的key。
```python
# 创建一个set，需要提供一个list作为输入集合
s = set([1, 1, 2, 3])
print(s)
# 添加元素到set，重复添加不会有效果
s.add(4)
print(s)
s.add(4)
print(s)
# 从set中删除元素
s.remove(4)
print(s)
# set集合可以做交集、并集等运算
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
```
##### 对不可变对象的补充说明
set和dict的区别仅在于没有存储对应的value，两者都不可以放入可变对象。
比如，字符串是不可变对象，而list是可变对象，看下面代码，对比输出理解一下。这里的a是变量，`"abc"`是不可变对象，`a.replace`方法创建了一个新的字符串"Abc"并返回，用变量b指向该新字符串，变量`a`仍指向原有的字符串`"abc"`，`a = "xyz"`改变了指向，此时`a`指向`"xyz"`。但是字符串`"abc"`没有变。
```python
a = "abc"
print(a.replace('a', 'A'))
b = a.replace('a', 'A')
print(b)
print(a)
a = 'xyz'
print(a)
```
@import "/pic/2.png"

### 函数
#### 调用函数
调用Python函数，需要根据函数定义，传入正确的参数。
Python内置函数：[内置函数](https://docs.python.org/3/library/functions.html#abs)

#### 定义函数
定义函数时，需要确定函数名和参数个数，如：
```Python
def add(num1, num2):
```
如果有必要，可以先对参数的数据类型进行检查，可以使用`isinstance()`函数，函数体内部可以用`return`返回函数结果，函数执行完毕也没有`return`语句时，自动`return None`，且函数可以返回多个值，本质上是个元组tuple。

关于空函数，如果想定义什么也不做的空函数，可以使用`pass`语句：
```python
def pop():
  pass
```
`pass`实际上可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个`pass`， 让代码跑起来。

#### 函数的参数
除了正常定义的必选参数之外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
在Python中，可以用必选参数、默认参数、可变参数、关键字参数、命名关键字参数，这五种参数都可以组合使用，需注意：<b>参数定义的顺序必须是：必选参数、可选参数、可变参数、命名关键字参数、关键字参数。</b>
参数类型：
- 位置参数
- 默认参数
注意必选参数在前，默认参数在后。当函数有多个参数时，把变化大的参数放在前面，变化小的放在后面，可以作为默认参数。
<b>为什么默认参数要在必选参数后面？</b>
会引起歧义，python解释器有时候不知道到底是否采用默认参数。
*note:默认参数必须指向不变对象*
- 可变参数
可变参数允许传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。定义一个可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个`*`号：
```python
def calc(*number):
  sum = 0
  for n in number:
    sum += n
  return sum
```
调用
```python
L = [1, 2, 3]
print(calc(*L))
```
`*L`表示把`L`这个list的所有元素作为可变参数传进去。
- 关键字参数
关键字参数允许传入0个或任意个含参数名的参数，这些关键字在函数内部自动组装成为一个dict。示例：
```python
def person(name, age, **kw):
  print(name, age, kw)
```
关键字参数起到扩展函数的功能。
调用
```python
extra = {"city": "Beijing", "job": "Programmer"}
print(person("Jack", 24, **extra))
```
`**extra`表示把`extra`这个dict的所有key-value用关键字参数传入到函数的`**kw`参数里，`**kw`将获得一个dict。这里`kw`只是`extra`的一份拷贝，对`kw`的改动不会影响到`extra`

- 命名关键字参数
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，至于到底传入了哪些，需要在函数内部对`kw`进行检查。如果要限制关键字参数的名字，就可以使用命名关键字参数，例如只接受`city`和`job`作为关键字参数，这种方式定义的函数如下：
```python
def person(name, age, *, city, job):
  print(name, age, city, job)
```
和关键字参数`*kw`不同，命名关键字参数需要一个特殊的分隔符`*`，`*`后面的参数被视作命名关键字参数。
调用
```python
print(person("jack", 23, city = "beijing", job = "Programmer"))
```
如果函数定义中已经有一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了。比如，

```python
def person(name, age, *args, city, job):
  print(name, age, args, city, job)
```
命名关键字参数必须传入参数名，这和位置参数不同。

#### 递归函数
如果一个函数在内部调用自身，那这个函数就是递归函数。
使用递归函数的优点是逻辑结构简单清晰，缺点是过深的调用会导致栈溢出。
针对尾递归优化的语言可以通过尾递归防止栈溢出，Python标准的解释器没有针对尾递归做优化。
