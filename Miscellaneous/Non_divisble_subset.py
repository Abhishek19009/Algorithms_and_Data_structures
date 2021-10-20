"""
Refer to "Non_divisible_subset" of Hackerrank problem medium difficulty

Sum of 2 numbers is called evenly divisible if sum of remainder of each number
is equal to divisor.
ex- let k divides a+b.
Then if a/k + b/k = k
then pair of a and b is evenly divisible by k.

General Algorithm:- Since all we have to deal with is the modulus of each element in set S
when divides by k.
We can create a temp counter list which counts the number of times a remainder has been obtained.

After that, notice since we can't simultaneously have x and k-x elements in new S
which implies we have to select maximum of both 2 since that is the purpose of the question.
0 and k/2 is the special case since k-0 = k and k will not be present in new S
Also k - k/2 = k/2
or m = n = k/2
Even 2 of 0 and k/2 elements will give a pair i.e evenly divisible, hence we have to select only
1 for both each.

"""


def max_non_evenly_divisible_subset(n, k, numbers):
    temp = [0] * k

    for i in range(len(numbers)):
        temp[numbers[i]%k] += 1

    count = 0
    count += min(temp[0], 1)
    if k % 2 == 0:
        count += 1
    for i in range(1, k // 2 + 1):
        if i != k - i:
            count += max(temp[i], temp[k - i])
    return count

if __name__ == "__main__":
    n, k = map(int, input().strip().split(" "))
    numbers = list(map(int, input().strip().split(" ")))
    result = max_non_evenly_divisible_subset(n, k, numbers)
    print(result)