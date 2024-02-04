class Solution(object):
    def removeElement(self, nums, val):
        # two pointers
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[j] == val:
                j -= 1
                continue
            elif nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            i += 1
        return i + (0 if len(nums) == 0 or nums[i] == val else 1)

    def removeElement1(self, nums, val):
        # standard func in py
        while val in nums:
            nums.remove(val)
        return len(nums)
