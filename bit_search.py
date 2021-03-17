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



if __name__ == "__main__":
    budget = 1000
    books = (("Safari",420),("Leon",320),("Gill",560))
    bit_search(budget,books)

"""
pattern 0: 
[]
pattern 1: 
['Safari']
pattern 2: 
['Leon']
pattern 3: 
['Safari', 'Leon']
pattern 4: 
['Gill']
pattern 5: 
['Safari', 'Gill']
pattern 6: 
['Leon', 'Gill']
pattern 7: 
['Safari', 'Leon', 'Gill']
"""
