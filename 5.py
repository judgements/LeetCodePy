"""
5. 最长回文子串
"""

import os
import sys

def longestPalindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    begin = 0
    max_len = 1       # 最大应设置为1, 而不是零
    # 字串长度
    for L in range(2, n+1):
        # 字串左边界
        for i in range(n):
            # 字串又边界
            j = L + i - 1
            if j >= n:
                break
            if s[i] != s[j]:
                dp[i][j] = False
            else:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            if dp[i][j] and j - i + 1 > max_len:
                begin = i
                max_len = j - i + 1
    return s[begin : begin + max_len]


s1 = "babad"       # 输出"bab"
s2 = "cbbd"       # 输出"bb"
print(longestPalindrome(s2))       
