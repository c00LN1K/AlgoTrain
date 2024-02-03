import json

n, m = map(int, input().split())

ans = []
flag = 0
for i in range(n):
    if len(ans) >= m: break
    data = json.loads(input())
    for offer in data['offers']:
        if len(ans) >= m:
            flag = 1
            break
        ans.append(offer)

print({'offers': ans})
