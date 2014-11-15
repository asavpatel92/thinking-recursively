#===============================================================================
# find the factorial of the given integer
#===============================================================================

def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num-1)

if __name__ == '__main__':
    print "Factorial of given number is" , factorial(9)