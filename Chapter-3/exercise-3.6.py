#===============================================================================
# find the no of combinations of given letters and wordlength
#===============================================================================

def combination(letters, wordLength):
    if( wordLength == 0 or wordLength ==  letters ):
        return 1
    else:
        return combination(letters - 1, wordLength-1) + combination(letters - 1, wordLength)    

if __name__ == '__main__':
    letters = int(raw_input("Enter the no of letters:"))
    wordLength = int(raw_input("Enter the wordlength:"))
    print combination(letters, wordLength)