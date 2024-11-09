import sys

ans = 0

for line in sys.stdin:
    ans += sum(map(int, line.split()))

print(ans)
