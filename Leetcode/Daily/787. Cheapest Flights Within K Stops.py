import math
from collections import deque


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        ways = {}
        for i, j, price in flights:
            ways[i] = ways.setdefault(i, []) + [(j, price)]

        ans = [math.inf] * n
        ans[src] = 0
        d = deque()
        d.append((src, 0, k + 1))
        while d:
            src, cost, temp_k = d.popleft()
            for next, price in ways.get(src, []):
                if temp_k and ans[next] > (price + cost):
                    ans[next] = price + cost
                    d.append((next, price + cost, temp_k - 1))
        return ans[dst]


print(Solution().findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))
