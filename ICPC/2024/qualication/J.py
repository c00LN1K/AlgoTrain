import math

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    m = math.ceil(math.log2(n))
    if math.ceil(m / 2) <= k:
        print(m)
    else:
        q = (k * 2) - 1
        print(q + math.ceil(n / (2 ** q)) - 1)
