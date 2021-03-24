def simple_gcd(a,b):
    if a < b:
        a,b = b,a
    x = b
    while True:
        if a % x == 0 and b % x == 0:
            return x
        x -= 1