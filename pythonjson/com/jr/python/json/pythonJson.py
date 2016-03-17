#encoding=utf-8
__author__ = 'Administrator'
import demjson

"""
需要先安装JSON模块,Demjson
JSON           函数
函数	        描述
encode	   将 Python 对象编码成 JSON 字符串
decode	   将已编码的 JSON 字符串解码为 Python 对象
"""

"""
encode
Python encode()函数用于将Python对象编码成JSON字符串
demjson.encode(self, obj, nest_level=0)
"""

data = [{'a':1,'b':2,'c':3,'d':4,'e':5}]

json = demjson.encode(data)
print json


"""
decode
Python可以使用demjson.decode()函数解码JSON数据。该
函数返回Python字段的数据类型
语法: demjson.decode(self,txt)
"""

text = demjson.decode(json);
print text;