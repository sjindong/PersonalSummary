#!/usr/bin/env python3    #linux使用，window忽略
# -*- coding: utf-8 -*-

#这里学习pytho的笔记，基本一样
# https://www.liaoxuefeng.com/

#直接运行python
##1.引用包，
##2.linux执行命令（添加权限），chmod a+x print.py

#调用函数
help(abs)

abs(-89)
max(2,3,3,1)
int('123') #类型转换

a = abs #已有方法搞个别名
a(-90)


#定义函数
def my_abs(x):
    if not isinstance (x,(int,float)):  #处理非法参数，返回自定义错误消息
        raise TypeError('bad operand type')
    if x<0:
        return -x
    else:
        return x

#调用其他文件的函数,froom（关键字）  文件名 import 函数名
from base_1_method import my_abs

#空函数
def nop():
    pass

import math
def move(x,y,step,angle=0):  #这里angel 设置了默认值，然后
    nx = x+step*math.cos(angle)
    ny = y+step*math.sin(angle)
    return nx,ny
r = move(0,0,3,0)

#！！！！！ 定义默认参数要牢记一点：默认参数必须指向不变对象！ list会出现问题
def add_end(L=[]):
    L.append('END')
    return L

# >>> add_end()
# ['END', 'END']
# >>> add_end()
# ['END', 'END', 'END']

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(*numbers):
     sum = 0
     for n in numbers:
         sum = sum + n * n
     return sum
# *nums表示把nums这个list的所有元素作为可变参数传进去

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

#！！！ 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def person(name,age,*,city=‘beijing’,job)
#命名关键字参数，需要特殊嗯个服*
#指定可变参数 ，city 有默认值，可以调用的时候 不传入

def person(name,age,*aa,city=‘beijing’,job)
#如果前面有个可变参数，后面就不需要特殊分隔符 * 了


#递归函数
#使用递归函数需要注意防止栈溢出
def fact(n):
    if  n == 1:
        return 1
    return n*fact(n-1)

#尾递归  ： python对 尾递归 没有做优化，所以也会导致栈溢出
def fact1(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
