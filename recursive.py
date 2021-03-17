def recursion(i,v,a):
    # ベースケース
    if i == 0:
        if v == 0:
            return True
        return False
    # a[i-1]を選択しない場合
    if recursion(i-1,v,a):
        return True
    # a[i-1]を選択する場合
    if recursion(i-1,v-a[i-1],a):
        return True
    return False

N = W = 0

print("1つめの数字を入力してください")
N = int(input())
print("2つめの数字を入力してください")
W = int(input())

for i in range(W):
    a[i] 