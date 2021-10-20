'''
Python has a very cool and short codeline to swap elements without using any temporary variable.
'''

arr = [3,4,5,6,9,1]
arr[2],arr[3] = arr[3],arr[2]   # swap element at 3 index with element at 2 index

'''
This is much shorter than creating temp variable to store 3 element and then assigning it to 2 element.
'''