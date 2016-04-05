#encoding=utf8

if __name__== "__main__":
    import time
    import random

    play_it = raw_input("Do you want to play it.(y or n)")
    while play_it == 'y':
        c = raw_input("Input a character:\n")
        i = random.randint(0,2**32) % 100
        #print "The guess number is %d" %i
        print "Please input a little smaller"
        start = time.clock()
        a=time.time()
        guess =int(raw_input("Input you guess:\n"))
        while guess != i:
            if guess > i:
                print 'Please input a little smaller'
                guess = int(raw_input("Input your guess:\n"))
            else:
                print "Please input a little bigger"
                guess = int(raw_input("Input your guess:\n"))
        end = time.clock()
        b = time.time()
        var = (end-start)/18.2
        print var

        if var < 15:
            print "You are very clerver!"
        elif var < 25:
            print "You are normal!"
        else:
            print "you are stupid!"

        print "Congradulations"
        print "The number you guess is %d" %i
        play_it = raw_input("Do you want to play it.")
