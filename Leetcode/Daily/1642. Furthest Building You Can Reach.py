class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        was = []
        p = 0
        ladders1 = ladders
        bricks1 = bricks
        for end in range(1, len(heights)):
            if heights[end - 1] < heights[end]:
                dif = heights[end] - heights[end - 1]
                was.append(dif)
                if dif <= bricks:
                    bricks -= dif
                elif ladders:
                    ladders -= 1
                else:
                    break

print(Solution().furthestBuilding([14, 3, 19, 3], 17, 0))
