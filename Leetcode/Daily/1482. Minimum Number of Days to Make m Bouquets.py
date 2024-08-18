from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < k * m:
            return -1

        l, r = 0, max(bloomDay)

        def check(days):
            curr = 0
            l = 0
            count = 0
            for r in range(len(bloomDay)):
                if bloomDay[r] <= days:
                    count += 1
                if r - l + 1 == k:
                    if count == k:
                        curr += 1
                        if m <= curr: return True
                        l = r + 1
                        count = 0
                    else:
                        if bloomDay[l] <= days:
                            count -= 1
                        l += 1
            return False

        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


print(Solution().minDays([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2))
