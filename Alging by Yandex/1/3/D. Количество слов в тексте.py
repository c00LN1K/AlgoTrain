import sys

ans = set()
for row in sys.stdin:
    for word in row.split():
        ans.add(word)

print(len(ans))
