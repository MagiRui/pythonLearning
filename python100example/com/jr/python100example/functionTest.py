#encoding=utf8
__author__ = 'Administrator'

def hello_word():
    print 'Hello World'


def three_hellos():
    for i in range(3):
        hello_word()

if __name__ == '__main__':
    three_hellos()

