class Solution(object):
    def strStr(self, haystack, needle):
        st = end = -1
        for i, val in enumerate(haystack):
            if val == needle[end - st]:
                if st == -1:
                    st = i
                end = i + 1
                if (end - st) == len(needle):
                    return st
            else:
                if st != -1:
                    st = end = -1
        return -1


print(Solution().strStr('mississippi', 'issip'))
