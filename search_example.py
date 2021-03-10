# [25,36,4,55,71,18,0,71,89,65]
# 89


# O(N)
def linearSearch(nums,ans):
    for i in range(len(nums)):
        if nums[i] == ans:
            return True
    return False
    


nums = [25,36,4,55,71,18,0,71,89,65]
ans = 89

print(linearSearch(nums,ans)) # True



