def compute_formula(n, k):
    # Инициализируем сумму
    total_sum = 1  # C(k, 0) = 1
    current_coefficient = 1  # Это будет хранить C(k, i)

    # Считаем сумму для всех i от 1 до n-2
    for i in range(1, n - 1):
        # Вычисляем C(k, i) на основе предыдущего C(k, i-1)
        current_coefficient = current_coefficient * (k - i + 1) // i
        # Добавляем текущий коэффициент к сумме
        total_sum += current_coefficient
    # Умножаем на n
    return (total_sum - min((current_coefficient, n - 1))) * n % (10 ** 9 + 7)


n = int(input())
k = (n - 1) * (n - 2) // 2
print(compute_formula(n, k))
