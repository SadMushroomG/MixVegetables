# – coding: gbk –

from ast import Str


counter = 100       #整型变量
miles   = 100.0     #浮点型变量
name    = "Amoeba"  #字符串

a = b = c = 1
a, b, c = 1, 2.0, "Amoeba"

"""
标准数据类型：
可变数据：
Number      数字
String      字符串
List        列表
不可变数据：
Tuple       元组
Set         集合
Dictionary  字典
"""

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
#type()         不会认为子类是一种父类类型
#isinstance()   会认为子类是一种父类类型
print(isinstance(a,  int))
#Python3中bool是int的子类，True和False可以和数字相加
print(issubclass(bool, int))
print(True == 1)
print(True + 1)

"""
5 + 4       加法 
4.3  - 1    减法
3 *7        乘法
2 / 4       除法
17 % 3      取余
2  ** 5     乘方
""" 
print("1/2 = " , 1/2)
print("1//2 = ", 1//2) #返回一个整数

str = "Ambrosia"
print(str)

print("str[0:-1]", str[0:-1])
print("str[0]", str[0])
print("str[2:5]", str[2:5])
print("str[2:]", str[2:])
print("str * 2", str * 2)
print("str + \"Test\"", str + "Test")

#取消转义
print("Test\nground")
print(r"Test\nground")

list = ["Ambrosia",123, 55.5, True]
print(list[1:-1])
list[1] = 666
print(list[1:-1])

inputword = "I am Ambrosia"
inputword = inputword[-1::-1]
output = ''.join(inputword)
print(output)