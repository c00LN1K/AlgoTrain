n = int(input())
d = {}
i = 0
topics = {}
while n != i:
    num = int(input())
    if num == 0:
        topic = input()
        message = input()
        topics[i] = [0, topic]
        d[i] = i
    else:
        message = input()
        d[i] = num - 1
    i += 1

for key, parent in d.items():
    while parent not in topics:
        parent = d[parent]
    topics[parent][0] += 1
print(sorted(topics.items(), key=lambda x: (-x[1][0], x[0]))[0][1][1])
