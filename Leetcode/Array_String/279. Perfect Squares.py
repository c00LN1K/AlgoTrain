class Solution(object):
    def numSquares(self, n):
        ans = 0
        if (int(n ** 0.5) + 1) * 3 == n:
            return 3
        while n:
            ans += 1
            cl_sq = int(n ** 0.5)
            if cl_sq == n ** 0.5:
                break
            else:
                n = n - cl_sq ** 2
        return ans


print(Solution().numSquares(12))
