from collections import Counter

n = int(input())
nums = list(map(int, input().split()))

c = Counter(nums)
ans = 0

for k in c:
    ans = max(ans, c[k] + c.get(k + 1, 0), c.get(k - 1, 0) + c[k])

print(len(nums) - ans)
