from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        ans = len(nums)
        for i in range(1, len(nums) - 1):
            left = self.lengthOfLIS(nums[:i], nums[i])
            right = self.lengthOfLIS(nums[i + 1:][::-1], nums[i])
            print(f'num: {nums[i]}, left: {left}, right:{right}, res: {len(nums) - left - right - 1}')
            if left and right:
                ans = min(len(nums) - left - right - 1, ans)
        return ans

    def lengthOfLIS(self, nums, target):
        # Binary search approach
        n = len(nums)
        ans = []

        # Initialize the answer list with the
        # first element of nums

        for i in range(n):
            if nums[i] >= target:
                continue
            if not ans or nums[i] > ans[-1]:
                # If the current number is greater
                # than the last element of the answer
                # list, it means we have found a
                # longer increasing subsequence.
                # Hence, we append the current number
                # to the answer list.
                ans.append(nums[i])
            else:
                # If the current number is not
                # greater than the last element of
                # the answer list, we perform
                # a binary search to find the smallest
                # element in the answer list that
                # is greater than or equal to the
                # current number.
                low = 0
                high = len(ans) - 1
                while low < high:
                    mid = low + (high - low) // 2
                    if ans[mid] < nums[i]:
                        low = mid + 1
                    else:
                        high = mid
                # We update the element at the
                # found position with the current number.
                # By doing this, we are maintaining
                # a sorted order in the answer list.
                ans[low] = nums[i]

        # The length of the answer list
        # represents the length of the
        # longest increasing subsequence.
        return len(ans)


print(Solution().minimumMountainRemovals([100, 92, 89, 77, 74, 66, 64, 66, 64]))
