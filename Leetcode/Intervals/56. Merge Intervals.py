class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        s = set()
        for left, right in intervals:
            print(s)
            if left in s and right in s:
                continue
            elif left in s:
                while right not in s and left <= right:
                    s.add(right)
                    right -= 1
            else:
                while left not in s and left <= right:
                    s.add(left)
                    left += 1

        s = sorted(s)
        start = 0
        ans = []
        print(s)
        for i in range(1, len(s)):
            if s[i - 1] != s[i] - 1:
                ans.append([s[start], s[i - 1]])
                start = i
        return ans + [[s[start], s[-1]]]


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
