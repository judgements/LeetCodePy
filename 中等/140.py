"""
140. 单词拆分2
给定一个字符串 s 和一个字符串字典 wordDict, 在字符串 s 中增加空格来构建一个句子，使得句子中所有的单词都在词典中。以任意顺序 返回所有这些可能的句子。
"""

import os
import sys
from typing import List

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    n = len(s)
    def backtrack(index: int) -> List[List[str]]:
        if index == len(s):
            return [[]]
        ans = list()
        for i in range(index + 1, len(s) + 1):
            word = s[index:i]
            if word in wordSet:
                nextWordBreaks = backtrack(i)
                for nextWordBreak in nextWordBreaks:
                    ans.append(nextWordBreak.copy() + [word])
        return ans
    
    wordSet = set(wordDict)
    breakList = backtrack(0)
    return [" ".join(words[::-1]) for words in breakList]

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(wordBreak(s, wordDict))         # ["cats and dog","cat sand dog"]
