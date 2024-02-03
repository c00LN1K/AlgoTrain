n = int(input())
lst = list(map(int, input().split()))

zero_index = 0

for i in range(n):
    if lst[i] == 0 and lst[zero_index] != 0:
        zero_index = i
    elif lst[i] != 0 and lst[zero_index] == 0:
        lst[i], lst[zero_index] = 0, lst[i]
        zero_index += 1

print(*lst)
