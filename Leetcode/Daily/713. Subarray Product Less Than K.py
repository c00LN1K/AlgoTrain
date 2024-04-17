from collections import deque


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left = right = 0
        t = 1
        ans = 0
        while left < len(nums):
            while right < len(nums) and t * nums[right] < k:
                if right - left:
                    ans += 1
                t *= nums[right]
                right += 1
            if nums[left] < k:
                ans += 1
            t /= nums[left]
            left += 1
            if right - left > 1:
                ans += 1
            if left > right:
                right = left

        return ans


print(Solution().numSubarrayProductLessThanK([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19))
