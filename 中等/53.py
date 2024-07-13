"""
53. 最大子数组和
"""

import os
import sys
from typing import List

def maxSubArray(nums: List[int]) -> int:
    size = len(nums)
    if size == 0:
        return 0
    dp = [0 for _ in range(size)]   # 初始化
    dp[0] = nums[0]      # 更新第一个
    for i in range(1, size):
        if dp[i-1] <= 0:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i-1] + nums[i]
    return max(dp)

# nums2 = [2]
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))

'''
解法二：分治法。 时间复杂度O(NlogN), 空间复杂度为O(logN)
'''
def maxSubArray2(nums: List[int]) -> int:
    size = len(nums)
    if size == 0:
        return 0
    return max_sub_array(nums, 0, size - 1)

def max_sub_array(self, nums, left, right):
    if left == right:
        return nums[left]
    mid = (left + right) >> 1
    return max(max_sub_array(nums, left, mid),
                max_sub_array(nums, mid + 1, right),
                max_cross_array(nums, left, mid, right))

def max_cross_array(self, nums, left, mid, right):
    # 一定包含 nums[mid] 元素的最大连续子数组的和，
    # 思路是看看左边"扩散到底"，得到一个最大数，右边"扩散到底"得到一个最大数
    # 然后再加上中间数
    left_sum_max = 0
    start_left = mid - 1
    s1 = 0
    while start_left >= left:
        s1 += nums[start_left]
        left_sum_max = max(left_sum_max, s1)
        start_left -= 1

    right_sum_max = 0
    start_right = mid + 1
    s2 = 0
    while start_right <= right:
        s2 += nums[start_right]
        right_sum_max = max(right_sum_max, s2)
        start_right += 1
    return left_sum_max + nums[mid] + right_sum_max
