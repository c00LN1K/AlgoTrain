n = int(input())
lst = list(map(int, input().split()))
mini = lst[0]
curr = lst[0]
ans = lst[0]
for i in range(1, n):
    curr += lst[i]
    ans = max(ans, curr - mini, curr)
    mini = min(mini, curr)
print(ans)
