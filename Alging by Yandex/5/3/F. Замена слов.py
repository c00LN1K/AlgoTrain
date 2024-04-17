d = set(input().split())
ans = []
maxx = max(map(len, d))
for word in input().split():
    for i in range(min(maxx + 1, len(word))):
        if word[:i + 1] in d:
            ans.append(word[:i + 1])
            break
    else:
        ans.append(word)
print(*ans)
