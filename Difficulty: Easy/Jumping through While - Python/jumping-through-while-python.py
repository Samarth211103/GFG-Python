def printIncreasingPower(x):
    #code here
    y = 1
    # Loop to jump in powers of 2
    while(y <= x):
        #code here
        i = y ** 2
        if i <= x:
            print (i , end = " ")
        y += 1
        #code here