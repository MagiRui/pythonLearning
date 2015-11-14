# encoding=utf-8
__author__ = 'Administrator'

"""
键必须独一无二，但值则不必。
值可以取任何数据类型，但必须是不可变的，如字符串，数或元组。
"""

dict1={'Name':'Zara','Age':7,'Class':'First'}
print "dict1['Name']= ",dict1['Name']
print "dict1['Age']=",dict1['Age']

dict1['Age'] = 8;
dict1['School']="DPS School"

print "dict1['Age']:",dict1['Age']
print "dict1['School']:",dict1['School']

dict2=dict1

print dict1
print dict2

del dict2['Name']
print dict2

del dict2

#print dict2

dict3={['Name']:'Zara','Age':7}
print dict3



