#encoding=utf-8
__author__ = 'Administrator'

"""
>>> range(1,5) #代表从1到5(不包含5)
[1, 2, 3, 4]
>>> range(1,5,2) #代表从1到5，间隔2(不包含5)
[1, 3]
>>> range(5) #代表从0到5(不包含5)
[0, 1, 2, 3, 4]
"""
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (j!=k) and (i!=k):
                print i,j,k

