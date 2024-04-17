k = int(input())
xt, yt = map(int, input().split())
xmin = xmax = xt
ymin = ymax = yt

for i in range(k - 1):
    xt, yt = map(int, input().split())
    xmin = min(xt, xmin)
    xmax = max(xt, xmax)
    ymin = min(yt, ymin)
    ymax = max(yt, ymax)

print(xmin, ymin, xmax, ymax)
