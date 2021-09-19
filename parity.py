def parity(x:int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
# O(n)

"""
Parity of a binary word is  if the number of 1s is in the word is odd, otherwise, it is 0.
ex. 1011 -> 1, 1000100 -> 0
Parity checks are used to detect the single bit error in data storage and communication.
"""