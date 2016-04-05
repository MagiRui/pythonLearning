#encoding=utf8

if __name__ == "__main__":

    fp = open("inputWordWriteFile.txt","w")
    string = raw_input("please input a string:\n")
    fp.write(string.upper())
    fp = open("inputWordWriteFile.txt","r")
    print fp.read()
    fp.close()