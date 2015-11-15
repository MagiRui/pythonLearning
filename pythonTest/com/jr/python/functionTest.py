#encoding=utf8
__author__ = 'Administrator'

def printme(str):
    "打印任何输入的字符串"
    print str;
    return ;

printme("我要调用自己的函数！")
printme("再调一次");


def changeme(mylist):
    "修改传入的里列表"
    mylist.append([1,2,3,4]);
    print "函数内取值：", mylist
    return

#所有参数（自变量）在Python里都是按引用传递。如果你在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了
mylist=[10,20,30]
changeme(mylist)
print "外函数取值：",mylist,mylist[3][0]

#必备参数
def printStr(str):
    print str;
    return ;

printStr("123");


#命名参数
#命名参数和函数调用关系紧密，调用方用参数的命名确定传入的参数值。
#你可以跳过不传的参数或者乱序传参，因为Python解释器能够用参数名匹配参数值

def printme(str):
    print str;
    return ;

printme(str="My String")


def printInfo(name,age):
    print "Name: " ,name;
    print "Age:",age;
    return ;

printInfo(age=50,name="MiKi")

print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>";

def printInfo(name,age = 35):
    print "Mame:", name
    print "Age:",age
    return ;


printInfo(name="JiangRui")

#不定长参数
#def functionname([formal_args,] *var_args_tuple):

def printInfo(arg1,*vartuple):
    "打印任何传入的参数"
    print "输出:";
    print arg1
    for var in vartuple:
        print var
    return ;

printInfo(10);
printInfo(70,60,50,40,30)

#匿名函数
#python 使用 lambda 来创建匿名函数。
#lambda只是一个表达式，函数体比def简单很多。
#lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
#lambda函数拥有自己的名字空间，且不能访问自有参数列表之外或全局名字空间里的参数。
#虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
#lambda [arg1 [,arg2,.....argn]]:expression

sum=lambda arg1,arg2:arg1 + arg2
print "相加后的值为: " ,sum(10,20)
print "相加后的值为：" ,sum(20,20)


def sum(arg1,arg2):
    total = arg1 + arg2;
    print "函数内：",total
    return total;

total = sum(50,50)
print "函数外:",total


#变量作用域
#一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。
#变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：
#全局变量
#局部变量
#变量和局部变量
#定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
#局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。



total = 0
def sum(arg1,arg2):
    total = arg1 + arg2;
    print "函数内是局部变量：",total
    return total;

sum(10,20)
print "函数外是全局变量:" ,total
