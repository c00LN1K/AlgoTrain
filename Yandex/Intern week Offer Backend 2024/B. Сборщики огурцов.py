n = int(input())
groups = []
avg = []
for i in range(n):
    m, *group = map(int, input().split())
    groups.append(group)
    avg.append(sum(group) / m)

print(groups)
print(avg)

# находить avg группы (округлять по правилам математики?)

