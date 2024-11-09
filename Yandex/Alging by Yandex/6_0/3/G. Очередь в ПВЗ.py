n, b = map(int, input().split())
lst = list(map(int, input().split()))
curr = 0
ans = 0

for i in range(n):
    curr += lst[i]
    ans += curr
    curr = max(0, curr - b)

print(ans + curr)
