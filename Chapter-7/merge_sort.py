import random
from math import floor

def merge(array, start_index, end_index, join_index):
    low_half = []
    high_half = []
    k = start_index
    i = 0
    j = 0
    
    #===========================================================================
    # now we'll divide the array in two parts --> low_half[0...i] and high_half[0...j]
    #===========================================================================
    while k <= join_index:
        low_half.append(array[k])
        k += 1
        i += 1
    
    while k <= end_index:
        high_half.append(array[k])
        k += 1
        j += 1
    
    #===========================================================================
    # now array is divided and we'll reset the indexes
    #===========================================================================
    
    k = start_index
    i = 0
    j = 0
    
    #===========================================================================
    # now we'll merge the both arrays while sorting it
    #===========================================================================
     
    while i < len(low_half) and j < len(high_half):
        if low_half[i] < high_half[j]:
            array[k] = low_half[i]
            i += 1
        else:
            array[k] = high_half[j]
            j += 1
        k +=  1
    
    while i < len(low_half):
        array[k] = low_half[i]
        i += 1
        k += 1
            
    while j < len(high_half):
        array[k] = high_half[j]
        j += 1
        k += 1
    
    return array

def merge_sort(array, start_index, end_index):
    if ( start_index < end_index):
        mid_point = int(floor((start_index + end_index) / 2))
        merge_sort(array, start_index, mid_point)
        merge_sort(array, mid_point + 1, end_index)
        merge(array, start_index, end_index, mid_point)
        

def main():
    n = 10
    array = [random.randint(0, 100) for _ in range(n)] 
    print "Unsorted array is: ", array
    merge_sort(array, 0, len(array) - 1)
    print "Sorted array is: ", array

if __name__ == '__main__':
    main()