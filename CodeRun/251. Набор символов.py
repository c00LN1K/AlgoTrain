s = input()
c = set(input())

d = set()
k = 0
minn = len(s)

# это цикл найдет первую подходящую под условие подстроку
for i in range(len(s)):
    if c >= set(s[i]):
        if d == set(s[i]):
            k = 0
        d.add(s[i])
        k += 1
        if d == c:
            print(k)
            break
    else:
        d = set()
        k = 0
else:
    print(0)

d = set()
k = 0

for i in range(len(s)):
    if c >= set(s[i]):
        d.add(s[i])
        k += 1
    else:
        # ищем минимальную подстроку в максимальной (тогда надо хранить индексы начала и конца)
        d = set()
        k = 0

print(k)
