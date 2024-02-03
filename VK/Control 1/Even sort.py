n = int(input())
lst = list(map(int, input().split()))


# 1. Вставки - делим массив на отсортированную и неотсортированную части.
# Если находим четное число, то сдвигаем его влево (до отсортированной части)
# 2. Два указателя
# 3. Новый массив

def insert_solve(n, lst):
    sorted_index = -1

    for i in range(n):
        key = lst[i]
        if key % 2 == 1:
            continue
        j = i - 1
        while j > sorted_index:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        sorted_index += 1

    print(lst)


def two_pointers_solve(n, lst):
    odd_index = 0

    for i in range(n):
        if lst[i] % 2 == 1 and lst[odd_index] % 2 != 1:
            odd_index = i
        elif lst[i] % 2 == 0 and lst[odd_index] % 2 == 1:
            lst[odd_index], lst[i] = lst[i], lst[odd_index]
            odd_index += 1

    print(*lst)


evens = []
odds = []

for i in range(n):
    if lst[i] % 2 == 0:
        evens.append(lst[i])
    else:
        odds.append(lst[i])

print(*(evens + odds))
two_pointers_solve(n, lst)

