class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        def binary_search(left, right, target, is_left=True):
            while (left + 1) < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if is_left:
                        right = mid
                    else:
                        left = mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            if is_left:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
            else:
                if nums[right] == target:
                    return right
                elif nums[left] == target:
                    return left
            return -1

        return binary_search(0, len(nums) - 1, target), binary_search(0, len(nums) - 1, target, False)


print(Solution().searchRange([1], 1))
