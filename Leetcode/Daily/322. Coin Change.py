class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0] * (amount + 1)
        for i in coins:
            if i <= amount:
                dp[i] = 1

        for i in range(amount + 1):
            t = [dp[i - coin] for coin in coins if (i - coin) > 0 and dp[i - coin]]
            if t:
                dp[i] = min(min(t) + 1, dp[i] if dp[i] else float('inf'))

        return dp[amount] if dp[amount] else -1


print(Solution().coinChange([2, 5], 1))
