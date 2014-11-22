 #==============================================================================
 # function to find the different arrangements possible using smaller number of letters
 #==============================================================================
 
def permutations(letters, wordLength):
    if(wordLength < letters):
        if (wordLength == 1):
            return letters
        else:
            return letters * permutations(letters - 1, wordLength - 1)
    else:
        return "Wordlength can not be greater than no of available letters"
     
if __name__ == '__main__':
    letters = int(raw_input("Enter the no of letters:"))
    wordLength = int(raw_input("Enter the length of word:"))
    print permutations(letters, wordLength) 

 
