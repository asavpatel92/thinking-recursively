#===============================================================================
# this function finds GCD for the given pair of integers
#===============================================================================

def findGCD(a,b):
    if ( a == b):
        return a
    elif (a > b):
        return findGCD(a - b, b)
    else:
        return findGCD(a, b-a)
    

if __name__ == '__main__':
    a = int(raw_input("Insert first number:"))
    b = int(raw_input("Insert second number:"))
    print findGCD(a,b)
