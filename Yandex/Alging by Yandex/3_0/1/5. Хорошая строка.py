n = int(input())
prev = 0
ans = 0
for i in range(n):
    curr = int(input())
    ans += min(curr, prev)
    prev = curr
print(ans)