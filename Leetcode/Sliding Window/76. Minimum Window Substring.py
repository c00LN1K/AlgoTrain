from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = 0
        temp = Counter(t)
        count = len(t)
        min_length = float('inf')
        ans_start = 0
        while right < len(s):
            if temp.get(s[right]) is not None:
                if temp.get(s[right]) > 0:
                    count -= 1
                temp[s[right]] -= 1

            right += 1

            while count == 0:
                if min_length > (right - left):
                    ans_start = left
                    min_length = right - left
                if temp.get(s[left]) is not None:
                    if temp.get(s[left]) == 0:
                        count += 1
                    temp[s[left]] += 1
                left += 1

        return '' if min_length == float('inf') else s[ans_start:ans_start + min_length]


print(Solution().minWindow("ADOBECODEBANC", 'ABC'))
