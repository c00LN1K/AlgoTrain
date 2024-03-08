class Solution(object):
    def hIndex(self, citations):
        start, end = 0, len(citations)
        citations.sort(reverse=True)
        ans = 0
        while start < end:
            mid = (start + end) // 2
            k = 0
            for citation in citations:
                if citation >= mid:
                    k += 1
                else:
                    break
            if k == mid:
                return mid
            if k < mid:
                end = mid - 1
            else:
                ans = max(ans, mid)
                start = mid + 1
        return ans
