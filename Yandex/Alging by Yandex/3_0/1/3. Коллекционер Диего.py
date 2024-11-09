n = int(input())
marks = sorted(set(map(int, input().split())), reverse=True)
k = int(input())
guests = []
for i, num in enumerate(map(int, input().split())):
    guests.append((num, i))
guests.sort(reverse=True)
p = 0
ans = [0] * k
for val, index in guests:
    while p < len(marks) and val <= marks[p]:
        p += 1
    if p >= len(marks):
        break
    ans[index] = len(marks) - p
print(*ans, sep='\n')
