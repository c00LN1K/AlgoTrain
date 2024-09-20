from collections import deque, defaultdict


def min_completion_time(n, durations, dependencies):
    graph = defaultdict(list)
    in_degree = [0] * n
    finish_time = [0] * n
    queue = deque()

    for u in range(n):
        for v in dependencies[u]:
            graph[v].append(u)
            in_degree[u] += 1

    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
            finish_time[i] = durations[i]

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
            finish_time[v] = max(finish_time[v], finish_time[u] + durations[v])

    return max(finish_time)


n = int(input())
durations = []
dependencies = {}
for i in range(n):
    t = input().split()
    durations.append(int(t[0]))
    dependencies[i] = [int(t[i]) - 1 for i in range(1, len(t))]

print(min_completion_time(n, durations, dependencies))
