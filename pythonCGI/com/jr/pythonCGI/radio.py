#encoding=utf8
__author__ = 'Administrator'

import cgi,cgitb

"""
<form action="/cgi-bin/radiobutton.py" method="post" target="_blank">
    <input type="radio" name="subject" value="maths" /> Maths
    <input type="radio" name="subject" value="physics" /> Physics
    <input type="submit" value="Select Subject" />
</form>
"""

form = cgi.FieldStorage

if form.getvalue('subject'):
    subject = form.getvalue("subject")
else:
    subject =  "Not Set";

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Radio - Fourth CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Selected Subject is %s</h2>" %subject
print "</body>"
print "</html>"
