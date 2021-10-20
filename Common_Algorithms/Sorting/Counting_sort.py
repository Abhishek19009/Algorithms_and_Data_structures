'''
This is stable implementation of counting sort.
Unstable version is easier to implement but not that useful for keys that contain
essential info other than just values.

Time Complexity of stable counting sort:- O(n+k)
where n is the number of elements in the array
k is the range of values in the array (i.e the element with maximum value in the array)

Auxiliary space of counting sort:- O(n+k)
'''


def count_sort(arr):
    # Get the range of elements in array

    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1

    # Create count array to store count of individual element and initialize it to 0

    count_arr = [0 for _ in range(range_of_elements)]
    out_arr = [0 for _ in range(len(arr))]

    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i] - min_element] += 1

    # Do cumulative addition
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Create the output array
    # Below code uses element indexing from back to front
    # If want to use front indexing, make sure you handle 0 index accordingly
    # And take care of negative indexing

    for i in range(len(arr) - 1, -1, -1):
        out_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    arr = [out_arr[i] for i in range(len(out_arr))]

    return arr


if __name__ == '__main__':
    arr = [1, 0, 3, 1, 3, 1]

    result = count_sort(arr)

    print(result)
