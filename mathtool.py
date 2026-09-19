import sys
import math

# Предельное значение коэффициентов по модулю
MAX = 10000
A = sys.argv
HELP_TEXT = f"""mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами

Коэффициенты A, B, C — целые числа, по модулю не превышающие {MAX}."""


# Разбор параметров командной строки
ar = len(A) - 1

# Без параметров или --help
if ar == 0 or A[1] == "--help":
    print(HELP_TEXT)
    sys.exit(0)

# Первым параметром должна быть команда solve
if A[1] != "solve":
    print(f"ОШИБКА: неизвестная команда '{A[1]}'", file=sys.stderr)
    sys.exit(1)

# Только solve - ввод с клавиатуры; solve -a .. -b .. -c .. - из параметров
if ar == 1:
    kb = True
elif ar == 7:
    if A[2] != "-a" or A[4] != "-b" or A[6] != "-c":
        print("ОШИБКА: неизвестный параметр, ожидаются -a, -b, -c", file=sys.stderr)
        sys.exit(1)
    kb = False
else:
    print("ОШИБКА: неверный набор параметров", file=sys.stderr)
    sys.exit(1)


# Получение и преобразование исходных данных
try:
    if kb:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    else:
        a = int(sys.argv[3])
        b = int(sys.argv[5])
        c = int(sys.argv[7])
except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)


# Проверка значений на соответствие ограничениям
if abs(a) > MAX or abs(b) > MAX or abs(c) > MAX:
    print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
    sys.exit(1)


# Решение уравнений и вывод результата
if a == 0:
    # Линейное уравнение
    if b != 0:
        print("Уравнение линейное")
        x = round(-c / b, 3) + 0.0
        print(f"x = {x:.3f}")
    else:
        print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
        sys.exit(1)
else:
    # Квадратное уравнение
    print("Уравнение квадратное")
    d = b * b - 4 * a * c
    print(f"D = {d}")

    if d > 0:
        x1 = round((-b + math.sqrt(d)) / (2 * a), 3) + 0.0
        x2 = round((-b - math.sqrt(d)) / (2 * a), 3) + 0.0
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")
    elif d == 0:
        x = round(-b / (2 * a), 3) + 0.0
        print(f"x = {x:.3f}")
    else:
        print("Действительных корней нет")
