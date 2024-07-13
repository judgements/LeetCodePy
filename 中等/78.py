"""
78.子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
"""

import os
import sys
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    ans = []
    n = len(nums)
    def call_back(i, temp):
        ans.append(temp)
        for j in range(i, n):
            call_back(j+1, temp + [nums[j]])
    call_back(0, [])
    return ans

nums = [1,2,3]         # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(subsets(nums))
