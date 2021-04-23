# Find the maximum number into the list.
def find_max(A,l,r):
    # Divide
    m = (l + r) // 2
    if l == r-1:
        return A[l]
    else:
        u = find_max(A,l,m)
        v = find_max(A,m,r)
        x = max(u,v) # conquer
    return x

def main():
    A = [2,8,9,4,5,1]
    l = 6
    r = 5
    find_max(A,l,r)

if __name__=='__main__':
    main()
    # [2, 8, 9, 4, 5, 1]
    # [1, 2, 4, 5, 8, 9]