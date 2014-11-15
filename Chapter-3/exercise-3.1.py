#===============================================================================
# power(X,K) this functions raises the real value of X to the K power
#===============================================================================

def power(number, exponent):
    if (exponent == 0):
        return 1
    elif (exponent == 1):
        return number
    else:
        return number * power(number, exponent -1)

if __name__ == '__main__' :
    
    numValue = int(raw_input("Enter the number:"))
    expoValue = int(raw_input("Enter the value of exponent:"))
    print "Power of the given number is" , power(numValue, expoValue)