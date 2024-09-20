d = int(input())
x, y = map(int, input().split())

if (d > 0 and x >= 0 and 0 <= y <= -x + d) or (d < 0 and x <= 0 and y <= 0 and y <= -x + d):
    print(0)
else:
    dA = x ** 2 + y ** 2
    dB = (x - d) ** 2 + y ** 2
    dC = x ** 2 + (y - d) ** 2
    if dA <= dB <= dC:
        print(1)
    elif dB <= dC:
        print(2)
    else:
        print(3)

