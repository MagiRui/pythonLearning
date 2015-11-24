#encoding=utf8
__author__ = 'Administrator'

print "Content-disposition: attachment;filename=\"foo.txt\"\r\n\n";

fo = open("foo.txt","rb")
str=fo.read()
print str;
fo.close()