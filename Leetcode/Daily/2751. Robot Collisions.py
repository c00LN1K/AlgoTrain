from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        data = sorted(zip(positions, healths, directions, range(len(healths))))
        stack = []
        for position, health, direction, index in data:
            if direction == 'R':
                stack.append([positions, health, direction, index])
                continue
            while stack:
                last = stack[-1]
                if last[1] > health:
                    health = 0
                    last[1] -= 1
                    healths[last[3]] -= 1
                    break
                elif stack[-1][1] < health:
                    healths[stack[-1][3]] = 0
                    health -= 1
                    stack.pop()
                else:
                    health, healths[stack[-1][3]] = 0, 0
                    stack.pop()
                    break
            healths[index] = health
        return list(filter(lambda x: x, healths))


print(Solution().survivedRobotsHealths([4, 33, 36, 8, 38, 31], [47, 28, 39, 25, 48, 48], "LRLRLR"))
