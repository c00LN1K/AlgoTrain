first = input()
second = input()
pull = set()

for i in range(len(second) - 1):
    pull.add(second[i] + second[i + 1])

ans = 0

for i in range(len(first) - 1):
    if first[i] + first[i + 1] in pull:
        ans += 1

print(ans)
