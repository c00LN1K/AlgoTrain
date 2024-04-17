from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        step = len(words[0])
        t = Counter(words)
        ans = []
        left = right = 0
        count = len(words)
        while right < (len(s) - step + 1):
            word = s[right:right + step]
            if word in t:
                if t.get(word):
                    t[word] -= 1
                    count -= 1
                else:
                    while t.get(word) == 0:
                        new_word = s[left:left + step]
                        t[new_word] += 1
                        count += 1
                        left += step
                    t[word] -= 1
                    count -= 1
            else:
                t = Counter(words)
                count = len(words)
                left = right = right + 1
                continue

            if count == 0:
                ans.append(left)
                t[s[left:left + step]] += 1
                count += 1
                left += step

            right += step

        return ans


print(Solution().findSubstring("aaaaaaaaaaaaaa",
                               ["aa","aa"]))
