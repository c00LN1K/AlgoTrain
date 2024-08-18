n, m = map(int, input().split())
set_a = set(int(input()) for _ in range(n))
set_b = set(int(input()) for _ in range(m))
set_c = set_a & set_b

print(len(set_c))
print(*sorted(set_c))
print(len(set_a - set_c))
print(*sorted(set_a - set_c))
print(len(set_b - set_c))
print(*sorted(set_b - set_c))
