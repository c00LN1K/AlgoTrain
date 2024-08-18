from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        def backtracking(now, temp):
            ans.append(temp.copy())
            for j in range(now + 1, len(nums)):
                temp.append(nums[j])
                backtracking(j, temp)
                temp.pop()

        for i in range(len(nums)):
            backtracking(i, [nums[i]])
        return ans


print(Solution().subsets([1, 2, 3]))
