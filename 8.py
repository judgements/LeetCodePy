"""
8. 字符串转换整数
"""

import os
import sys

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Automaton:
    def __init__(self) -> None:
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start' : ['start', 'sign', 'number', 'start'],
            'sign' : ['end', 'end', 'number', 'end'],
            'number' : ['end', 'end', 'number', 'end'],
            'end' : ['end', 'end', 'end', 'end']
        }
    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit:
            return 2
        return 3
    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'sign':
            self.sign = 1 if c == '+' else -1
        if self.state == 'number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else max(self.ans, INT_MIN)

def myAtoi(s: str) -> int:
    autoMaton = Automaton()
    for i in s:
        autoMaton.get(i)
    return autoMaton.sign * autoMaton.ans

s1 = "42"          # ans is 42
s2 = "   -42"         # ans is -42
s = "4193 with words"    # ans is 4193
print(myAtoi(s2))
