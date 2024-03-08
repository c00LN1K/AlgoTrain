class Solution(object):
    def trap(self, height):
        left = 0
        ans = 0
        peak = height.index(max(height))
        for i in range(min(peak + 1, len(height))):
            if height[left] <= height[i]:
                left = i
            else:
                ans += height[left] - height[i]
        left = len(height) - 1
        for i in range(len(height) - 1, max(-1, peak - 1), -1):
            if height[left] <= height[i]:
                left = i
            else:
                ans += height[left] - height[i]
        return 6
