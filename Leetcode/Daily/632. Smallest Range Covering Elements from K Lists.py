import math
from collections import defaultdict
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        lst = [0] * len(nums)
        ans = [0, math.inf]
        is_end = False
        while True:
            minn, maxx = 0, 0
            for i in range(len(lst)):
                if lst[i] >= len(nums[i]):
                    is_end = True
                    break
                if nums[minn][lst[minn]] > nums[i][lst[i]]:
                    minn = i
                if nums[maxx][lst[maxx]] < nums[i][lst[i]]:
                    maxx = i
            if is_end:
                break
            if (ans[1] - ans[0] > nums[maxx][lst[maxx]] - nums[minn][lst[minn]]) or (
                    ans[1] - ans[0] == nums[maxx][lst[maxx]] - nums[minn][lst[minn]] and ans[0] > nums[minn][
                lst[minn]]):
                ans = [nums[minn][lst[minn]], nums[maxx][lst[maxx]]]
            lst[minn] += 1
        return ans

    def optimal_smallestRange(self, nums: List[List[int]]) -> List[int]:
        lst = sorted((el, i) for i, num in enumerate(nums) for el in num)
        l = 0
        ans = [0, math.inf]
        d = defaultdict(int)
        for r in range(len(lst)):
            num, index = lst[r]
            d[index] += 1
            while len(d) == len(nums):
                if ans[1] - ans[0] > lst[r][0] - lst[l][0]:
                    ans = [lst[l][0], lst[r][0]]
                d[lst[l][1]] -= 1
                if d[lst[l][1]] == 0:
                    d.pop(lst[l][1])
                l += 1
        return ans


print(Solution().optimal_smallestRange([[-5,-4,-3,-2,-1],[1,2,3,4,5]]))
