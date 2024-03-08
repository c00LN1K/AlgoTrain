class Solution(object):
    def canJump(self, nums):
        end = len(nums) - 1

        def dfs(start):
            if start == end:
                return True
            if start > end:
                return False
            else:
                for move in range(1, nums[start] + 1):
                    res = dfs(start + move)
                    if res:
                        return res

        return dfs(0)

    def canJump2(self, nums):
        end = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= (end - i):
                end = i
        return end == 0


print(Solution().canJump([2, 0, 0]))
