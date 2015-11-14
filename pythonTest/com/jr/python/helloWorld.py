#coding=utf-8
__author__ = 'Administrator'

print "你好,世界！";

counter=100
miles=1000.95
name="JR"

print counter
print miles
print name

a,b,c=1,2,"JR"

print a
print b
print c

s="Ilovepython"
print s[0];
print s[1:5];
print s[5:]
print s*2;

list=['abc',786,2.23,"JR",70.2]
tinylist=[123,"JR"]

print list;
print list[0]
print list[2:3]
print list[3:]
print tinylist * 2
print list + tinylist

list[1] = 796
print  " >>>>>>>>>>> "
print list[1]
print  " >>>>>>>>>>> "
print list;
list = tinylist
print list;

tuple=("abcd",786,2.23,"john",70.2);
tinytuple=(345,'john'
           );

print tuple
print tinytuple


print tuple[1:3]
print tuple[2]
print tinytuple *2
print tuple + tinytuple

'''tuple[1] = 796'''
print  " >>>>>>>>>>> "
print tuple[1]
print  " >>>>>>>>>>> "
print tuple;


tuple = tinytuple
print tuple


dict={}
dict['one']="This is one"
dict[2]="This is two"

tinydict = {"name":"John","code":6734,"dept":"sales"}

print "<<<<<<<<<<<<<<<<<<dict>>>>>>>>>>>>>>>>>>>>>>"
print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()

print "<<<<<<<<<<<<<<<<<<运算符>>>>>>>>>>>>>>>>>>>>>>"
print 9/2


print "<<<<<<<<<<<<<<<python成员运算符>>>>>>>>>>>>>>>>"
a=10
b=20
list = [1,2,3,4,5];
if (a in list):
    print "Line 1 -a is available in the given list"
else:
    print "Line 1 -a is not available in the given list"

if(b not in list):
    print "Line 2 -b is not available in the given list"
else:
    print "Line 2 -b is  available in the given list"

a=2
if(a in list ):
    print "Line 3 -a is available in the given list"
else:
    print "Line 3 -a is not available in the given list"


print "<<<<<<<<<<<<<<<<<Python身份运算符>>>>>>>>>>>>>>>>"

a=20
b=20
if ( a is b ):
    print "Line 4 - a and b have same identity"
else:
    print "Line 4 - a and b do not have same identity"


if (id(a) ==id(b)):
    print "Line 5 - a and b have same identity"
else:
    print "Line 5 - a and b do not have same identity"

b=30
if ( a is b ):
    print "Line 6 - a and b have same identity"
else:
    print "Line 6 - a and b do not have same identity"

if ( a is not b ):
    print "Line 7 - a and b do not have same identity"
else:
    print "Line 7 - a and b have same identity"


print "<<<<<<<<<<Python for循环>>>>>>>>>>";
for letter in "Python":
    print "当前字母: " ,letter

fruits=["banana","apple","mango"]
for fruit in fruits:
    print "当前水果味:",fruit

for index in range(len(fruits)):
    print "当前水果：",fruits[index],index,len(fruits),range(len(fruits))



for num in range(10,20):
    for i in range(2,num):
        if  num % i ==0:
            j=num/i;
            print "%d 等于 %d * %d " %(num,i,j)
            break;
    else:
        print num,"是一个质数"










