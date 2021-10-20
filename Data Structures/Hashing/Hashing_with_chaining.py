'''
Usually hashing creates problem of multiple elements belonging to same hash.
To accommodate this we can store such elements in some data structure like list.
'''

# Consider the hash function f(n) = n mod 7 where n is the element of the list.

arr = [15, 47, 23, 34, 85, 97, 56, 89, 70]

# Creating 7 empty buckets

buckets = [[] for _ in range(7)]

for elem in arr:
    buckets[elem%7].append(elem)

print(buckets)