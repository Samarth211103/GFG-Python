def pos(n):
    ## Write the code
    if n >= 0:
        if n == 0:
            return 'already zero'
        else:
            n -= 1
            while n >= 0:
                print(n, end = ' ')
                n -= 1
    
def neg(n):
    ##Write the code
    if n < 0:
        while n <= 0:
            print(n, end = ' ')
            n += 1