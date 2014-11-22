#===============================================================================
#     this function gives you power of given integer in O(logn) complexity
#===============================================================================

def power(number, exponent):
    if(exponent == 0):
        return 1
    elif (exponent == 1):
        return number
    else:
        if(exponent % 2 == 0):
            return power(number, exponent / 2 ) * power(number, exponent / 2)
        else:
            return number * power(number, (exponent-1) / 2 ) * power(number, (exponent-1) / 2) 
        

if __name__ == '__main__':
    number = int(raw_input("Enter the number:"))
    exponent = int(raw_input("Enter the exponent:"))
    print power(number, exponent)