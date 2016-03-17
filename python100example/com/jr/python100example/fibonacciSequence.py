#encoding=utf8
__author__ = 'Administrator'

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a;

print fib(10)
