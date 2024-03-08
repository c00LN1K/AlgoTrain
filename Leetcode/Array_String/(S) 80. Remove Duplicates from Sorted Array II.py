class Solution(object):
    def removeDuplicates(self, nums):
        # Two pointers
        left, right = 0, 1
        k = 1
        index = 1
        while (right != len(nums)):
            if nums[left] == nums[right] and k > 1:
                right += 1
            else:
                if nums[left] == nums[right]:
                    k += 1
                else:
                    k = 1
                nums[index] = nums[right]
                left = right
                right += 1
                index += 1
        return index
