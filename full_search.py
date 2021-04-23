def make_combination():
    for i in range(n):
        S[i] = 0
    rec(0)

def rec(i):
    if i == n:
        print(S)
        return
    rec(i+1)
    S[i] = 1
    rec(i+1)
    S[i] = 0