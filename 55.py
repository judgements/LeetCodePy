"""
55. 跳跃游戏
给定一个非负整数数组 nums , 你最初位于数组的 第一个下标.
数组中的每个元素代表你在该位置可以跳跃的最大长度.
判断你是否能够到达最后一个下标.
"""

import os, sys
from typing import List

def canJump(nums: List[int]) -> bool:
    n, rightMost = len(nums), 0
    for i in range(n):
        if i <= rightMost:
            rightMost = max(rightMost, i + nums[i])
        if rightMost >= n - 1:
            return True
    return False

nums1 = [2,3,1,1,4]   # ans is true
nums2 = [3,2,1,0,4]   # ans is false
print(canJump(nums2))
