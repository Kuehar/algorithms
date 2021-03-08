# This program is to calculate greatest common divisor.That's called Euclid algorithm.
# Implemented with recursion.


def euclid(m,n):
    if n == 0:
        return m
    else:
        return euclid(n,m%n)

print("Input:Number1 that you want to calculate greatest common divisor")
n = int(input())
print("Input:Number2 that you want to calculate greatest common divisor")
m = int(input())

print(euclid(m,n))