#encoding=utf8
__author__ = 'Administrator'

"""
基础重载方法
下表列出了一些通用的功能，你可以在自己的类重写：
__init__ ( self [,args...] )
构造函数
简单的调用方法: obj = className(args)
__del__( self )
析构方法, 删除一个对象
简单的调用方法 : dell obj
__repr__( self )
转化为供解释器读取的形式
简单的调用方法 : repr(obj)
__str__( self )
用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)
__cmp__ ( self, x )
对象比较
简单的调用方法 : cmp(obj, x)
"""

class Vector:

    def __init__(self,a,b):
        self.a =a;
        self.b=b;

    def __str__(self):
        return "Vector (%d,%d)" %(self.a,self.b)

    def __add__(self, other):
        return Vector(self.a + other.a,self.b + other.b)


v1 = Vector(2,10)
v2 = Vector(5,-2)

print v1 + v2


"""
类属性与方法
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
类的方法
在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数
类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods
"""

class JustCounter:
    __secretCount = 0;
    publicCount = 0 ;

    def count(self):
        self.__secretCount += 1;
        self.publicCount += 1
        print self.__secretCount


counter = JustCounter()
counter.count();
counter.count();
print counter.publicCount

"""
Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性
"""
print counter._JustCounter__secretCount


