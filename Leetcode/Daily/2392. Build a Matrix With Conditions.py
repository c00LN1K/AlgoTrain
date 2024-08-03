from collections import deque, defaultdict
from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(graph):
            rating = [0] * k
            for key in graph:
                for node in graph[key]:
                    rating[node - 1] += 1

            q = deque()
            for i, val in enumerate(rating, 1):
                if not val:
                    q.append(i)
            res = []
            while q:
                node = q.popleft()
                res.append(node)
                for adj in graph[node]:
                    rating[adj - 1] -= 1
                    if not rating[adj - 1]:
                        q.append(adj)
            if len(res) == k:
                return res

        graph = defaultdict(list)
        for st, end in rowConditions:
            graph[st].append(end)
        rows = topological_sort(graph)
        if rows is None:
            return []

        graph = defaultdict(list)
        for st, end in colConditions:
            graph[st].append(end)
        cols = topological_sort(graph)
        if cols is None:
            return []

        ans = [[0] * k for _ in range(k)]
        d = {}
        for i, val in enumerate(rows):
            if val not in d:
                d[val] = [0, 0]
            d[val][0] = i

        for i, val in enumerate(cols):
            if val not in d:
                d[val] = [0, 0]
            d[val][1] = i

        for key, val in d.items():
            ans[val[0]][val[1]] = key
        return ans


print(Solution().buildMatrix(3, [[1, 2], [3, 2]], [[2, 1], [3, 2]]))
