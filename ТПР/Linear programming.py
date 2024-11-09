from scipy.optimize import linprog

# Коэффициенты целевой функции (для максимизации умножим на -1, так как метод minimization-based)
F = [-5, -1]  # [3, 2] -> -[3, 2]

# Коэффициенты ограничений
A = [
    [1, -3],
    [-1, -1],
    [2, 1],
    [0, 1],
]

# Правые части ограничений
B = [1, -5, 16, 8]

# Границы переменных (x1 >= 0, x2 >= 0)
x_bounds = [(0, None), (0, None)]

# Решение задачи
result = linprog(F, A_ub=A, b_ub=B, bounds=x_bounds, method='simplex')

# Вывод результата
if result.success:
    print(f"Оптимальные значения переменных: x1 = {result.x[0]}, x2 = {result.x[1]}")
    print(f"Максимальное значение целевой функции: Z = {-result.fun}")
else:
    print("Задача не имеет решения.")
