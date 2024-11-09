n = int(input())

variants = int(input())
desk = int(input()) - 1
pos = int(input()) - 1

total_pos = desk * 2 + pos
up_pos, down_pos = total_pos - variants, total_pos + variants
if up_pos < 0 and down_pos >= n:
    print(-1)
elif down_pos >= n:
    print(up_pos // 2 + 1, up_pos % 2 + 1)
elif up_pos < 0:
    print(down_pos // 2 + 1, down_pos % 2 + 1)
else:
    if down_pos // 2 - total_pos // 2 <= total_pos // 2 - up_pos // 2:
        print(down_pos // 2 + 1, down_pos % 2 + 1)
    else:
        print(up_pos // 2 + 1, up_pos % 2 + 1)
