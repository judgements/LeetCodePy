"""
91. 解码游戏
"""

import os
import sys

def numDecodings(s: str) -> int:
    n = len(s)
    f = [1] + [0] * n
    for i in range(1, n + 1):
        if s[i - 1] != '0':
            f[i] += f[i - 1]
        if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
            f[i] += f[i - 2]
    return f[n]

s1 = "12"         # ans is 2
s2 = "226"      # ans is 3
s = "0"
print(numDecodings(s))
