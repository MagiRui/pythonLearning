#encoding=utf8
__author__ = 'Administrator'

import MySQLdb

db = MySQLdb.connect("localhost","testuser","test123","TESTDB");

cursor = db.cursor()

cursor.execute("drop table if exists employee");

sql="""
create table employee (
first_name char(20) not null,
last_name  char(20),
age int,
sex char(1),
income float
)
"""

cursor.execute(sql)

db.close()

