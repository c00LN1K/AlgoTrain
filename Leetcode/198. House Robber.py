def rob(nums: list):
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]
    for i in range(2, len(nums) + 1):
        dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

    return dp[-1]


print(rob([1, 2, 3, 1]))
