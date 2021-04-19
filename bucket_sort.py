import random

def counting_sort(nums,max_num):
    # 最大個数分バケツを用意
    count_list = [0]*(max_num)
    # 一旦全てのデータをバケツに放り込む
    for n in nums:
        count_list[n] += 1

    # バケツの順番に数値を取り出し、配列にいれる
    n = 0
    for i in range(len(count_list)):
        for j in range(count_list[i]):
            nums[n] = i
            nums += 1


