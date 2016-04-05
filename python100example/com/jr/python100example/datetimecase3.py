#encoding=utf8

if __name__ == "__main__":

    import time
    start = time.clock()
    j = 0
    for i in range(10000):
        print i
        j = j + 1
    end = time.clock()
    print "different is %6.3f  %d" %(end-start,j)


