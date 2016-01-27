#encoding=utf8
__author__ = 'Administrator'

import  MySQLdb

db = MySQLdb.connect("localhost","testuser","test123","TESTDB")

cursor = db.cursor();

sql = "insert into employee(first_name,last_name,age,sex,income) values ('%s','%s','%d','%c','%d')" %('Mac','Mohan',20,'M',2000)


try:
    cursor.execute(sql);
    db.commit();
except:
    db.rollback();

db.close()
