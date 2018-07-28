#!/usr/bin/env python3
#linux使用，window忽略
# -*- coding: utf-8 -*-

#面向对象编程
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name,self.score))


bart = Student('Bart Simpson',79)
lisa = Student('lisa Simpson',29)
bart.print_score();
lisa.print_score();


#类和实例
#关键字  类名    父类‘object’
class Student(object):
    pass

_name 是私有变量，在python编译中会将其改变名称，无法直接使用（可能编程_Student_name)
使用 __name 后 外部无法直接修改该变量名称了


#继承和堕胎
和java的继承/多态一样。

调用的时候， 不一定非要继承父类，只要定义了一样的方法供调用即可


#判断类型
isinstance(a,list)


#获取对象信息
type(123) == types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType
type((x for x in range(10)))==types.GeneratorType
isinstance(h, Dog)

#获取一个对象的所有属性和方法，使用dir()
dir("abc")
配合 三个方法一起使用：getattr()、setattr()以及hasattr()
hasattr(object,'x')
getattr(object,'x')
getattr(a,'x',"default")
setattr(object,'x',19)


#实例属性和类属性
名称相同时，
实例属性会 覆盖类属性，
但当删除掉实例属性的时候，会访问到类属性
