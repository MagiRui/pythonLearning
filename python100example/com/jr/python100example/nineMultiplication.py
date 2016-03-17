#encoding=utf8
__author__ = 'Administrator'

for i in range(1,10):
    x = i;
    for j in range(1,10):
        print "%d * %d = %-3d " %(j,x,x*j),
        if j== x:
            print "\n"
            break