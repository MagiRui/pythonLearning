#encoding=utf8
__author__ = 'Administrator'

"""
数据库查询操作
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall():接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
"""

import MySQLdb;


db = MySQLdb.connect("localhost","testuser","test123","TESTDB");

cursor = db.cursor();

sql = "select * from employee \
        where income > '%d' " %(1000)

try:
    cursor.execute(sql);
    # 获取所有记录列表
    results = cursor.fetchall();

    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex=row[3]
        income=row[4]
        print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" %\
              (fname,lname,age,sex,income)
except:
    print "Error: unable to fetch data"

db.close()