def random_randint(k,A):
    for i in range(k):
        # Generate a random index in i to lenngth of A - 1
        r = random_randint(i,len(A)-1)
        A[i],A[r] = A[r],A[i]