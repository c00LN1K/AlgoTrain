import math


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        last = {}
        for j in range(len(ring)):
            if ring[j] == key[0]:
                last[j] = min(j, len(ring) - j) + 1
        for i in range(1, len(key)):
            t = {}
            for j in range(len(ring)):
                if ring[j] == key[i]:
                    t[j] = math.inf
                    for z, val in last.items():
                        t[j] = min(t[j], val + min(abs(z - j), len(ring) - abs(z - j)) + 1)
            last = t
        return min(last.values())


print(Solution().findRotateSteps('nyngl', 'yyynnnnnnlllggg'))
