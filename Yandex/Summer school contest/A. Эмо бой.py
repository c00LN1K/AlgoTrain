from string import digits, ascii_lowercase, ascii_uppercase


def f(coll):
    return set(s) & set(coll)


s = input()
print('YES' if len(s) >= 8 and all(map(f, [digits, ascii_lowercase, ascii_uppercase])) else 'NO')
