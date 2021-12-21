""" 
最長共通部分列(Common Longest Subsequence)の解法
二つの文字列+1の長さの二次元配列を作り、それぞれの文字列を二重for文で舐めながら比較する
仮に合致するならdp[i+1][j+1]の値をプラス1する
ex.X = "abcde",Y="ace"の場合
      a b c d e
      0 1 2 3 4 5
a 0 [[0,0,0,0,0,0]
c 1  [0,1,1,1,1,1]
e 2  [0,1,1,2,2,2]
  3  [0,1,1,2,2,3]]
になる。
例えば a=aとなるX[j] = Y[i]の場合にはその右下の値になるdp[i+1][j+1]をプラス1している。
それ以外の場合に当たるa=bの場合にはdp[i+1][j],dp[i][j+1]の大きい値をdp[i+1][j+1]に代入し、これを最後まで繰り返すと最終的に最長共通部分列の値が導き出せることになる
"""



def lcs(X,Y):
    dp = [[0 for i in range(len(X)+1)] for j in range(len(Y)+1)]
    for i in range(len(Y)):
        for j in range(len(X)):
            if X[j] ==  Y[i]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

    return max(list(map(lambda x: max(x), dp)))