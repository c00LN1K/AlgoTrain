import math
from collections import deque
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pole = [[math.inf] * n for _ in range(n)]
        seen = set()
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    seen.add((i, j))

        dist = -1
        while q:
            dist += 1
            for i in range(len(q)):
                i, j = q.popleft()
                pole[i][j] = dist
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = dx + i, dy + j
                    if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
                        seen.add((x, y))
                        q.append((x, y))

        def dfs(root, end, seen):
            if root == end:
                return True
            x, y = root
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                xx = dx + x
                yy = dy + y
                if 0 <= xx < n and 0 <= yy < n and (xx, yy) not in seen and pole[xx][yy] >= mid:
                    seen.add((xx, yy))
                    res = dfs((xx, yy), end, seen)
                    if res:
                        return res

        left, right = 0, dist + 1
        while left < right:
            mid = (left + right + 1) // 2
            if pole[0][0] >= mid and pole[-1][-1] >= mid and dfs((0, 0), (n - 1, n - 1), {(0, 0)}):
                left = mid
            else:
                right = mid - 1
        return left


print(Solution().maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]]))
