import math
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [True] * m
        for j in range(1, n):
            t = [False] * m
            for i in range(m):
                conditions = [
                    i > 0 and grid[i - 1][j - 1] < grid[i][j] and dp[i - 1],
                    grid[i][j - 1] < grid[i][j] and dp[i],
                    i + 1 < m and grid[i + 1][j - 1] < grid[i][j] and dp[i + 1],
                ]
                if any(conditions):
                    t[i] = True
            dp = t
            if not any(dp):
                return j - 1
        return n - 1


print(Solution().maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]))
