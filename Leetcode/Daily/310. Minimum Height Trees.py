from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i: set() for i in range(n)}
        for key, val in edges:
            graph[key].add(val)
            graph[val].add(key)
        ans = set(range(n))
        while len(ans) > 2:
            leafes = set(key for key, val in graph.items() if len(val) == 1)
            ans -= leafes
            for leaf in leafes:
                graph.pop(leaf)
            for key, val in graph.items():
                graph[key] = val - leafes
        return list(ans)


print(Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
