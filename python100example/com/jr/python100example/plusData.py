#encoding=utf8
__author__ = 'Administrator'

Tn = 0
Sn = []

n = int(raw_input("n=:\n"))
a=  int(raw_input("a=:\n"))

for count in range(n):
    Tn =Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn

Sn = reduce(lambda x,y:x+y,Sn)
print "Total value：%d" %Sn
