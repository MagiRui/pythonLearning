#encoding=utf8
__author__ = 'Administrator'

"""
empCount变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用Employee.empCount访问。
第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
"""
class Employee:
    "所有员工的基类"
    empCount = 0

    def __init__(self,name,salary):
        self.name = name;
        self.salary = salary;
        Employee.empCount +=1;


    def displayCount(self):
        print "Total Employee %d " %Employee.empCount


    def displayEmployee(self):
        print "Name : ",self.name, ", Salary: ",self.salary

emp1 = Employee("Zara",2000)
emp2 = Employee("Manni",500)

emp1.displayEmployee();
emp2.displayEmployee();

print "Total Employee %d " % Employee.empCount

"""
你可以添加，删除，修改类的属性，如下所示：
"""
emp1.age = 7;
emp1.age = 8
emp1.displayEmployee()
del emp1.age;

"""
你也可以使用以下函数的方式来访问属性：
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
"""

emp1.age=27
print "Object Emp1 has age attribute?",hasattr(emp1,"age")
print "Object Emp1 Current attribute value ",getattr(emp1,"age")
print "Object Emp1 new attribute",setattr(emp1,"age",19),emp1.displayEmployee()
delattr(emp1,"age")

"""
Python内置类属性
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了以个由所有父类组成的元组）
"""

print "Employee.__doc__:",Employee.__doc__
print "Employee.__module__:",Employee.__module__
print "Employee.__dict__",Employee.__dict__

