
# NOTE:- TRADITIONALLY RADIX SORT USES COUNTING SORT AS A SUBROUTINE, BUT IN THIS CASE WE EMPLOYED BUCKET METHOD
# WHICH IS NOTICEABLY FASTER AND LESS CUMBERSOME.

'''
Also know as Bucket Sort because it involves creating buckets.
It comes under Integer sorting and is very fast for elements with smaller digits but large in numbers
Complexity is O(n*d) where n is number of elements and d is length of max number in array.
Obviously if d<<n, then it can be considered as constant and complexity become linear.
ex- if max element is 125 and there are 10 million of elements in array, radix sort is very quick
and complexity is linear ( 3 << n = 10 million )
But if element is 64564334767454774549
and there are 20 elements
That accounts for 20*20 or n^2 complexity.

A simple way to prevent this is to use hashing for larger digits.
'''
from functools import reduce
from random import shuffle

# flattens our Bucket list into a 1D list
def __flatten(A):
    return reduce(lambda x, y: x + y, A)

def radix(A, num_digits):
    for digit in range(0, num_digits):
        # Creating 10 buckets for each value 0-9
        B = [[] for i in range(10)]
        for item in A:
            # num is the index of bucket where item will be put into
            num = (item // 10**(digit)) % 10
            B[num].append(item)

            # flatten the list i.e extract the elements from each bucket and assign them to our another array
            # basically the flattened list will be sorted list for corresponding digit value
            # And then this list will become our new A
            # refer to Joe James radix sort video for clear explanation

        A = __flatten(B)

    return A

if __name__ == "__main__":
    A = [55, 45, 3, 289, 213, 1 ,288, 53, 2]
    num_digits = len(str(max(A)))
    A = radix(A, num_digits)
    print(A)

    # Another Test Case
    C = [i for i in range(1000000)]
    shuffle(C)
    C = radix(C, len(str(max(C))))
    print(C[:6], C[-6:])

     
# Observation:- There is no comparison or if statements. That makes radix sort fairly quick.
# In this case we didn't used counting sort as subroutine because bucket method is much quicker than
# performing counting sort at digit.