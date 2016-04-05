#encoding=utf8

testList = [100086,"中国移动",[1,2,3,4,5]]

#列表的长度
print "列表的长度 %d" %len(testList)

#到列表尾
print "到列表尾部", testList[1:]

#向列表添加元素
testList.append("I'm new here!")

print "新列表的长度 %d" %len(testList)
print "到列表尾部", testList[1:]

#弹出列表的最后一个元素
print testList.pop(1)
print "新列表的长度 %d" %len(testList)
print "列表所有元素", testList


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print matrix
print matrix[1]

col2 = [row[1] for row in matrix]
print col2

col2even = [row[1] for row in matrix if row[1] % 2 == 0]
print col2even

print matrix[1]








