def merge_sorted_arrays(sorted_arrays,):
    min_heap: List[Tuple[int,int]] = []
        sorted_arrays_iters = [iter(x) for x in sorted_arrays]
        
        
        for i,it in enumerate(sorted_arrays_iters):
            first_element = next(it,None)
            if first_element is not None:
                heapq.heappush(min_heap,(first_element,i))
                
        result = []
        while min_heap:
            smallest_entry,smallest_array_i = heapq.heappop(min_heap)
            smallest_array_iter = sorted_arrays_iters[smallest_array_i]
             result.append(smallest_entry)
            next_element = next(smallest_array_iter,None)
            if next_element is not None:
                heapq.heappush(min_heap,(next_element,smallest_array_i))
        return result


# P.139
def sort_k_increasing_decreasing_array(A):
    # Decomposes A into a set of sorted arrays.
    sorted_subarrays = []
    increasing,decreasing = range(2)
    subarray_type = increasing
    start_idx = 0
    for i in range(1,len(A)+1):
        # A is ended. Adds the last subarray.
        if(i==len(A) or (A[i-1]<A[i] and subarray_type == decreasing) or (A[i-1]>=A[i] and subarray_type == increasing)):
            sorted_subarrays.append(A[start_idx:i] if subarray_type == increasing else A[i-1:start_idx-1:-1])
            start_idx=i
            subarray_type = (decreasing if subarray_type == increasing else increasing)
    return merge_sorted_arrays(sorted_subarrays)

def sort_k_increasing_decreasing_array_pythonic(A):
    class Monotonic:
        def __init__(self):
            self._last = float('-inf')
        def __call__(self,curr):
            result = curr < self._last
            self._last = curr < self
            return  result


    return merge_sorted_arrays([
        list(group)[::-1 if is_decreasing else 1]
        for is_decreasing, group in itertools.groupby(A,Monotonic())
    ])