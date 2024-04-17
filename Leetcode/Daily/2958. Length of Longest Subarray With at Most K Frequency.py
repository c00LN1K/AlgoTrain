class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        left = right = 0
        d = {}
        ans = 0
        while right < len(nums):
            if d.get(nums[right], 0) < k:
                d[nums[right]] = d.setdefault(nums[right], 0) + 1
                right += 1
            else:
                while d.get(nums[right], 0) == k:
                    ans = max(ans, right - left)
                    d[nums[left]] -= 1
                    left += 1
                if left > right:
                    right = left
        return ans


print(Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2))
