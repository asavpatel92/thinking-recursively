#===============================================================================
# this function gives square of the given integer by computing squares of the previous integer --> square(N) = square(N-1) + N + (N-1)
#===============================================================================

def square(number):
    if (number == 0):
        return 0
    elif (number == 1):
        return 1
    else:
        return number + (number - 1) + square(number-1)

if __name__ == '__main__':
    number = int(raw_input("Enter the number:"))
    print square(number)
