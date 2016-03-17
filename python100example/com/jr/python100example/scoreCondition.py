#encoding=utf8
__author__ = 'Administrator'

score = int(raw_input("Please input score:\n"))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = "C"

print "%d belongs to %s " %(score,grade)
