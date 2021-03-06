class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
# Time Limit Exceeded

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = collections.defaultdict(int)
        memo[0], memo[1], memo[2] = 0,1,1
        for i in range(3,n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[n]
# Runtime: 28 ms, faster than 80.87% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 14.3 MB, less than 13.79% of Python3 online submissions for N-th Tribonacci Number.
# https://qiita.com/KueharX/items/0ece7bf16e94046861d6
# https://www.kueharx.com/2021/03/leetcode.html
