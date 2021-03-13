# -*- coding: UTF-8 -*-

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
