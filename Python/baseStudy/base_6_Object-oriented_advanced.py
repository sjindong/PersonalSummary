#!/usr/bin/env python3
#linux使用，window忽略
# -*- coding: utf-8 -*-

#面向对象高级编程

#使用 __slots__
__slots__
class Student(object):
    pass

s = Student()
s.name = 'Michael'

def set_age(self,age): #定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s) #给实例绑定一个方法

#调试方法
s.set_age(25)
s.age

#所有实例都需要使用这个方法，可以给类绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

# __slots__限定变量定义
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

#仅对当前类有效，对继承的子类无效


#使用@property
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

#多重继承
class Bat(Mammal, Flyable):
    pass
MixIn 是用于多继承类的一个标志
由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。

只允许单一继承的语言（如Java）不能使用MixIn的设计。


#定制类
__str__  ：打印类的参数信息

class Student(object):
...     def __init__(self, name):
...         self.name = name
...     def __str__(self):
...         return 'Student object (name: %s)' % self.name
...__repr__ = __str__
# __repr__  是程序开发者可见的
# __str__   是print打印调用的
>>> print(Student('Michael'))
Student object (name: Michael)

__iter__ ：声明列表，能够被for ... in 一样使用
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

__getitem__：获取第几个参数
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
兼容 传入的 int类型或是切片类型
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

__getattr__：避免调用不存在的参数时报错，需要重定义方法
#调用不存在参数
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
#调用不存在的函数
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
只有在没有找到该属性或者该方法的时候才会在 getattr方法中查找，
getattr默认返回None
#常规处理，响应几个特殊的，其他按照
class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
这种完全动态调用的特性作用就是，可以针对完全动态的情况作调用。
现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：

这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
还有些REST API会把参数放到URL中，比如GitHub的API：
GET /users/:user/repos

__call__：直接对实例进行调用
一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。

任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
调用方式如下：

>>> s = Student('Michael')
>>> s() # self参数不要传入
My name is Michael.
__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：

>>> callable(Student())
True
>>> callable(max)
True
>>> callable([1, 2, 3])
False
>>> callable(None)
False
>>> callable('str')
False
通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

小结
Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。


#使用枚举类
