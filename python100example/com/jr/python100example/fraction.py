#encoding=utf8
__author__ = 'Administrator'

a=2.0
b=1.0
s=0

for n in range(1,21):
    s += a/b;
    t = a
    a = a + b
    b = t
print s

"""
reduce()
格式：reduce( func, seq[, init] )
reduce函数即为化简，它是这样一个过程：每次迭代，将上一次的迭代结果（第一次时为init的元素，如没有init则为seq的第一个元素）
与下一个元素一同执行一个二元的func函数。在reduce函数中，init是可选的，如果使用，则作为第一次迭代的第一个元素使用。
简单来说，可以用这样一个形象化的式子来说明：
reduce( func, [1, 2,3] ) = func( func(1, 2), 3)
"""

if __name__ == '__main__':
    a = 2.0
    b = 1.0
    l = []
    for n in range(1,21):
        b,a = a,a+b
        l.append(a/b)
    print reduce(lambda x,y:x+y,l)




