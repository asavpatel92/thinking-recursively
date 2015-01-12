#===============================================================================
# implementation of quicksort
#===============================================================================

import random

def swap (array, first_index, second_index):
    array[first_index], array[second_index] = array[second_index], array[first_index]
    return array

def partition(array, first_index, last_index):
    q = first_index
    p = first_index
    for p in range(first_index, last_index):
        if array[p] <= array[last_index]:
            swap(array, p, q)
            q += 1
        p += 1
    swap(array, last_index, q)
    return q

def quick_sort(array, first_index, last_index):
    if first_index < last_index:
        pivot = partition(array, first_index, last_index)
        quick_sort(array, first_index, pivot - 1)
        quick_sort(array, pivot + 1, last_index)
        

def main():
    n = 10
    array = [random.randint(0,100) for _ in range(n)]
    print "Unsorted Array is : %s" %(array)
    quick_sort(array, 0, len(array) - 1)
    print "Sorted Array is : %s" %(array) 
    

if __name__ == '__main__':
    main()