''' Read Universal_Hashing.txt for more details '''
import random

arr = [i for i in range(100)]

# Let say we want to map arr into a array with 150 elements
# i.e we want to create hashmap for arr to another array arr2

# We will use ((ak+b)mod p)mod m    hash function

# Let's take 101 or any prime number p, then we can take any random number a and b less than p.
# m would be number 150

p = 163

a = random.randint(1,1000)%p
b = random.randint(1,1000)%p

m = 150

arr2 = [0]*m

for i in arr:
    hash_val = ((a*i + b)%p)%m
    arr2[hash_val] += 1

print(arr2)

# We get fairly randomized hash values. And we can observe that number of 2's obtained in the arr2 is very low.
