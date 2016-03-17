#encoding=utf8
__author__ = 'Administrator'

n = 0
s = 0
t = 1

for n in range(1,21):
     t *= n
     s += t
print '1! + 2! + 3! + ... + 20! = %d' % s


"""
其实sum()的参数是一个list
例如：
sum([1,2,3])

MapReduce的设计灵感来自于函数式编程，这里不打算提MapReduce，就拿python中的map()函数来学习一下。

文档中的介绍在这里：

map(function, iterable, ...)
Apply function to every item of iterable and return a list of the results.
If additional iterable arguments are passed, function must take that many
arguments and is applied to the items from all iterables in parallel. If one
iterable is shorter than another it is assumed to be extended withNoneitems.
If function isNone, the identity function is assumed; if there are multiple
arguments, map() returns a list consisting of tuples containing the corresponding
items from all iterables (a kind of transpose operation). The iterable arguments
may be a sequence or any iterable object; the result is always a list.

1、对可迭代函数'iterable'中的每一个元素应用‘function’方法，将结果作为list返回。
2、如果给出了额外的可迭代参数，则对每个可迭代参数中的元素‘并行’的应用‘function’。（翻译的不好，这里的关键是‘并行’）
>>> def abc(a, b, c):
...     return a*10000 + b*100 + c
...
>>> list1 = [11,22,33]
>>> list2 = [44,55,66]
>>> list3 = [77,88,99]
>>> map(abc,list1,list2,list3)
[114477, 225588, 336699]
"""
s=0
l=range(1,21)
def op(x):
    r = 1
    for i in range(1,x+1):
        r *= i
    return r
s = sum(map(op,l))
print "1! + 2! + 3! + ... + 20! = %d" %s



