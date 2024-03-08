class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        ans = []
        for i in range(numRows):
            t = (numRows - 1) * 2 - i
            j = i
            while j < len(s):
                ans.append(s[j])
                j += (numRows - 1) * 2
                if 0 < t < len(s) and t not in ((numRows - 1) * 2, numRows - 1):
                    ans.append(s[t])
                    t += (numRows - 1) * 2
        return ''.join(ans)


print(Solution().convert('Q', 1))
