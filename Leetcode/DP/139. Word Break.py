from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(now):
            if not now:
                return True
            for word in wordDict:
                if now.startswith(word):
                    res = dfs(now[len(word):])
                    if res:
                        return True
            return False

        return dfs(s)


print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
