# 最長共通部分列(Common Longest Subsequence)の解法
# 二つの文字列+1の長さの二次元配列を作り、それぞれの文字列を二重for文で舐めながら比較する


def lcs(X,Y):
    dp = [[0 for i in range(len(X)+1)] for j in range(len(Y)+1)]
    for i in range(len(Y)):
        for j in range(len(X)):
            if X[j] ==  Y[i]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

    return max(list(map(lambda x: max(x), dp)))