def insertion_sort(A,N):
    for i in range(N):
        v = A[i]
        j = i-1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v

def main():
    A = [2,8,9,4,5,1]
    N = 6
    print(A)
    insertion_sort(A,N)
    print(A)

if __name__=='__main__':
    main()