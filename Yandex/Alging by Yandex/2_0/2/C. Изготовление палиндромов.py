s = input()
n = len(s)
ans = 0

for curr in range(len(s) // 2):
    if s[curr] != s[n - curr - 1]:
        ans += 1
print(ans)
