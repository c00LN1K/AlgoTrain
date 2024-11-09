n = int(input())
pool = set(range(1, n + 1))

while True:
    k = input()
    if k == 'HELP':
        break
    was = set(map(int, k.split()))
    if input() == 'YES':
        pool &= was
    else:
        pool -= was
print(*sorted(pool))