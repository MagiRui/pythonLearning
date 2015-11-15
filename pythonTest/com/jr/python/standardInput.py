#encoding=utf8
__author__ = 'Administrator'

#Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘。如下：
#raw_input
#input
#raw_input函数
#raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：

str = raw_input("Enter your input: ");
print "Received input is: ", str;


#input函数
#input([prompt]) 函数和raw_input([prompt]) 函数基本可以互换，但是input会假设你的输入是一个有效的Python表达式，并返回运算结果。

str2 = input("Enter your input:")
print "Received input is: ",str2
