#encoding=utf8
__author__ = 'Administrator'

import cgi,cgitb

#创建FieldStorage的实例化
"""
/cgi-bin/hello_get.py?first_name=ZARA&last_name=ALI
表单post、get方法都可以用如下代码获取表单的属性值
<form action="/cgi-bin/hello_get.py" method="get">
    First Name: <input type="text" name="first_name"><br/>
    Last Name: <input type="text" name="last_name" />
    <input type="submit" value="Submit" />
</form>
"""
form=cgi.FieldStorage();

first_name=form.getvalue("first_name");
last_name=form.getvalue("last_name");

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</tittle>"
print "</head>"
print "<body>"
print "<h2>Hello %s %s</h2>" %(first_name,last_name)
print "</body>"
print "</html>"


