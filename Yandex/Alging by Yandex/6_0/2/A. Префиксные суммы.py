n = int(input())
prefix = [0] * n
for i, el in enumerate(map(int, input().split())):
    prefix[i] = prefix[i - 1] + el

print(*prefix)
