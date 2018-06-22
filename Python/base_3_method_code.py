#!/usr/bin/env python3    #linux使用，window忽略
# -*- coding: utf-8 -*-

#将函数本身赋值给变量
f = abs
f(-1)

#高阶函数
def add(x,y,f):
    return f(x)+f(y)

add(-5,-6,abs)


#map / reduce
def f(x):
    return x *x

r = map(f,[1,2,34,4,5])
list(r)
list(map(f,[1,2,3,4,5,5]))

#reduce
#循环调用
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#函数f 必须接收两个参数，然后reduce把结果和下个参数进行操作
#案例：数据类型转换，str ，char，数字，map，【】

#fitter
#筛选数据
#一次作用每个参数，然后根据结果 true 或者false，来决定是否除去参数
list(fitter(mathod,[1,2,3,4,5,6,6]))


def _odd_iter():
    n =1
    while True:
        n = n+2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
a=[]
for n in primes():
    if n < 1000:
        a.append(n)
    else:
        break
a

#sorted  排序算法
#key 进行运算结果比较
#reverse true  反向排序
sorted([6,5,4,3,21,1])
sorted([-1,2,-4,6, -5,4],key = abs)
sorted(['asd','cde','Aas',"Te",'23a','4d'],key = str.lower,reverse =True) #按照ASCII编码， 但int类型数字不在其中

#返回函数
f = lazy_sum(1, 3, 5, 7, 9)
f() #才会输出具体结果
#闭包
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


#匿名函数
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#这里的 lambda x: x*x 就是前面定义的函数，


#装饰器
没懂， 以后需要加深学习

#偏函数
int2 = functools.partial(int, base=2)
#取代下面函数
def int2(x, base=2):
    return int(x, base)

#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
