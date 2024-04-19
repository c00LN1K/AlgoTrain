n = int(input())
ans = 0
for i in range(n):
    t = int(input())
    ans += t // 4
    t %= 4
    ans += 2 if t == 3 else t
print(ans)
