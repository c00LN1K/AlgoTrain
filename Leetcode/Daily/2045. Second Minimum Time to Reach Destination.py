import math
from collections import defaultdict, deque
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(set)
        for st, end in edges:
            graph[st].add(end)
            graph[end].add(st)

        min_distance = [math.inf] * (n + 1)
        second_min_distance = [math.inf] * (n + 1)
        q = deque()
        q.append([1, 0])
        min_distance[1] = 0

        while q:
            node, t = q.popleft()
            if (t // change) % 2 == 1:
                t += change - t % change
            new_time = t + time
            for adj in graph[node]:
                if min_distance[adj] > new_time:
                    min_distance[adj], second_min_distance[adj] = new_time, min_distance[adj]
                    q.append((adj, new_time))

                elif min_distance[adj] < new_time < second_min_distance[adj]:
                    second_min_distance[adj] = new_time
                    q.append((adj, new_time))

        return second_min_distance[-1]


print(Solution().secondMinimum(5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5))
