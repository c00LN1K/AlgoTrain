x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x, y = int(input()), int(input())

if x <= x1:
    if y >= y2:
        print('NW')
    elif y1 < y < y2:
        print('W')
    else:
        print('SW')
elif x1 < x < x2:
    if y2 < y:
        print('N')
    elif y1 > y:
        print('S')
else:
    if y >= y2:
        print('NE')
    elif y1 < y < y2:
        print('E')
    else:
        print('SE')
