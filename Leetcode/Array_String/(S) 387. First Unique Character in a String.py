class Solution(object):
    def firstUniqChar(self, s):
        d = {}
        for i in s:
            d[i] = d.setdefault(i, 0) + 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1


print(Solution().firstUniqChar("loveleetcode"))
