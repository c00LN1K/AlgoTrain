class Solution(object):
    def maxProfit(self, prices):
        index = 0
        ans = 0
        for i, price in enumerate(prices):
            if (price - prices[index]) > ans:
                ans = price - prices[index]
            elif prices[index] > price:
                index = i
        return ans
