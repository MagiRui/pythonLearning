#encoding=utf8
__author__ = 'Administrator'

"""
对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。
commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。
"""

import MySQLdb

def printResutls(results):

    for result in results:
         print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" %\
              (result[0],result[1],result[2],result[3],result[4])

    return 0;

def queryEmployee(db):
    querySql = "select * from employee "
    try:
        cursor = db.cursor()
        cursor.execute(querySql)
        results = cursor.fetchall();
        printResutls(results)
    except:
        print "Query Error "


db = MySQLdb.connect("localhost","test","test123","TESTDB")

print "Before update---------------------"
queryEmployee(db)

cursor = db.cursor()
sql = "update employee set age = age + 1 \
       where sex='%c'" %('M')
try:
    cursor.execute(sql);
    db.commit()
except:
    db.rollback()

print "After update-------------------"
queryEmployee(db)

db.close()






