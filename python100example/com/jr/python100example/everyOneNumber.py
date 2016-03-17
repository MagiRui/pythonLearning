#encoding=utf8
__author__ = 'Administrator'

x = int(raw_input("Input a number:\n"))
a = x / 10000
b = x % 10000/1000
c = x % 1000 / 100
d = x % 100 / 10
e = x % 10

if a != 0:
    print "There are 5 ",e,d,c,b,a
elif b != 0:
    print "There are 4 ",e,d,b,c
elif c != 0:
    print "There are 3 ",e,d,c
elif d != 0 :
    print "There are 2",e,d
else:
    print "There are 1",e