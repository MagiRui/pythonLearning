#encoding=utf8
__author__ = 'Administrator'

import datetime

"""
当你打开一个.py文件时,经常会在代码的最下面看到if __name__ == '__main__':,现在就来介 绍一下它的作用.
模块是对象，并且所有的模块都有一个内置属性 __name__。一个模块的 __name__ 的值取决于您如何应用模块。
如果 import 一个模块，那么模块__name__ 的值通常为模块文件名，不带路径或者文件扩展名。但是您也可以像
一个标准的程序样直接运行模块，在这 种情况下, __name__ 的值将是一个特别缺省"__main__"。

在cmd 中直接运行.py文件,则__name__的值是'__main__';
而在import 一个.py文件后,__name__的值就不是'__main__'了;
从而用if __name__ == '__main__'来判断是否是在直接运行该.py文件

__name__ == "__main__"
这个表示执行的是此代码所在的文件。 如果这个文件是作为模块被其他文件调用，不会执行这里面的代码。
 只有执行这个文件时， if 里面的语句才会被执行。 这个功能经常可以用于进行测试。
"""
if __name__ == "__main__":

   # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
   print(datetime.date.today().strftime("%d/%m/%Y"))

   #创建日期对象
   miyazakiBirthDate = datetime.date(2016,1,28)

   print(miyazakiBirthDate.strftime("%d/%m/%Y"))

   #日期算术运算
   miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
   print(miyazakiBirthNextDay.strftime("%d/%m/%Y"))


   #日期替换
   miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1);
   print(miyazakiFirstBirthday.strftime("%d/%m/%Y"))




