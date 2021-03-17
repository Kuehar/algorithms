# [25,36,4,55,71,18,0,71,89,65]
# 89
# O(N)
def linearSearch(nums,ans):
    for i in range(len(nums)):
        if nums[i] == ans:
            return True
    return False
    


## nums = [25,36,4,55,71,18,0,71,89,65]
## ans = 89
## O(N)
## print(linearSearch(nums,ans)) # True


## O(N^2)
##for i in range(10):
##    for j in range(i+1):
##        print(i)
##        print(j)


n,inf = 0,2000000000
for i in range(len(n)):
    