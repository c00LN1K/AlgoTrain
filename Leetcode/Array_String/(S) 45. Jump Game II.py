class Solution(object):
    def jump(self, nums):
        if (len(nums) <= 1):
            return 0
        lp = 0
        rp = 0
        res = 0
        while (rp < len(nums) - 1):
            new_rp = rp
            while (lp <= rp):
                new_rp = max(new_rp, lp + nums[lp])
                lp += 1
            lp = rp + 1
            rp = new_rp
            res += 1
        return res


print(Solution().jump([2, 3, 1, 1, 4]))
