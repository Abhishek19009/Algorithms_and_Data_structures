# HeapSort is bit tricky. Use GeeksforGeeks video to get clear visualization of heap sort.
# Try to get bigger picture of what is happening

def heapify(arr, n, i):
    largest = i     # Initialize largest as root
    l = 2*i + 1     # left = 2*i + 1
    r = 2*i + 2     # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root is applicable
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        # heapify the root
        heapify(arr, n , largest)

def heap_sort(arr):
    n = len(arr)

    # for each loop call we are basically trying to heapify subtree starting from middle element - 1
    # because left child of this element 2i + 1 = 2(n//2-1) + 1 = n-1 which is index within bound.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # This is the meat and potato of the code. At each stage we swap first and current index value because we know
    # first element after each heapify step is largest element. Furthermore we are starting from last index so that
    # will be smaller than each parent element.

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print(arr)
