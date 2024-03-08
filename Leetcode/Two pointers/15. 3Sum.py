class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        for i, val in enumerate(nums):
            left, right = 0, len(nums) - 1
            while left < right:
                if left == i:
                    left += 1
                elif right == i:
                    right -= 1
                elif (nums[left] + nums[right]) == -val:
                    ans.add(tuple(sorted([nums[left], nums[right], val])))
                    left += 1
                    right -= 1
                elif (nums[left] + nums[right]) < -val:
                    left += 1
                else:
                    right -= 1
        return list(ans)


print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
