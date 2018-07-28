#!/usr/bin/env python3
#linux使用，window忽略
# -*- coding: utf-8 -*-

#模块
# 模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。

# 创建自己的模块时，要注意：
# 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
# 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。


#使用模块
'任何模块的第一个字符串均被认为是注释'

__author__ = 'SJD'  #自定义变量，装逼告诉别人 这是谁写的;同时阐明作者

import sys #导入模块
sys.argv


name      # 正常参数，随意使用（public）
__name__  #可以直接使用，但是有特殊用途。
__name    #私有参数，非公开（private)


## 第三方模块
#普通模式
pip install Pillow

#第三方整合模式
Anaconda
