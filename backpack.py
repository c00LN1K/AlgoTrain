import heapq

things = [
    (1, 6, 5, 5 / 6),
    (2, 4, 3, 3 / 4),
    (3, 3, 1, 1 / 3),
    (4, 2, 3, 3 / 2),
    (5, 5, 6, 6 / 5),
    (6, 7, 9, 9 / 7),
    (7, 4, 8, 8 / 4),
    (8, 2, 6, 6 / 2),
    (9, 9, 10, 10 / 9),
    (10, 3, 7, 7 / 3),
    (11, 5, 9, 9 / 5),
    (12, 6, 9, 9 / 6),
    (13, 2, 5, 5 / 2),
    (14, 4, 5, 5 / 4),
    (15, 5, 10, 10 / 5),
    (16, 7, 8, 8 / 7),
    (17, 4, 7, 7 / 4),
    (18, 9, 10, 10 / 9),
    (19, 5, 7, 7 / 10),
    (20, 3, 6, 6 / 3),
]
size = 30

# things = [
#     (1, 18, 8, 8 / 18),
#     (2, 12, 4, 4 / 12),
#     (3, 20, 7, 7 / 20),
#     (4, 23, 11, 11 / 23),
#     (5, 12, 5, 5 / 12),
#     (6, 10, 6, 6 / 10),
#     (7, 11, 5, 5 / 11),
#     (8, 9, 10, 10 / 9),
#     (9, 7, 8, 8 / 7),
# ]
# size = 72

things.sort(key=lambda x: x[-1], reverse=True)

heap = []


def get_mark(start, size):
    l = start
    t = 0
    d1 = 0
    while l < len(things) and t + things[l][1] <= size:
        t += things[l][1]
        d1 += things[l][2]
        l += 1
    d2 = things[l][-1] * (size - t) if l < len(things) else 0
    return -(d1 + d2)


heap.append((get_mark(0, size), 0, []))
heapq.heapify(heap)
ans = [0, [], 0]
while heap:
    mark, index, taken = heapq.heappop(heap)
    d0 = -sum(things[thing][2] for thing in taken)
    new_size = size - sum(things[thing][1] for thing in taken)
    if new_size >= 0 and ans[0] <= -d0:
        ans = [-d0, taken, new_size]
    if index + 1 < len(things):
        if new_size > 0:
            heapq.heappush(heap, (get_mark(index, new_size) + d0, index + 1, taken + [index]))
            heapq.heappush(heap, (get_mark(index + 1, new_size) + d0, index + 1, taken))

print(ans)
print(f'Максимальная стоимость = {ans[0]}')
print('Предметы')
for index in ans[1]:
    print(things[index][0], end=' ')
print(f'\nОсталось места - {ans[2]}')
