# Permutation is a reaarangement of numbers like below.
# [1,2,3,4]
# [1,2,4,3],[1,3,2,4],[1,3,4,2],[1,4,2,3],[1,4,3,2],
# [2,1,3,4],[2,1,4,3],[2,3,1,4],[2,3,4,1],[2,4,1,3],[2,4,3,1],
# ............
# Total number of permutation about [1,2,3,4] is 24.this program calculate this number(in this case,the number is 24).

# both args are list.perm is short of permutation,A is an array of n elements.
def apply_permutation(perm,A):
    for i in range(len(A)):
        while perm[i] != i:
            A[perm[i]],A[i] = A[i],A[perm[i]]
            perm[perm[i]],perm[i] = perm[i],perm[perm[i]]