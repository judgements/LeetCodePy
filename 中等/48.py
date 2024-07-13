"""
48. 旋转图像
给定一个 n * n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""

import os
import sys
from typing import List

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    matrix_copy = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_copy[j][n-i-1] = matrix[i][j]
    print(matrix_copy)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
