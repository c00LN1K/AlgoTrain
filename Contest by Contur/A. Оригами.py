n, m = map(int, input().split())

ans = 0
while n % 2 == 0:
    ans += 1
    n //= 2

while m % 2 == 0:
    ans += 1
    m //= 2

print(ans)
