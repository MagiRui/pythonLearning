#encoding=utf-8
__author__ = 'Administrator'


"""
Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
"""

tup1 =("Physics","Chemistry",1977,2000)
tup2=(1,2,3,4,5)
tup3="a","b","c","d"

#创建空元组
tup4=()

#元组中只包含一个元素时，需要在元素后面添加逗号
tup5=(50,)


print "tup1[0]:",tup1[0]
print "tup2[1:5]",tup2[1:5]

tup6=tup1 + tup2
print "tup6: " ,tup6

#del tup6
print "tup6:",tup6

ps =  'abc',-4.24e93,18+6.6j,'xyz'
x, y=1, 2
print "Value of x,y: ",ps,x,y
print x;
print y;