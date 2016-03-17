#encoding=utf8
__author__ = 'Administrator'

def output(s,l):
    if l==0:
        return
    print (s[l-1])
    output(s,l-1)


s = raw_input("Input a String: ")
l = len(s)
output(s,l)
