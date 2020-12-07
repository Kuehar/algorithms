class Solution:
  def greedy(self):
    n = int(input())
    k = int(input())
    start = 1
    for i in range(n):
      start = min(start*2,start+k)
    return start
