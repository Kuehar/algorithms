def greedy(price):
    # コインの種類を設定
    value = [500,100,50,10,5,1]
    result = add = 0
    # コインの種類の回数for文を実行し、その中でadd(枚数)
    for i in range(6):
        add = price / value[i]

        price -= value[i]*add
        result += add
    return result

print(greedy(507))