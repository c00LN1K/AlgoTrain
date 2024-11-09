k = int(input())
x, y = map(int, input().split())
x1 = x2 = x
y1 = y2 = y
for _ in range(k - 1):
    x, y = map(int, input().split())
    x1, x2 = max(x1, x), min(x2, x)
    y1, y2 = max(y1, y), min(y2, y)

print(x2, y2, x1, y1)
