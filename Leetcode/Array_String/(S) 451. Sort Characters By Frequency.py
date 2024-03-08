class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = d.setdefault(i, 0) + 1
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        ans = []
        for key, value in d.items():
            ans.append(key * value)
        return ''.join(ans)


print(Solution().frequencySort('tree'))
