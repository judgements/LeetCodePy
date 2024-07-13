"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""

import os
import sys
from typing import List

def generateParenthesis(n: int) -> List[str]:
    if n == 0:
        return []
    total_l = []
    total_l.append([None])
    total_l.append(['()'])
    for i in range(2, n+1):
        temp = []
        for j in range(i):
            p_list = total_l[j]
            q_list = total_l[i-j-1]
            for kp in p_list:
                for kq in q_list:
                    if kp == None:
                        kp = ""
                    if kq == None:
                        kq = ""
                    temp.append("(" + kp + ")" + kq)
        total_l.append(temp)
    return total_l[n]

n = 1
# n = 3
print(generateParenthesis(n))
