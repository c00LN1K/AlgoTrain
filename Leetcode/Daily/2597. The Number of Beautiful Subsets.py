from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.ans = 0

        def backtracking(now, s):
            self.ans += 1
            for i in range(now + 1, len(nums)):
                if (k + nums[i]) not in s and (nums[i] - k) not in s:
                    ss = s.copy()
                    ss.add(nums[i])
                    backtracking(i, ss)

        for j in range(len(nums)):
            backtracking(j, {nums[j]})
        return self.ans


print(Solution().beautifulSubsets([10, 4, 5, 7, 2, 1], 3))
