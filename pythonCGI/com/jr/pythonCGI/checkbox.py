#encoding=utf8
__author__ = 'Administrator'

import cgi,cgitb
"""
checkbox用于提交一个或者多个选项数据
<form action="/cgi-bin/checkbox.cgi" method="POST" target="_blank">
    <input type="checkbox" name="maths" value="on" /> Maths
    <input type="checkbox" name="physics" value="on" /> Physics
    <input type="submit" value="Select Subject" />
</form>
"""

form = cgi.FieldStorage;

if form.getvalue("maths"):
    math_flag = "ON";
else:
    math_flag = "OFF";

if form.getvalue('physics'):
    physics_flag="ON"
else:
    physics_flag="OFF"

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Checkbox - Third CGI Program</title>"
print "</head>"
print "<body>"
print "<h2> CheckBox Maths is: %s</h2>" %math_flag
print "<h2> CheckBox Maths is: %s</h2>" %physics_flag
print "</body>"
print "</html>"








