#encoding=utf8
__author__ = 'Administrator'

if __name__ == '__main__':

    N = 10
    print "Please input ten num:\n"
    l = []
    for i in range(N):
        l.append(int(raw_input("input a number:\n")))
    print

    for i in range(N):
        print l[i]
    print()

    for i in range(N - 1):
        min = i
        for j in range(i+1,N):
            if l[min] > l[j] :
                min= j
        l[i],l[min] = l[min],l[i]
    print "after sorted"
    for i in range(N):
        print l[i]



