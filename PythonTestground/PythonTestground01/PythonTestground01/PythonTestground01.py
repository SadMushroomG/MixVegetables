# �C coding: gbk �C

from ast import Str


counter = 100       #���ͱ���
miles   = 100.0     #�����ͱ���
name    = "Amoeba"  #�ַ���

a = b = c = 1
a, b, c = 1, 2.0, "Amoeba"

"""
��׼�������ͣ�
�ɱ����ݣ�
Number      ����
String      �ַ���
List        �б�
���ɱ����ݣ�
Tuple       Ԫ��
Set         ����
Dictionary  �ֵ�
"""

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
#type()         ������Ϊ������һ�ָ�������
#isinstance()   ����Ϊ������һ�ָ�������
print(isinstance(a,  int))
#Python3��bool��int�����࣬True��False���Ժ��������
print(issubclass(bool, int))
print(True == 1)
print(True + 1)

"""
5 + 4       �ӷ� 
4.3  - 1    ����
3 *7        �˷�
2 / 4       ����
17 % 3      ȡ��
2  ** 5     �˷�
""" 
print("1/2 = " , 1/2)
print("1//2 = ", 1//2) #����һ������

str = "Ambrosia"
print(str)

print("str[0:-1]", str[0:-1])
print("str[0]", str[0])
print("str[2:5]", str[2:5])
print("str[2:]", str[2:])
print("str * 2", str * 2)
print("str + \"Test\"", str + "Test")

#ȡ��ת��
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