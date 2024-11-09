class Solution:
    def shortestPalindrome(self, s: str) -> str:
        count = self.kmp(s, s[::-1])
        return s[count:][::-1] + s

    def kmp(self, patt: str, txt: str) -> int:
        new_string = patt + '@' + txt
        pi = [0] * len(new_string)
        i = 1
        k = 0
        while i < len(new_string):
            if new_string[i] == new_string[k]:
                k += 1
                pi[i] = k
                i += 1
            else:
                if k > 0:
                    k = pi[k - 1]
                else:
                    pi[i] = 0
                    i += 1
        return pi[-1]


print(Solution().shortestPalindrome('abbb'))

# abbb#bbba