#!/usr/bin/env python3    #linux使用，window忽略
# -*- coding: utf-8 -*-

#这里学习pytho的笔记，基本一样
# https://www.liaoxuefeng.com/

#直接运行python
##1.引用包，
##2.linux执行命令（添加权限），chmod a+x print.py


print("python")
print("name = ","aaaa","bbbb")
print("1+1=",1+1)

name = input()
name2 = input("name:")

a = 1000
if a>=0:
    print(a)
else:
    print(-a)

#整数
 0
 1000
 -10
 0xfa2 #16进制

 #浮点数
 1.23
 -0.30
 1.2e5 #120000
 1.2e-5 #0.000012

 #字符串
 "a.,jglg"
 'kakg.,/'
 'a \' a \" a \\'
 '\n' #换行
 '\t' #制表符
 print(r'')  #内部不转义
print(r'''
a \\ \t
b
c
''')#打印多行 ,有 r则不转义

#布尔值
True
False
True and  False
True or False
not True

#空值
None

#变量
int b = 1 #b = 'aa' 会报错

#赋值
a = '1'  # a 指向了 '1'
b = a    # b 指向了 ‘1’
a = '2'  # a 指向了 '2'

#运算符号
10/3    #3.3333
9/3     #3.0
10//3   #3
10%3    #

#字符串和编码
ord('a') #显示整数
chr(66) #显示字符
'\u4e2d\u6587' #16进制写中文

b'ABC' #byte类型的数据
‘abc’.encode('ascii')
'中文'.encode('utf-8')
#'中文'.encode('ascii')  会报错

 b'ABC'.decode('ascii')
 b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

 len(b'ABC')#长度
 len(b'\xe4\xb8\xad\xe6\x96\x87')
 len('中文'.encode('utf-8'))
 '中文'# -*- coding: utf-8 -*-  #按照utf-8读取，一般文件头也写

#格式化字符串
'hi, %sdasb %d%%'%(11,123)
%d 整数
%f 浮点数
%s 字符串
%x 十六进制整数
%% %显示

## List
list =  [1,'a',b'c']
list[0]
list[1]
list[-1] #倒数第一个
list[-2] #倒数第二个
list.append('adf') #List 是有序的，可以直接添加后续
list.insert(3,'3') #插入数据操作
list.pop() #删除最后一个数据
list[2] = 'a' #替换数据
list.append(['a',2,3]) # List 数据里面可是List
len(list)  #获取list长度

#tuple
t = ('a','2',[2,1])#tuple 使用（）来定义数据，一旦定义了，指向的地址不可改变
t[2][0] = 2 #即我想说的是： 它指向的可变list 还是可以改变的

t = (2) --> t=2 #这个时候会有歧义，计算机认为 这是在运算符（），这个t是int数据，可变
t = (2,)   #定义为tuple类型，需要添加个，来区分

#条件语句
a = 0;
if a>0:
    print("1:%s" %(a))
elif a<-2:
    print("2:%s" %(a))
else:
    print("3:%s" %(a))
    print("end") #in判断语句
print("end2")#out判断语句

a = input("num :")
b = int(a)

#循环
for a in ["a","b","c","d"]:
    print(a)

range(110)
list(range(5)) #罗列0<= x<5的数字

sum = 0
n=10
while(n>0):
    if n==8:
        n -= 2
        continue
    sum += n
    print("n: %s" %(n))
    n = n-2
    if n==2:
        break
    #按照空格，这个注释在循环里面
print(sum)

#使用dict 和 set
d = {'a':1,'b':2,'c':'c','d':'d',1:'e'}
print(d['a'])
##  d[2] 会报错
2 in d # 返回false，避免方法一
d.get(2, None) #调用方法get，返回默认None，避免方法二

#删除dict
d.pop('a')

list(d) #只返回关键字 kye
# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

#set key的集合，不会存在重复的key
s = set([1,2,3,2])

#论 string 的 不可变  和 list的可变性
a = 'abc'
a = a.replace('a', 'A') #如果不赋值，那么 结果是 ‘Abc’，但是 a的值没有变化

a = ['c','b','a']
a.sort()  #排序 变成  ['a','b','c']
