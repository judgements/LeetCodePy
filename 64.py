"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格 grid , 请找出一条从左上角到右下角的路径, 使得路径上的数字总和为最小.
"""

import os, sys
from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    if grid is None or grid[0] is None:
        return 0
    m, n = len(grid), len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if i == 0 and j > 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            if i > 0 and j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[m-1][n-1]
grid1 = [[1,3,1],[1,5,1],[4,2,1]]       # ans is 7
grid2 = [[1,2,3],[4,5,6]]              # ans is 12
print(minPathSum(grid2))
