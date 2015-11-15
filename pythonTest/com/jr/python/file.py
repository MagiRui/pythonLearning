#encoding=utf8
__author__ = 'Administrator'

import os;

#open函数
#你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的辅助方法才可以调用它进行读写。
#语法：
#file object = open(file_name [, access_mode][, buffering])

fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
fo.write( "Python is a great language.\nYeah its great!!\n");
fo.close()

fo1 = open("foo.txt", "r+")
str = fo1.read(10);
print "文件的内容是：",str
fo1.close()


#重命名和删除文件
#Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。
#要使用这个模块，你必须先导入它，然后可以调用相关的各种功能。
#rename()方法：
#rename()方法需要两个参数，当前的文件名和新文件名。