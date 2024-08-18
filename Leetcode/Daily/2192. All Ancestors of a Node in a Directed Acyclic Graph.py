from collections import defaultdict
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [[] for _ in range(n)]
        graph = [[] for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])

        def dfs(st, curr):
            for node in graph[curr]:
                if not ancestors[node] or ancestors[node][-1] != st:
                    ancestors[node].append(st)
                    dfs(st, node)

        for i in range(n):
            dfs(i, i)

        return ancestors


print(Solution().getAncestors(8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]))
