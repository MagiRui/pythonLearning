#encoding=utf8

if __name__ == "__main__":

    from sys import stdout
    #filename = raw_input("input a file name :\n")
    fp = open("everyWordAndWrite.txt","w")
    ch = raw_input("input string:\n")
    while ch != "#":
        fp.write(ch);
        stdout.write(ch)
        ch=raw_input("")
    fp.close()

