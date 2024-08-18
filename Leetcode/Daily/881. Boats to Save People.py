from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        ans = 0
        left, right = 0, len(people) - 1
        while left <= right:
            now = limit
            ans += 1
            while left <= right and (now - people[left]) >= 0:
                now -= people[left]
                left += 1
            while left <= right and (now - people[right]) >= 0:
                now -= people[right]
                right -= 1

        return ans


print(Solution().numRescueBoats([3, 2, 3, 2, 2], 6))
