n = input()

digits = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900,
}
ans = 0
i = 0

while i < len(n):
    if n[i:min(i + 2, len(n))] in digits:
        ans += digits[n[i:min(i + 2, len(n))]]
        i += 2
    else:
        ans += int(digits[n[i]])
        i += 1

print(ans)
