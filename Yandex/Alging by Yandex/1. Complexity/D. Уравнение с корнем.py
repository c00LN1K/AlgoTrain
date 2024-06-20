def solve_eq(a, b, c):
    if c < 0 or (a == 0 and c ** 2 != b):
        return 'NO SOLUTION'
    c **= 2
    if a == 0 and c == b:
        return 'MANY SOLUTIONS'
    x = (c - b) / a
    if x.is_integer():
        return int(x)
    return 'NO SOLUTION'


a, b, c = int(input()), int(input()), int(input())
ans = solve_eq(a, b, c)
print(int(ans) if isinstance(ans, float) and ans == int(ans) else ans)
