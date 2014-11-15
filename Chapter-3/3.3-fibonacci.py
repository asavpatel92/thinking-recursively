#===============================================================================
# find the fibonacci sequence of the given integer number
#===============================================================================

def fiboSequence(num):
    if(num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return fiboSequence(num-1) + fiboSequence(num -2)


if __name__ == '__main__':
    numValue = int(raw_input("Enter the number:"))
    print "Fibonacci sequence of the given number is" , fiboSequence(numValue)
