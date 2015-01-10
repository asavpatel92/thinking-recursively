#===============================================================================
# this function generates the permutations for given string which has repeating characters  
#===============================================================================

def swapChars(var_string, position1, position2):
    string_list = list(var_string)
    string_list[position1], string_list[position2] = string_list[position2], string_list[position1]
    return ''.join(string_list)

def permute(var_string, start_position):
    if (not isinstance(var_string, str)):
        raise Exception("Input must be string")
    if (start_position == len(var_string)):
        print var_string, "," ,
    else:
        for i in range (start_position, len(var_string)):
            if ( start_position == i):
                var_string = swapChars(var_string, start_position, i)
                permute(var_string, start_position + 1)
            elif (var_string[start_position] != var_string[i]):
                var_string = swapChars(var_string, start_position, i)
                permute(var_string, start_position + 1)
                
def main():
    permute(str(raw_input("Enter the String:")), 0) 
if __name__ == '__main__':
    main()

                