#encoding=utf8
__author__ = 'Administrator'

"""
CGI(Common Gateway Interface),通用网关接口,它是一段程序,运行在服务器上如：HTTP服务器，提供同客户端HTML页面的接口。
"""

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<tittle>Hello World -First CGI Program</tittle>'
print '</head>'
print '<body>'
print '<h2>Hello World! This is my first CGI program</h2>'
print '</body>'
print '</html>'