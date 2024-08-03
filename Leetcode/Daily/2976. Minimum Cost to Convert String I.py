import math
from typing import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[math.inf] * 26 for _ in range(26)]
        for l, r, price in zip(original, changed, cost):
            graph[ord(l) - ord('a')][ord(r) - ord('a')] = min(price, graph[ord(l) - ord('a')][ord(r) - ord('a')])

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if i == j:
                        graph[i][j] = 0
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        ans = 0
        for l, r in zip(source, target):
            val = graph[ord(l) - ord('a')][ord(r) - ord('a')]
            if val == math.inf:
                return -1
            ans += val
        return ans


print(Solution().minimumCost('abcd', 'acbe', ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"],
                             [2, 5, 5, 1, 2, 20]))
