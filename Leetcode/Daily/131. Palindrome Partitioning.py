from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtracking(j, t):
            if j == len(s):
                ans.append(t)

            for r in range(j, len(s)):
                right = s[j:r + 1]
                if right and right == right[::-1]:
                    backtracking(r + 1, t + [right])

        backtracking(0, [])
        return ans


print(Solution().partition('aaa'))
