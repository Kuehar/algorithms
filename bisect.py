import bisect

a = [3,8,11,18,18,27,31]

bisect.bisect_right(a,18) # 5

bisect.bisect_left(a,18) # 3