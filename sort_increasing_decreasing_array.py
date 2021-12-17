# P.139
def sort_k_increasing_decreasing_array(A):
    # Decomposes A into a set of sorted arrays.
    sorted_subarrays = []
    increasing,decreasing = range(2)
    subarrays_type = increasing
    start_idx = 0
    for i in range(1,len(A)+1):
        # A is ended. Adds the last subarray.
        if(i==len(A) or (A[i-1]<A[i] and subarray_type == decreasing) or (A[i-1]>=A[i] and subarray_type == increasing)):
            sorted_subarrays.append(A[start_idx:i] if subarray_type == increasing else A[i-1:start_idx-1:-1])
            start_idx=i
