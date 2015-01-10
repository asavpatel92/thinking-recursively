#===============================================================================
# this function generates all possible character string from the input phone number
#===============================================================================
from array import array

def char_from_digit(digit, index):
    if ( digit == 0 or digit == 1):
        return None
    else:
        digit_char_map = { "2":"ABC", "3":"DEF", "4":"GHI", "5":"JKL", "6":"MNO", "7":"PRS", "8":"TUV", "9":"WXY"  }
        return digit_char_map.get(digit)[index]

    
def phone_to_string(phone_no, possible_words, round, temp_word):
    if round == len(phone_no):
        return possible_words.append(''.join(temp_word))
        
    else:
        for i in range(3):
            character = char_from_digit(phone_no[round], i)
            if character != None:
                temp_word[round] = character
            phone_to_string(phone_no, possible_words, round+1, temp_word)            
        
        

def main():
    phone_no = str(raw_input("Enter the number:"))
    possible_words = []
    temp_word = array('c', [' ' for _ in phone_no])
    phone_to_string(phone_no, possible_words, 0, temp_word)
    print possible_words
    
    
if __name__ == "__main__":
    main()