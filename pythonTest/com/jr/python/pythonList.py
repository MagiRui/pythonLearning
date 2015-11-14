#encoding=utf-8
__author__ = 'Administrator'

list1=["physics","chemistry",1997,2000]

list2=[1,2,3,4,5]

list3= ["a","b","c","d"]

print "list1[0]:",list1[0]
print "list[1:5]:",list2[1:5]

print list1[2]
list1[2]=2001
print list1[2]


print list1
del list1[2]
print list1

print len([1,2,3])
print [1,2,3] + [4,5,6]
print ['Hi']*4
print 3 in [1,2,3]
for x in [1,2,3]:
    print x


L = ['span','Spam','SPAM']
print L[2]
print L[-2]
print L[1:]
