n, q = map(int, input().split())

lst = list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + lst[i - 1]

for _ in range(q):
    l, r = map(int, input().split())
    print(prefix[r]-prefix[l-1])