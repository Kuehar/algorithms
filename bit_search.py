# -*- coding: UTF-8 -*-


"""
budget = 1000
books = (("鬼滅の刃",420),("ジャンプ",320),("ソフトウェアデザイン",560))
booksLength = len(books)
for i in range(2**booksLength):
    cart = []
    print("pattern {}: ".format(i))
    for j in range(booksLength):
        if ((i >> j) & 1):
            cart.append(books[j][0])
    print(cart)

pattern 0: 
[]
pattern 1: 
['鬼滅の刃']
pattern 2: 
['ジャンプ']
pattern 3: 
['鬼滅の刃', 'ジャンプ']
pattern 4: 
['ソフトウェアデザイン']
pattern 5: 
['鬼滅の刃', 'ソフトウェアデザイン']
pattern 6: 
['ジャンプ', 'ソフトウェアデザイン']
pattern 7: 
['鬼滅の刃', 'ジャンプ', 'ソフトウェアデザイン']
"""

def bit_search(budget,books):
    booksLength = len(books)
    for i in range(2**booksLength):
        cart = []
        print("pattern {}: ".format(i))
        for j in range(booksLength):
            if ((i >> j) & 1):
                cart.append(books[j][0])
        print(cart)


budget = 1000
books = (("鬼滅の刃",420),("ジャンプ",320),("ソフトウェアデザイン",560))
bit_search(budget,books)