n = int(input())
cuts = []

for i in range(n):
    l, r = map(int, input().split())
    cuts.append((l, r))

cuts.sort(key=lambda x: x[1])

k = 1
champion_index = 0
for i in range(1, n):
    if cuts[champion_index][1] < cuts[i][0]:
        champion_index = i
        k += 1

print(k)
