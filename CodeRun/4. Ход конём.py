n, m = map(int, input().split())

dp = [[0] * (m + 2) for i in range(n + 2)]

dp[2][2] = 1

for i in range(3, n + 2):
    for j in range(3, m + 2):
        dp[i][j] = dp[i - 1][j - 2] + dp[i - 2][j - 1]

print(dp[-1][-1])
