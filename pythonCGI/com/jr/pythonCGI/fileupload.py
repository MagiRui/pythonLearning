#encoding=utf8
__author__ = 'Administrator'

"""
<html>
<body>
   <form enctype="multipart/form-data"
                     action="save_file.py" method="post">
   <p>File: <input type="file" name="filename" /></p>
   <p><input type="submit" value="Upload" /></p>
   </form>
</body>
</html>
"""

import cgi,os
import cgitb;cgitb.enable()


form = cgi.FieldStorage;

#获取文件名
fileitem = form['filename']
#检测文件是否上传

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    open("/tmp" + fn,'wb').write(fileitem.file.read);
    message = 'The file "' + fn + ' " was uploaded successfully'

else:
    message = "No file was uploaded";

print """\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,)

"""
如果你使用的系统是Unix/Linux，你必须替换文件分隔符，在window下只需要使用open()语句即可：
fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
"""