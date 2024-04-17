class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        left = right = 0
        ans = 0
        target = max(nums)
        num_target = 0
        while left < len(nums):
            while right < len(nums) and num_target != k:
                if nums[right] == target:
                    num_target += 1
                right += 1
            if num_target == k:
                ans += len(nums) - right + 1
            if nums[left] == target:
                num_target -= 1
            left += 1
        return ans


print(Solution().countSubarrays([1, 3, 2, 3], 3))
