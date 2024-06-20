n = int(input())
sectors = list(map(int, input().split()))
a, b, k = map(int, input().split())

a_moves = a // k + (-1 if a % k == 0 else 0)
b_moves = b // k + (-1 if b % k == 0 else 0)
length = len(sectors)

if a_moves == b_moves:
    a_moves %= len(sectors)
    print(max(sectors[a_moves], sectors[-a_moves]))

else:
    if b_moves - a_moves >= length:
        print(max(sectors))
    else:
        a_moves %= length
        b_moves %= length
        if a_moves < b_moves:
            print(max(sectors[a_moves:b_moves + 1] + sectors[length - b_moves:length - a_moves + 1]))
        else:
            print(max(sectors[a_moves:] + sectors[:b_moves + 1] + sectors[:length - a_moves + 1] + sectors[
                                                                                                   length - b_moves:]))
