n = int(input())
d = {key: val for key, val in enumerate(map(int, input().split()), 1)}
k = int(input())
for i in map(int, input().split()):
    d[i] -= 1

ans = {
    True: 'YES',
    False: 'NO'
}
print(*map(lambda x: ans[x < 0], d.values()), sep='\n')
