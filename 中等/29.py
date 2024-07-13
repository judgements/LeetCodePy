"""
29. 两数相除
给定两个整数，被除数 dividend 和除数 divisor。将两数相除, 要求不使用乘法、除法和 mod 运算符.
返回被除数 dividend 除以除数 divisor 得到的商。
整数除法的结果应当截去 (truncate) 其小数部分, 例如: truncate(8.345) = 8 以及 truncate(-2.7335) = -2
"""

import os
import sys

INT_MIN = - 2 ** 31
INT_MAX = 2 ** 31 - 1

def divide(dividend: int, divisor: int) -> int:
    if divisor == 0:
        return 0
    if divisor == 1:
        return dividend
    if divisor == -1:
        if dividend > INT_MIN: return -1 * dividend
        else: return INT_MAX
    a, b = dividend, divisor
    sign = 1
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        sign = -1
    a = a if a > 0 else -a
    b = b if b > 0 else -b
    ans = divi(a, b)
    return ans

def divi(a, b):
    if a < b:
        return 0
    tb = b
    count = 1
    while tb + tb < a:
        count = count + count
        tb = tb + tb
    return count + divi(a - tb, b)

dividend = 10
divisor = 3
print(divide(dividend, divisor))           # ans is 3 
