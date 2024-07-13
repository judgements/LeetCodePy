"""
3. 无重复字符的最长子串
给定一个字符串 s , 请你找出其中不含有重复字符的最长子串的长度.
"""

import os
import sys

def lengthOfLongestSubstring(s: str) -> int:
    max_len, hashmap = 0, {}
    start = 0
    for end in range(len(s)):
        hashmap[s[end]] = hashmap.get(s[end], 0) + 1
        if len(hashmap) == end - start + 1:
            max_len = max(max_len, end - start + 1)
        # Step 4: 
        # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
        # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
        # 当窗口长度大于哈希表长度时候 (说明存在重复元素)，窗口不合法
        # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap)
        while end - start + 1 > len(hashmap):
            head = s[start]
            hashmap[head] -= 1
            if hashmap[head] == 0:
                del hashmap[head]
            start += 1
    return max_len

s1 = "abcbbcbb"     # ans is 3
s2 = "bbbbb"          # ans is 1
s3 = "pwwkew"            # ans is 3
print(lengthOfLongestSubstring(s1)) 
