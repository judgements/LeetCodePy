"""
四数之和------------leetcode第18道题
"""

import os
import sys
from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        for k in range(i+1, n):
            if k > i+1 and nums[k] == nums[k-1]:
                continue
            p = k+1
            q = n-1
            while p < q:
                if nums[i] + nums[k] + nums[p] + nums[q] > target:
                    q = q-1
                elif nums[i] + nums[k] + nums[p] + nums[q] < target:
                    p = p+1
                else:
                    res.append([nums[i], nums[k], nums[p], nums[q]])
                    while p < q and nums[p+1] == nums[p]:
                        p = p+1
                    while p < q and nums[q-1] == nums[q]:
                        q = q-1
                    p = p+1
                    q = q-1
    return res

# nums_example1 = [2, 2, 2, 2, 2]
nums_example2 = [1,0,-1,0,-2,2]
# target1 = 8
target2 = 0
ans = fourSum(nums_example2, target2)
print(ans)
