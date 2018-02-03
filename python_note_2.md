## Python笔记（二）
### 高级特性
1行代码能实现的功能，决不写5行代码。
#### 切片
切片（Slice）操作可以取指定索引范围的数据，比如取list或tuple的部分元素。
```python
L = list(range(100))
# 每两个取一个
print(L[1:10:2])
print(L[-20:-10:2])
```
#### 迭代
如果给定一个list或tuple，可以通过`for`循环来遍历这个list或tuple，这种遍历称为迭代。
在Python中，迭代通过`for...in`来完成。对于dict，默认情况下迭代的是key，如果要迭代value，可以用`for value in d.values()`，如果要同时迭代key和value，可以用`for k, v in d.items()`。字符串也可以迭代。

#### 列表生成式
列表生成式是Python内置的可以用来创建list的生成式。运用列表生成式可以很快生成一个list。
举例：
```Python
L = list(range(11))
print(L)

s = [x*x for x in range(1, 11)]
print(s)
s = [x+x for x in range(1, 11)]
print(s)
s = [x+2 for x in range(1, 12)]
print(s)

s = [m+n for m in range(1, 12) for n in range(1, 10)]
print(s)

s = [m+n for m in "abc" for n in "xyz"]
print(s)

s = [d for d in os.listdir('.')]
print(s)

d = {"x": "A", "y": "B", "z": "C"}
s = [k + '=' + v for k, v in d.items()]
print(s)

L = ["DSDS", "DSDS", "DSDSSWW"]
s = [l.lower() for l in L]
print(s)
```

#### 生成器
生成器generator可以简单理解成一边循环一边计算的机制。
注意区分普通函数和generator函数，前者调用直接返回结果，后者返回generator对象。

#### 迭代器
可以被`next()`函数调用不断返回下一个值的对象称为迭代器：`Iterator`。生成器都是迭代器，但是list、dict、str虽然是`Iterable`却不是`Iterator`，可以通过`iter()`函数把它们变成`Iterator`。

<b>为什么`isinstance((x for x in range(10)), Iterator)`是`True`而`isinstance([x for x in range(10)], Iterator)`是`False`？</b>
后者是list生成式，可以看成list的`append`操作，把`for`的内容每次扩展到list中，但是元组tuple不行，它不支持扩展，基本都是一次生成，上面那个是生成器对象，而下面是个list。

### 函数式编程
函数：一种封装，定义了相关操作
函数式编程：将整个业务流程转化为函数之间的互相调用
面向对象编程：对象（函数+数值）之间的相互调用。

#### 高阶函数
一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数。编写高阶函数，就是让函数的参数能够接收别的函数。
```Python
def add(x, y, f):
  return f(x) + f(y)
print(-4, 5, abs)
```

##### map/reduce
Python内建了`map()`和`reduce()`函数，`map()`对数据执行分批并行操作，`reduce()`对操作所有返回值求结果。
`map()`函数接收两个参数，一个是函数，一个是'Iterable'，`map`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`返回。
`reduce()`把一个函数作用在一个序列上，这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做运算。
这里贴一个示例，将字符串转化为整数：
```Python
from functools import reduce
DIGITS = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
          "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: 10 * x + y, map(char2num, s))

print("1234")
```

##### filter
过滤器`filter()`和`map()`类似，也接收一个函数和一个序列，和`map()`不同的是，`filter()`把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素。
`filter()`使用了惰性计算。

##### sorted
排序的核心是比较两个元素的大小，Python内置的`sorted()`函数是一个高阶函数，可以对list进行排序，还可以接收一个`key`函数来实现自定义的排序。key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
对字符串排序，默认是按照ASCII的大小来进行比较的。
关于排序的示例，根据输出理解一下：
```python
L = ["bob", "about", "Zoo", "Credit"]
print(sorted(L))
print(sorted(L, key=str.lower))
print(sorted(L, key=str.lower, reverse=True))
```
#### 返回函数
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。返回一个函数时，该函数并未执行，返回函数中尽量不要引用任何可能会变化的变量。
<b>闭包</b>
通过Python语言介绍一下，一个闭包就是你调用了一个函数A，这个函数A返回了一个函数B给你，这个返回的函数B就叫做闭包，在调用函数A的时候传递的参数就是自由变量。举个栗子：
```Python
def func(name):
    def innner_func(age):
        print(name, age)
    return innner_func

bb = func("Jimf")
bb(21)
```
这里面调用`func`的时候就产生可一个闭包`innner_func`，并且该闭包持有自由变量`name`，因此这也意味着，当函数`func`的生命周期结束之后，`name`这个变量依然存在，因为它被闭包引用了，所以不会被回收。

#### 匿名函数
关键字`lambda`表示匿名函数，冒号前面的表示函数参数。匿名函数有个限制，就是只能有一个表达式，不用写`return`，返回值就是表达式的结果。用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突，此外，匿名函数也是一个函数对象，可以把它赋值给一个变量。
```Python
L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6]))
print(L)


def f(x):
    return x * x

f = lambda x: x * x
print(f)

def build(x, y):
    return lambda: x * x + y * y
```

#### 装饰器
Python的decorator可以用函数来实现，也可以用类来实现。装饰器（decorator）的功能是<b>将被装饰的函数当作参数传递给与装饰器对应的函数（名称相同的函数），并返回包装后的被装饰的函数。</b>看示意图，其中`a`是与装饰器`@a`对应的函数，`b`为装饰器修饰的函数：
![image](https://segmentfault.com/img/bVsSKY)

简而言之：`@a`就是将`b`传递给`a()`，并返回新的`b = a(b)`。

#### 偏函数
简单总结`functools.partial`的作用就是，把一个函数的某些参数固定住，返回一个新的函数，调用这个函数会更简单。

### 模块
模块是一组Python代码的集合，一个.py文件就称之为一个模块，可以使用其他模块，也可以被其他模块使用。
创建自己的模块时，要注意：
- 模块名称要遵循Python变量命名规范。
- 模块名称不要与系统模块名冲突。
- `_init_.py`文件表明该目录是一个包。

#### 使用模块
Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。
在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀（表示非公开）来实现的。外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
#### 安装第三方模块
在Python中，安装第三方模块，是通过包管理工具pip完成的。
当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到就会报错。
默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在`sys`模块的`path`变量中。
```Python
import sys
print(sys.path)
```
如果要添加自己的搜索目录，可以：
```python
import sys
sys.path.append("/.../...")
```
