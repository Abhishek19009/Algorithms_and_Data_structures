# Don't make mistake while doing recursion
# Recursion is easy. All you have to do is return the recursion values properly
# One common observation is in each recursion call, something should be returned.

def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l)//2
        if x == arr[mid]:
            return mid

        elif x < arr[mid]:
            return binary_search(arr, l, mid-1, x)

        else:
            return binary_search(arr, mid+1, r, x)

    else:
        return -1


if __name__ == "__main__":
    arr = [3, 5, 4, 7, 4, 2, 6, 8, 5, 9, 3, 34, 12, 87]
    arr.sort()
    index = binary_search(arr, 0, len(arr)-1, 12)

    if index == -1:
        print("No such element found!!!")
    else:
        print(f"Element present at {index} index !!")
