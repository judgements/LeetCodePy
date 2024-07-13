"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
"""

import os
import sys
from typing import List

def letterCombinations(digits: str) -> List[str]:
    phoneMap = {
        '2':'abc', 
        '3':'def', 
        '4':'ghi', 
        '5':'jkl', 
        '6':'mno', 
        '7':'pqrs', 
        '8':'tuv', 
        '9':'wxyz'}
    n = len(digits)

    def dfs(index):
        if index == n:
            combinations.append("".join(combination))
        else:
            digit = digits[index]
            for letter in phoneMap[digit]:
                combination.append(letter)
                dfs(index+1)
                combination.pop()

    combination = []
    combinations = []
    dfs(0)
    return combinations

digits = "23"         # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letterCombinations(digits))
