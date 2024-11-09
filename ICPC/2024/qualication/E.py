n = int(input())
points = set()
x_point = set()
for i in range(n):
    x, y = map(int, input().split())
    if y == 0:
        x_point.add((x, y))
    else:
        points.add((x, y))

if len(x_point) < 2 or len(points) == 0:
    print(0)
else:
    points = sorted(points, key=lambda x: abs(x[1]))
    x_point = sorted(x_point, key=lambda x: x[0])
    print(abs(x_point[0][0] - x_point[-1][0]) * abs(points[-1][1]) / 2)
