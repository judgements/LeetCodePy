"""
7. 整数反转
给你一个 32 位的有符号整数 x , 返回将 x 中的数字部分反转后的结果.
如果反转后整数超过 32 位的有符号整数的范围 [-2^31,  2^31 - 1] ,就返回 0.
"""

import os,sys

MAX_INT = 2 ** 31 - 1
MIN_INT = - 2 ** 31

def reverse(x: int) -> int:
    ans = 0
    sign = 1
    if x < 0:
        sign = -1
        x = -1 * x
    while x // 10:
        re = x % 10
        ans = ans * 10 + re
        x //= 10
    ans = ans * 10 + x % 10
    if ans > MAX_INT or ans < MIN_INT:
        return 0
    return ans * sign

x1 = -123
x2 = 123
print(reverse(x1))
