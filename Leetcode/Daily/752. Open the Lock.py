from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0
        now = [0] * 4
        seen = set(map(lambda x: tuple(map(int, x)), deadends))
        target = list(map(int, target))
        d = deque()
        d.append((now, 0))
        seen.add(tuple(now))
        while d:
            curr, moves = d.popleft()
            for i in range(4):
                t = curr[::]
                t[i] = (t[i] + 1) % 10
                if t == target:
                    return moves + 1
                if tuple(t) not in seen:
                    d.append((t, moves + 1))
                    seen.add(tuple(t))
                t = curr[::]
                if t[i] == 0:
                    t[i] = 9
                else:
                    t[i] -= 1
                if t == target:
                    return moves + 1
                if tuple(t) not in seen:
                    d.append((t, moves + 1))
                    seen.add(tuple(t))
        return -1


print(Solution().openLock(["1002","1220","0122","0112","0121"], '1200'))
