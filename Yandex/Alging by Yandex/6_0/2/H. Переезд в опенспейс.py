import math

n = int(input())
lst = list(map(int, input().split()))
t = 0
prefix_left = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_left[i] = prefix_left[i - 1] + t
    t += lst[i - 1]

t = 0
prefix_right = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    prefix_right[i] = prefix_right[i + 1] + t
    t += lst[i]

ans = math.inf
for i in range(n):
    ans = min(ans, prefix_left[i + 1] + prefix_right[i])
print(ans)
