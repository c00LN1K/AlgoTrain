class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def withAtMaxKDistinct(k):
            n = len(nums)
            left = 0
            right = 0
            d = {}
            result = 0
            while(right<n and left<=right):
                d[nums[right]] = d.get(nums[right], 0) + 1
                while(len(d) > k):
                    d[nums[left]] -= 1
                    if d[nums[left]] == 0:
                        del d[nums[left]]
                    left += 1
                result += (right - left + 1)
                right +=1
            return result

        return withAtMaxKDistinct(k) - withAtMaxKDistinct(k-1)