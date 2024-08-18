from collections import defaultdict, deque


def topological_sort(graph):
    rating = [0] * k
    for key in graph:
        for node in graph[key]:
            rating[node - 1] += 1

    q = deque()
    for i, val in enumerate(rating, 1):
        if not val:
            q.append(i)
    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for adj in graph[node]:
            rating[adj - 1] -= 1
            if not rating[adj - 1]:
                q.append(adj)
    if len(res) == k:
        return res


k, m = map(int, input().split())
conditions = set(tuple(map(int, input().split())) for _ in range(m))
graph = defaultdict(list)

for st, end in conditions:
    graph[st].append(end)

rows = topological_sort(graph)

if rows is None:
    print('NO')
else:
    print('YES')
    print(*rows)
