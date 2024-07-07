"""
139. 单词拆分
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
"""

import os
import sys
from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False for i in range(n+1)]
    dp[0] = True
    for i in range(n):
        for j in range(i+1, n+1):
            if dp[i] and s[i:j] in wordDict:
                dp[j] = True
    return dp[-1]
s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))      # true , 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成
