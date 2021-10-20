'''
The best way to perform this operation in linear time complexity is to add subsequent
terms at each index of the array, and compare it to element corresponding to current
index. Find the max of both these.
Then use another variable ('best' in this case) to compare the current and previous sums.
'''

def FindMax(arr):
    sum = 0
    best = 0
    for i in range(len(arr)):
        sum = max(arr[i], sum+arr[i])
        best = max(sum, best)
    return best

if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split(" ")))
    result = FindMax(arr)
    print(result)
