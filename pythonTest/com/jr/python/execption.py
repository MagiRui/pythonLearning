#encoding=utf8
__author__ = 'Administrator'

"""
异常处理
捕捉异常可以使用try/except语句。
try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
如果你不想在异常发生时结束你的程序，只需在try里捕获它。
语法：
以下为简单的try....except...else的语法：
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。
如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印缺省的出错信息）。
如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。
一下语句错误:
try:
finally:
else: 有finally时不能有else子句
"""

try:
    fh = open("testfile","w")
    fh.write("This is my test file for exception handling!!!")
except IOError:
    print "Error: can\'t find file or read data"
else:
    print "Written content in the file successfully"
fh.close()

print "<<<<<<<<<>>>>>>>>>>>>>>>>"
try:
    fh = open("testfile","r")
    fh.write("This is my test file for exception handling!!!")
except:
    print "Except:File not open for writing"
finally:
    print "|||| Error: can\'t find file or read data"
    fh.close()

"""
异常的参数
一个异常可以带上参数，可作为输出的异常信息参数。
你可以通过except语句来捕获异常的参数，如下所示：
try:
   You do your operations here;
   ......................
except ExceptionType, Argument:
   You can print value of Argument here...
变量接收的异常值通常包含在异常的语句中。在元组的表单中变量可以接收一个或者多个值。
元组通常包含错误字符串，错误数字，错误位置。
"""

print "Except Argument "
def temp_convert(var):
    try:
        return int(var)
    except ValueError,xxx:
        print "The argument does not contain numbers\n",xxx

temp_convert("xyz")


"""
触发异常
我们可以使用raise语句自己触发异常
raise语法格式如下：
raise [Exception [, args [, traceback]]]
语句中Exception是异常的类型（例如，NameError）参数是一个异常参数值。
一个异常可以是一个字符串，类或对象。 Python的内核提供的异常，大多数都是实例化的类，这是一个类的实例的参数。
定义一个异常非常简单，如下所示：
"""

print ">>>>>>>>>>>functionName(level)<<<<<<<<<<<<<"
def functionName(level):
    if level < 1:
        raise "Invalid level!",level

"""
一下代码运行提示
TypeError: exceptions must be old-style classes or derived from BaseException, not str
"""

try:
    functionName(0)
except :
   print "the argument level value is Error"
else:
  print "Everything is Passing"


"""
用户自定义异常
通过创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自Exception类，通过直接或间接的方式。
以下为与RuntimeError相关的实例,实例中创建了一个类，基类为RuntimeError，用于在异常触发时输出更多的信息。
在try语句块中，用户自定义的异常后执行except块语句，变量 e 是用于创建Networkerror类的实例。
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
"""

print "<<<<<<<<<<<<<<<用户自定义异常>>>>>>>>>>>>>>>>"
class Networkerror(RuntimeError):
    def __init__(self,arg):
        self.args = arg;


try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args