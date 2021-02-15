# Given n, return all primes up to and including n.
def generate_primes(n):
    primes = []
    is_prime = [False,False] + [True] * (n-1)
    for p in range(2,n+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p*2,n+1,p):
                is_prime[i] = False
    return primes

n = 100
print(generate_primes(n)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]