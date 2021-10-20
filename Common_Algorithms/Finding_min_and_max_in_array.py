'''
Very short cool algorithm to find minimum or maximum of an array
Obviously this would apply to any data structure whose elements
can be accessed via index or pointers.
( Python lists are actually highly optimised array)
This algo returns index of minimum or maximum element.
Time complexity:-
Best case :- O(1)
Worst case:- O(n)
'''

def get_min(array):
    min_index = 0
    for i in range(1, len(array)):
        if array[i] < array[min_index]:
            min_index = i
    return min_index

def get_max(array):
    max_index = 0
    for i in range(1, len(array)):
        if array[i] > array[max_index]:
            max_index = i
    return max_index


array = [3,5,3,45,21]

print(get_min(array))
print(get_max(array))