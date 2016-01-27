#encoding=utf8
__author__ = 'Administrator'

import cgi,cgitb

"""
<form action="/cgi-bin/dropdown.py" method="post" target="_blank">
    <select name="dropdown">
        <option value="Maths" selected>Maths</option>
        <option value="Physics">Physics</option>
    </select>
    <input type="submit" value="Submit"/>
</form>
"""

form = cgi.FieldStorage

if form.getvalue('dropdown'):
    subject = form.getvalue("dropdown");
else:
    subject = "Not Entered";

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Dropdown Box - Sixth CGI Program</title>"
print "</head>"
print "<body>"
print "<h2> Selected Subject is %s</h2>" % subject
print "</body>"
print "</html>"



