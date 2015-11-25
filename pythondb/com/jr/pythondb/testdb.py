#encoding=utf8
__author__ = 'Administrator'

import MySQLdb

#打开数据库连接
db = MySQLdb.connect("localhost","testuser","test123","TESTDB")

#使用Cursor()方法获取操作游标
cursor=db.cursor()

#使用execute方法执行sql
cursor.execute("SELECT VERSION()")

#使用fetchone()方法获取一条数据库
data=cursor.fetchone()

print "Database version: %s " %data

db.close()

