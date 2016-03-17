#encoding=utf8
__author__ = 'Administrator'

letter = raw_input("Please input")
if letter == 'S':
    print('Please input secode letter:')
    letter = raw_input("Please input:")
    if letter == 'a':
        print ('Saturday')
    elif letter =='u':
        print ("Sunday")
    else:
        print ('Data Error')
elif letter == 'F':
    print("Friday")
elif letter =='M':
    print ("Monday")
elif letter == "T":
    print ("Please input second letter")
    leter = raw_input("please input:")
    if letter == 'u':
        print("Tuesday")
    elif letter == 'h':
        print("Thursday")
    else:
        print ("Data error")
elif letter == 'W':
    print ("Wendesday")
else:
    print ("Data error")
