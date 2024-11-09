t = 72 + 3
tasks = [
    (18, 8), (12, 4), (20, 7), (23, 11), (12, 5), (10, 6), (11, 5), (9, 10), (7, 8), (9 + 1, 7 + 8),
]
n = len(tasks)
dp = [[0] * (t + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, t + 1):
        dp[i][j] = max(
            dp[i - 1][j], dp[i - 1][j - tasks[i - 1][0]] + tasks[i - 1][1] if (j - tasks[i - 1][0]) >= 0 else 0,
        )

print(f'Res: {dp[-1][-1]}')

ans = []
size = t
for i in range(n, 0, -1):
    if dp[i][size] != dp[i - 1][size] or dp[i][size] != dp[i - 1][size]:
        ans.append(i)
        size -= tasks[i - 1][0]

print(f'Nodes: {ans}')
