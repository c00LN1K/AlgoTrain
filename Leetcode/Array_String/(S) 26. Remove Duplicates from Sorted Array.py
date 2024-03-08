class Solution(object):
    def removeDuplicates(self, nums: list):
        s = set(nums)
        nums[:len(s)] = sorted(s)
        return len(s)

    def removeDuplicates1(self, nums: list):
        left, right = 0, 1
        index = 1
        while (right != len(nums)):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[index] = nums[right]
                left = right
                right += 1
                index += 1
        return index

    # def left_binary_search(self, arr, needle):
    #     start, end = 0, len(arr) - 1
    #     while (start + 1) < end:
    #         mid = (start + end) // 2
    #         if needle < arr[mid]:
    #             start = mid
    #         else:
    #             end = mid
    #     if arr[start] == needle:
    #         return start
    #     if arr[end] == needle:
    #         return end
    #     return -1
