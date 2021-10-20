def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

if __name__ == "__main__":
    arr = [3, 7, 2, 8, 76, 1, 23]
    arr_sort = InsertionSort(arr)
    print(arr_sort)
