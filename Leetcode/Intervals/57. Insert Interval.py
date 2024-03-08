class Solution():
    def solve(self, intervals, new_interval):
        i = 0
        ans = []

        def find_pos(curr, is_left=False):
            nonlocal i
            while i < len(intervals):
                left, right = intervals[i]
                if curr < left:
                    return curr
                elif left <= curr <= right:
                    if is_left:
                        return left
                    i += 1
                    return right
                i += 1
            return curr

        l, r = new_interval
        l = find_pos(l, True)
        ans += intervals[:i]
        r = find_pos(r)
        ans.append([l, r])
        ans += intervals[i:]

        return ans


print(Solution().solve([[1, 3], [6, 9]], [2, 5]))
