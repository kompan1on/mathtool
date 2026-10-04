import math

MAX_VALUE = 10000

def solve_check(coef):

    for name, value in coef.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"Коэффициент {name} вне допустимого диапазона")
    if coef["A"]==0 and coef["B"]==0:
        raise ValueError("Это не уравнение")


def solve(a, b, c):

    # Решение уравнений
    if a == 0:
        x = -c/b
        return "линейное", None, [x]
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return "квадратное", d, [x1, x2]
    elif d == 0:
        x = -b / (2 * a)
        return "квадратное", d, [x]
    else:
        return "квадратное", d, []

