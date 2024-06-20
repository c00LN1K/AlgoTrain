import math

n = int(input())
rooms = list(map(int, input().split()))

m = int(input())
d = {}
for i in range(m):
    power, price = map(int, input().split())
    d[power] = min(price, d.setdefault(power, price))

powers = [math.inf] * (max(d) + 1)
powers[-1] = d[len(powers) - 1]
for i in range(len(powers) - 2, -1, -1):
    powers[i] = min(powers[i + 1], d.get(i, math.inf))
print(powers)
ans = 0
for i in range(n):
    ans += powers[rooms[i]]

print(ans)
