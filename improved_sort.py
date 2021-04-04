"""
merge two sorted arrays such as [42,72],[39,71]

1.[42,72],[39,71] -> [39]
2.[42,72],[39,71] -> [39,42]
3.[42,72],[39,71] -> [39,42,71]
4.[42,72],[39,71] -> [39,42,71,72]
"""

import random

# O(N)
def merge_arrays(left,right=[]):
    res = []
    i,j = 0,0
    n,m = len(left),len(right)
    # This method will be over when it finished searching either one.
    while i < n and j < m:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    # Added remaining arrays element to return array.
    return res + left[i:] + right[j:]

def step(array):
    res = []
    for i in range(0,len(array),2):
        res.append(merge_arrays(*array[i:i+2]))
    return res

"""
# Initialize random number generator
random.seed(4)

my_array = [random.randint(0,100) for i in range(15)]
my_array = [[v] for v in my_array]

step1 = step(my_array)
print(step1)
# [[30, 38], [13, 92], [50, 61], [11, 11], [2, 2], [51, 70], [37, 97], [7]]

step2 = step(step1)
print(step2)
# [[13, 30, 38, 92], [11, 19, 50, 61], [2, 8, 51, 70], [7, 37, 97]]

step3 = step(step2)
print(step3)
# [[11, 13, 19, 30, 38, 50, 61, 92], [2, 7, 8, 37, 51, 70, 97]]

step4 = step(step3)
print(step4)
# [[2, 7, 8, 11, 13, 19, 30, 37, 38, 50, 51, 61, 70, 92, 97]]

def merge_sort(array):
    # Turning all numbers into list
    res = [[v] for v in array]
    while len(res[0]) != len(array):
        res = step(res)
    return res[0]

my_array = [random.randint(0,100) for i in range(15)]
my_array = [[v] for v in my_array]

print(merge_sort(my_array))
# [[7], [29], [30], [36], [37], [42], [49], [50], [57], [71], [74], [80], [81], [91], [94]]
"""

# Implement merge_sort with recursion.

def recursive_merge_sort(array):
    if len(array) <= 1:
        return array
    mid_idx = len(array) // 2
    left = array[:mid_idx]
    right = array[mid_idx:]
    return merge_arrays(merge_sort(left),merge_sort(right))

print(recursive_merge_sort(my_array))
# [[8], [12], [15], [23], [40], [44], [51], [51], [56], [57], [79], [80], [86], [92], [95]]