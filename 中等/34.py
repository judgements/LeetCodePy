"""
34. 在排序数组中查找元素的第一个和最后一个位置
"""

import os
import sys
from typing import List 

# 寻找左边界
def leftMargin(nums: List[int], target: int):

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        # 如果 nums[mid] = target，继续向左寻找左边界
        if nums[mid] == target:
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    if nums[low] == target:
        return low
    # 如果左边界的值不等于 target
    else:
        return -1

# 寻找右边界
def rightMargin(nums: List[int], target: int):

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        # 如果 nums[mid] = traget，继续向右寻找右边界
        if nums[mid] == target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    if nums[high] == target:
        return high
    # 如果右边界的值不等于 target
    else:
        return -1

def searchRange1(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0 or nums[0] > target or nums[-1] < target:
        return [-1,-1]

    lm = leftMargin(nums, target)
    rm = rightMargin(nums, target)

    return [lm,rm]

'''
解法二, 相比解法一时间复杂度要高, 解法一时间复杂度为O(logn)
'''
def searchRange2(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0 or nums[0] > target or nums[-1] < target:
        return [-1, -1]
    p, q = 0, len(nums) - 1
    while nums[p] < target and p < q:
        p = p + 1
    while nums[q] > target and p < q:
        q = q - 1
    if p == q:
        return [-1, -1]
    return [p, q]



nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
nums3 = []
target3 = 0
# ans = searchRange1(nums1, target1)
ans = searchRange2(nums3, target3)
print(ans)
