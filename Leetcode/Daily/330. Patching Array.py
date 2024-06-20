from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        curr = 0
        i = 0
        for num in range(1, n + 1):
            while i < len(nums) and nums[i] <= num:
                curr += nums[i]
                i += 1
            if curr < num:
                curr += num
                ans += 1
        return ans


print(Solution().minPatches([1, 2, 2], 5))
