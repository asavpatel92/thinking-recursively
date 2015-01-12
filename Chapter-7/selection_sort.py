#===============================================================================
# this function sorts the input array using selection sort . worst case time complexity of this algorithm is O(n^2)
#===============================================================================

import random

#===============================================================================
# swap functions swaps the entries from given two index in the array.
# basically it does the following operation
# temp = array[first_index]
# array[first_index] = array[second_index]
# array[second_index] = temp
#===============================================================================

def swap(array, first_index, second_index):
    array[first_index], array[second_index] = array[second_index], array[first_index]
    return array

#===============================================================================
# find_min_value function finds the minimum value from the array and it's index
#===============================================================================

def find_min_value(array, start_index):
    min_index = start_index
    min_value = array[start_index]
    for i in range(start_index + 1, len(array)): 
        #=======================================================================
        # main thing to notice here is we start iterating from start_index + 1 because we have stored the min_value in the variable above so we need that to compare future entries 
        #=======================================================================
        if array[i] < min_value:
            min_index = i
            min_value = array[i]
    return min_index

#===============================================================================
#===============================================================================
# # this is main function which performs selction sort.
# # start with index 0 of given array and call find_min_value for each index 
# # and swap current index with the index returned from find_min_value 
#===============================================================================
#===============================================================================

def selection_sort(array):
    for i in range(len(array)):
        ref_index = find_min_value(array, i)
        swap(array, i, ref_index)
    return array

def main():
    n = 10
    array = [random.randint(0, 100) for x  in range(n)]
    print "Unsorted array is : %s" %(array)
    selection_sort(array)
    print "Sorted array is : %s" %(array)
    
if __name__ == '__main__':
    main()