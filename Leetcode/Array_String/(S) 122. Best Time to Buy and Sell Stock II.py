class Solution(object):
    def maxProfit(self, prices):
        index = 0
        ans = 0
        for i in range(1, len(prices)):
            if prices[i - 1] > prices[i]:
                ans += prices[i - 1] - prices[index]
                index = i
        if prices[-2] <= prices[-1]:
            ans += prices[-1] - prices[index]
        return ans


print(Solution().maxProfit([1, 2, 3, 4, 5]))
