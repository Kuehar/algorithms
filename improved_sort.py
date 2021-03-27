"""
merge two sorted arrays such as [42,72],[39,71]

1.[42,72],[39,71] -> [39]
2.[42,72],[39,71] -> [39,42]
3.[42,72],[39,71] -> [39,42,71]
4.[42,72],[39,71] -> [39,42,71,72]
"""

def merge_arrays(left,right=[]):
    res = []
    i = j = 0
    n,m = len(left),len(right)
    # This method will be over when it finished searching of either one.
    while i < n and j < m:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            i += 1
    return res + left[i:] + right[j:]