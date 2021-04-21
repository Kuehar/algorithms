def bubble_sort(A,N):
    flg = 1
    for i in range(N):
        flg = 0
        for j in reversed(range(i+1, N)):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
                flg = 1


def main():
    A = [2,8,9,4,5,1]
    N = 6
    print(A)
    bubble_sort(A,N)
    print(A)

if __name__=='__main__':
    main()
    # [2, 8, 9, 4, 5, 1]
    # [1, 2, 4, 5, 8, 9]