s = input()
q = int(input())
letters = list(s)
for _ in range(q):
    l, r, x = map(int, input().split())
    x_small, x_big = x // 2, x % 2
    for i in range(l - 1, r):
        if letters[i].isupper():
            t = (ord(letters[i]) - 65 + x_small) % 26 + 65
            if x_big:
                if t == ord('Z'):
                    t = 97
                else:
                    t += 33
        else:
            t = (ord(letters[i]) - 97 + x_small) % 26 + 97
            if x_big:
                t -= 32
        letters[i] = chr(t)

print(''.join(letters))
