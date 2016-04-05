#encoding=utf8

if __name__ == "__main__":
    import time

    start = time.time()
    for i in range(3000):
        print i
    end = time.time()

    print end-start;


    print time.ctime(time.time())
    print time.asctime(time.localtime(time.time()))
    print time.asctime(time.gmtime(time.time()))