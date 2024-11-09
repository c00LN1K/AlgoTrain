from collections import defaultdict
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        prefix_left = defaultdict(list)
        prefix_right = defaultdict(list)
        prefix_left[0] = [-1]
        prefix_right[0] = [n]
        curr_left = curr_right = 0
        ans = n
        for i in range(n):
            curr_left = (curr_left + nums[i]) % p
            curr_right = (curr_right + nums[n - i - 1]) % p
            prefix_left[curr_left].append(i)
            prefix_right[curr_right].append(n - i - 1)

        curr_left = curr_right = 0
        for i in range(n // 2 + 2):
            curr_left = (curr_left + nums[i]) % p
            target_left = (p - curr_left) % p
            curr_right = (curr_right + nums[n - i - 1]) % p
            target_right = (p - curr_right) % p

            while prefix_right[target_left] and prefix_right[target_left][-1] <= i:
                prefix_right[target_left].pop()

            if prefix_right[target_left]:
                ans = min(ans, prefix_right[target_left][-1] - i - 1)

            while prefix_left[target_right] and prefix_left[target_right][-1] >= (n - i - 1):
                prefix_left[target_right].pop()

            if prefix_left[target_right]:
                ans = min(ans, (n - i - 1) - prefix_left[target_right][-1] - 1)

            if ans == 0:
                break

        return -1 if ans == n else ans


print(Solution().minSubarray([8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2], 148))
