#!/usr/bin/env python 
# -*- coding:utf-8 -*-r

# 一、见枫的Python学习Day1

#         1.书籍参考：主：《Python编程快速上手——让繁琐的工作自动化》 辅：《Python编程：从入门到实践》、菜鸟教程
#         2.编程IDE：Pycharm

# 二、学习要求：(在第三部分练习代码实操中并未完全体现，但大部分都会接触到，以主要参考书籍的学习为准)

#     1.环境搭建
#         anaconda环境配置
#         解释器
#     ---------------------------
#     2.python初体验
#         print and input
#     ---------------------------
#     3.python基础讲解
#         python变量特性+命名规则
#         注释方法
#         python中“：”作用
#         学会使用dir( )及和help( )
#         import使用
#         pep8介绍
#     ---------------------------
#     4.python数值基本知识
#         python中数值类型，int，float，bool，e记法等
#         算数运算符
#         逻辑运算符
#         成员运算符
#         身份运算符
#         运算符优先级
#     ---------------------------
#     5.string字符串
#         定义及基本操作（+，*，读取方式）
#         字符串相关方法
#         字符串格式化问题
#     ------------------------------------------------------------------------------------
#     【作业】
#         学习代码分享，200-300行要求。
#         作业：要求用户依次输入姓名，性别，年龄，并对用户信息进行输出格式如下：您的姓名是：***，您的性别是：***，您是***年出生的。
#     ------------------------------------------------------------------------------------


# 三、练习代码实操：(练习顺序按照《Python编程快速上手——让繁琐的工作自动化》为准)
# 1.print和input部分

print("hello,python world!")  # 入门Python的第一行代码，打印文本

name=input('Please input your name:\n')     # input函数的使用,input()函数总是返回字符串，即使你输入的是数字
print(name)     #
print('It\'s good to see you '+name)
print('The length of your name is: ')       # len()函数的使用
print(len(name))

print('I\'m ' + str(21) +' years old')      # 若要连接数字和字符串需使用str()函数，也不能用赋值后的变量

print("What is your age?")
MyAge=input()
# print('My age is '+str(int(MyAge)+1)+' in a year!')     # 使用int(MyAge)来返回字符串的整数值

# 2.控制流

# Python变量特性+命名规则
'''
1．只能是一个词。
2．只能包含字母、数字和下划线。
3．不能以数字开头。

注：虽然Python一般命名采用PEP8，但是采用驼峰命名法会是的变量看起来更加的直观，如：LookLikeThis，而不是look-like-this
'''

# 注释方法：单行注释用:#，多行注释为:'''xxx'''，或者"""xxx"""，在Pycharm中可以使用“Ctrl+/”进行快速注释

'''
各类运算符参考菜鸟教程中： http://www.runoob.com/python/python-operators.html#ysf4
'''

spam=True                        # 布尔值可以保存在变量中，但是不可以用做变量名
print(spam)

42==42                           # 在比较操作符中，比如像：==或者！=所返回的值都是布尔值(<=和>=也是如此)
42 == 99
2 != 3
'hello' == 'hello'
'hello' == 'Hello'
'dog' != 'cat'
True == True
True != False
42 == 42.0                       # 整形、浮点型永远不会和字符串相等
42 == '42'

'''
注意：
==操作符（等于）问两个值是否彼此相同。
=操作符（赋值）将右边的值放到左边的变量中
'''

True and True                    # 比较运算符(也叫关系运算符)
False and False
not True

'''
Python的赋值运算符和其他编程语言的类似，加减乘除不再赘述，但是取余，幂赋值和整除较易出错，所以记录下来
'''
a = 21
b = 10
c = 2
c %= a                           # 取余,等效于c=c%a
print("5-c的值为：",c)
c **= a                          # 幂赋值,等效于c=c**a
print("6-c的值为：",c)
c //= a                          # 整除,c=c//a
print("7-c的值为：",c)

a=10                               # 逻辑运算符，所有的非零常数都是True，字符串则判定为非空值为True，如果
b=20
if a and b:                        # 如果判定语句为真，则打印'a,b为True',否则返回'a,b有一个不为TRUE'
    print('a,b为True')
else:
    print('a,b有一个不为TRUE')

a=0                                # 在a,b都为0时判定为FALSE
b=0
if a or b:
    print('a,b为True')
else:
    print('a,b有一个不为TRUE')


a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):                     # 成员运算符,一般用于列表
    print("a在list中")
else:
    print("a不在list中")

a=10
b=20
if (a is b):                            # 身份运算符,用于比较两个对象的存储单元
    print('a,b相同')
else:
    print('a,b不同')

'''
运算符优先级:指数 >乘，除，取模和取整除>加法减法>比较运算符>赋值运算符>身份运算符>成员运算符>逻辑运算符
'''

# 3.字符串string
py='Hello,Python world!'     # Python中常见的一种数据类型，一般用双引号""或者单引号''去创建
# 转义字符，在C中学习过，不再赘述
'''
\\	反斜杠符号
\'	单引号
\"	双引号
\a	响铃
\b	退格(Backspace)
\e	转义
\000	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
'''

# Python字符串运算符
a="Hello"
b="Python"
print(a+b)                  # +为字符串连接
print(2*a)                  # *重复输出字符串
print(a[1])                 # []通过索引获取字符串中字符,注意是从前索引为0开始，从后索引为-1开始
print(a[1:5])               # [:]截取字符串中的一部分，冒号"："前后的数字可以理解为"围墙"

# 格式化
# print("My name is %s and weight is %d kg!" % ('jianfeng', 50) #
'''
在C中已经接触过，不再赘述

%c	 格式化字符及其ASCII码
%s	 格式化字符串
%d	 格式化整数
%u	 格式化无符号整型
%o	 格式化无符号八进制数
%x	 格式化无符号十六进制数
%X	 格式化无符号十六进制数（大写）
%f	 格式化浮点数字，可指定小数点后的精度
%e	 用科学计数法格式化浮点数
%E	 作用同%e，用科学计数法格式化浮点数
'''

# 4.模块化编程
'''
模块化编程像一个个不同的工具箱，在需要不同的工具时可以将模块导入，并且调入其中的函数
'''
import math     # 导入数学模块
print(math)
print(math.pi)

from math import pi     # 调用模块中的函数
print(pi)

from math import *      # 将模块中的函数全部导入

print(dir(math))          # dir()函数，查询一个模块里定义的所有模块，变量和函数
print(help(math))         # help()函数，用来解释说明
'''
比如math模块中，特殊字符串变量__name__指向模块的名字，__file__指向该模块的导入文件名
'''

# 四、作业代码

# Name=input('您的姓名是：')
# Sex=input('您的性别是：')
# Birth=input('您的出生日期是：')
# print('您的姓名是：',Name)
# print('您的性别是：',Sex)
# print('您的出生日期是：',Birth)

