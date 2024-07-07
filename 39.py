"""
39. 组合总和
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target, 找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合
并以列表形式返回。你可以按 任意顺序 返回这些组合。
"""

import os
import sys
from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def dfs(candidates, target, index, n, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
        for i in range(index, n):
            dfs(candidates, target-candidates[i], i, n, path+[candidates[i]], res)
    
    n = len(candidates)
    if n == 0:
        return []
    path = []
    res = []
    dfs(candidates, target, 0, n, path, res)
    return res

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))      # [[2,2,3],[7]]
