import math
import networkx as nx
import matplotlib.pyplot as plt


def variate(root, count, seen):
    if len(seen) == len(ways):
        variants.append([count + ways[root][start], seen + [start]])
    for i, val in enumerate(ways[root]):
        if i not in seen:
            variate(i, count + val, seen + [i])


ways = [
    [math.inf, 7, 7, 5, 1],
    [8, math.inf, 7, 4, 2],
    [5, 7, math.inf, 9, 4],
    [7, 8, 6, math.inf, 2],
    [5, 6, 9, 1, math.inf],
]

n = len(ways)
variants = []
start = 0
variate(start, 0, [start])
print(sorted(variants))
ans = sorted(variants)[0]

# Создание графа
G = nx.DiGraph()

# Добавляем узлы
G.add_nodes_from(range(1, n + 1))

# Добавляем ребра
for i in range(n):
    for j in range(n):
        if i != j:
            G.add_edge(i + 1, j + 1, weight=ways[i][j])

pos = nx.spring_layout(G)

# Все рёбра графа
edges = G.edges()

# Рёбра, которые нужно выделить
highlighted_edges = [(ans[1][i] + 1, ans[1][i + 1] + 1) for i in range(len(ans[1]) - 1)]
print(highlighted_edges)

# Визуализация всех рёбер (по умолчанию)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=1, alpha=0.8, edge_color='black', arrows=True, connectionstyle='arc3,rad=0.1', arrowsize=20)

# Визуализация выделенных рёбер (с другим цветом и толщиной)
nx.draw_networkx_edges(G, pos, edgelist=highlighted_edges, width=3, alpha=0.8, edge_color='blue', arrows=True, connectionstyle='arc3,rad=0.1', arrowsize=30)

# Визуализация узлов
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=500)

# Визуализация подписей узлов
nx.draw_networkx_labels(G, pos, font_size=16)

# Визуализация весов рёбер
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green', font_size=10, connectionstyle='arc3,rad=0.1')

# Показать граф
plt.show()
