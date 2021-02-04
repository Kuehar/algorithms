def dutch_flag_partition(pivot_name: int, A: List[int]) -> None:
    pivot = A[pivot_name]
    # first pass : group elements smaller than pivot
    for i in range(len(A)):
        # Look for smaller element
        for j in range(i+1,len(A)):
            if A[j] < pivot:
                A[i],A[j] = A[j],A[i]
                break
    # Second pass: group elements larger than pivot/
    for i in reversed(range(len(A))):
        # Look for a larger element. 
        # Stop when we reach an element less than pivot,since first pass has moved them to the start of A
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i],A[j] = A[j],A[i]
                break