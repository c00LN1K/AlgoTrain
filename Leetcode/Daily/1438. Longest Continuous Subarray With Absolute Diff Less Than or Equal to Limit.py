from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        incr = deque()
        decr = deque()
        l, ans = 0, 0
        for r in range(len(nums)):
            while incr and incr[-1] > nums[r]:
                incr.pop()
            while decr and decr[-1] < nums[r]:
                decr.pop()
            incr.append(nums[r])
            decr.append(nums[r])
            while decr[0] - incr[0] > limit:
                if incr[0] == nums[l]:
                    incr.popleft()
                if decr[0] == nums[l]:
                    decr.popleft()
                l += 1
            ans = max(ans, r - l + 1)
        return ans

print(Solution().longestSubarray([8, 2, 4, 7], 4))