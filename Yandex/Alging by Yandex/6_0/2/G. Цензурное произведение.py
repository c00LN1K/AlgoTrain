n, c = map(int, input().split())
s = input()
l = 0
a = b = 0
ans = 0
counter = 0
for r in range(n):
    if s[r] == 'a':
        a += 1
    if s[r] == 'b':
        b += 1
        counter += a
    while l <= r and counter > c:
        if s[l] == 'a':
            a -= 1
            counter -= b
        if s[l] == 'b':
            b -= 1
        l += 1
    if counter <= c:
        ans = max(ans, r - l + 1)
print(ans)
