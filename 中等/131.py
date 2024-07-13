"""
131. 分割回文串
给你一个字符串 s, 请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
用动态规划的方法做
"""

import os, sys
from typing import List

def partition(s: str) -> List[List[str]]:
    n = len(s)
    f = [[True] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

    ret = list()
    ans = list()

    def dfs(i: int):
        if i == n:
            ret.append(ans[:])
            return
        
        for j in range(i, n):
            if f[i][j]:
                ans.append(s[i:j+1])
                dfs(j + 1)
                ans.pop()

    dfs(0)
    return ret
s1 = "aab"    # [["a","a","b"],["aa","b"]]
s2 = "a"     # [["a"]]
print(partition(s1))
