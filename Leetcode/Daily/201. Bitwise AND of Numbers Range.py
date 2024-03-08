class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if len(bin(left)) != len(bin(right)):
            return 0
        ans = left
        while left <= right:
            ans &= left
            left += 1
        return ans


print(Solution().rangeBitwiseAnd(130, 222))
