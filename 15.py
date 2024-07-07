"""
15. 三数之和
给你一个整数数组 nums , 判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 
"""

import os
import sys
from typing import List

# 使用双指针
def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = []
    if not n or n < 3:
        return res
    nums.sort()
    for i in range(n):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i] == nums[i-1]:
            continue
        L = i+1
        R = n-1
        while L < R:
            if nums[i] + nums[L] + nums[R] == 0:
                res.append([nums[i], nums[L], nums[R]])
                while L < R and nums[L+1] == nums[L]:
                    L = L + 1
                while L < R and nums[R-1] == nums[R]:
                    R = R - 1 
                L = L + 1
                R = R - 1
            elif nums[i] + nums[L] + nums[R] < 0:
                L = L + 1
            else:
                R = R - 1
    return res
        

nums = [-1,0,1,2,-1,-4]       # [[-1,-1,2],[-1,0,1]]
print(threeSum(nums))
