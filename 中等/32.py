"""
32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
"""

import os, sys

def longestValidParentheses(s: str) -> int:
    n = len(s)
    if n < 2:
        return 0
    if n == 2:
        if s == '()':
            return 2
        else:
            return 0
    dp = [0 for i in range(n)]
    for i in range(2, n):
        if s[i] == ')':
            if s[i-1] == '(':
                dp[i] = dp[i-2] + 2
            if s[i-1] == ')':
                if s[i-1-dp[i-1]] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-2-dp[i-1]]
    return max(dp)

s1 = "(()"       # ans is 2
s2 = ")()())"         # ans is 4
s3 = ""          # ans is 0
print(longestValidParentheses(s2))
