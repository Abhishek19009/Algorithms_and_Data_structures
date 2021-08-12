import math

# Understand that divisors are in pairs ex - (2,50), (4,25), (5,20), (10,10) etc
# time complexity of below algorithm:- sqrt(n)

def printDivisors(n):
    i = 1
    new_list = []
    while i <= math.sqrt(n):
        if n % i == 0:
            if n // i == i:
                new_list.append(i)
            else:
                new_list.append(i)
                new_list.append(n // i)
        i = i + 1
    return new_list


print("The divisors of 100 are:")
print(printDivisors(100))
