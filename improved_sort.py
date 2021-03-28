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
    i = j = 0
    n,m = len(left),len(right)
    # This method will be over when it finished searching either one.
    while i < n and j < m:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            i += 1
    # Added remaining arrays element to return array.
    return res + left[i:] + right[j:]

def step(array):
    res = []
    for i in range(0,len(array,2):
        res.append(merge_arrays(*array[i:i+2]))
    return res