#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    temp_shift_count = 0
    final_shift_count = 0
    while True:
        for i in range(len(a) - 1):
            if a[i] <= a[i + 1]:
                continue
            else:
                temp_int = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp_int
                temp_shift_count += 1
        if temp_shift_count != 0:
            final_shift_count += temp_shift_count
            temp_shift_count = 0
        else:
            break

    print(f"Array is sorted in {final_shift_count} swaps.")
    print(f"First Element:", a[0])
    print(f"Last Element:", a[-1])

