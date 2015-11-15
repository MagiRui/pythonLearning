#encoding=utf8
__author__ = 'Administrator'

#import 语句
#想使用Python源文件，只需在另一个源文件里执行import语句，语法如下：
#import module1[, module2[,... moduleN]

#From…import 语句
#Python的from语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
#from modname import name1[, name2[, ... nameN]]
#例如，要导入模块fib的fibonacci函数，使用如下语句：
#from fib import fibonacci
#这个声明不会把整个fib模块导入到当前的命名空间中，它只会将fib里的fibonacci单个引入到执行这个声明的模块的全局符号表。

#From…import* 语句
#把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
#from modname import *
#这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。

print ">>>>>>>>>>>全局变量加Global>>>>>>>>>>>>>>>>"
Money = 2000
def addMoney():
    global Money
    Money = Money + 5000

print Money
addMoney()
print Money




