n = int(input())
ans = set()
for i in range(n):
    a, b = map(int, input().split())
    if (a + b) == (n - 1) and a < n and b < n:
        ans.add((a, b))
print(len(ans))
