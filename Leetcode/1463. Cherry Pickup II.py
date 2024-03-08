class Solution(object):
    def cherryPickup(self, grid):
        dp = [[0] * len(grid[0]) for i in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                dp[i][j] = max([dp[i - 1][r] for r in range(max(0, j - 1), min(j + 2, len(grid[0])))]) + grid[i][j]
        print(dp)
        return 24
