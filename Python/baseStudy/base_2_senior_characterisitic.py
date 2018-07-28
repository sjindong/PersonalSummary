#!/usr/bin/env python3    #linux使用，window忽略
# -*- coding: utf-8 -*-

# python 中 代码越少越好， 不要超过5行

#切片Slice
L[] #list 或 tuple
L[0:n] #截取从0开始到n为止，但不包括n
L[:n] #效果同上， 如果是0开始，则可以隐藏

L[-1] #倒数第一个参数
L[-3:-1] #倒数 第3个参数 ，倒数第2个参数， 不包括最后一个参数
L[-3:] #最后三个参数

L[start : end : space/interval]
L[::5] #每五个取一个
L[:10:2] #前10个，每2个取一个


#tuple 也是可以，结果还是tuple
(1,2,3,4,5)[1:3]   #return   (2,3)

#字符串 ，结果返回 也是 字符串
'abcdefg'[:3] #return  'abc'

#只要是 可迭代的对象，均可以使用 for
#已知：string ，list ，tuple，dict
for l in 'abc':
  print(l)

#判断是否是可迭代对象
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代


#
for i,value in enumerate(['a','b','c']):
    print(i,value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

#列表生成器
[x * x for x in range(1,11)]
[x * x for x in range(1,11) if  x%2 ==0]
[m+n for m in "ABC" for n in "XYZ"]

#列出文件目录
import os #导入os模块
[d for d in os.listdir('.')]

[s.lower() for s in L] #将字符串均变成小写
d = {'x':'a','2':'b','3':'c'}
[k +'='+v for k,v in d.items()] #dict类型对象

#生成器：generator 和list区别是[] 变成了()
g = (x*x for x in range(10))
next(g)
for n in g:
    print(n)


g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


yield 1     #打断 生成器
yield (1)   #打断 生成器

#迭代器
#可以被next不断调用
from  collections import Iterable
isinstance([],Iterable) #判断类型
#可以被next()调用 并不断返回下一个值的对象称为 迭代器 Iterator
isinstance(iter([]), Iterator)  #list ,dict ,str 等Itrable比那成 Iterator
