import argparse
from calc import series
from calc import integration
def build_parser():
    parser=argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool - расчеты над уравнениями и числовыми последовательностями",
        allow_abbrev=False)

    commands = parser.add_subparsers(dest="command", title="команды")

    p = commands.add_parser("solve", allow_abbrev=False, help="Решение квадратного уравнения")
    p.add_argument("-a", type=int, help="Коэфициент А (целое, по модулю не более 10000)")
    p.add_argument("-b", type=int, help="Коэфициент B (целое, по модулю не более 10000)")
    p.add_argument("-c", type=int, help="Коэфициент C (целое, по модулю не более 10000)")

    p = commands.add_parser("stats", allow_abbrev=False, help="Показатели последовательности")
    p.add_argument("--input", help="Файл с числами")

    p = commands.add_parser("series", allow_abbrev=False, help="Сумма ряда")
    p.add_argument("--func", required=True, choices=sorted(series.FORMULAS), help="Какой ряд суммировать")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="Сколько слагаемых сложить")
    group.add_argument("--eps", type=float, help="Точность: до слагаемого меньше eps")

    p = commands.add_parser("integrate", allow_abbrev=False, help="Интеграл методом левых прямоугольников")
    p.add_argument("--func", required=True, choices=sorted(integration.FUNCTIONS), help="Какую функцию интегрировать")
    p.add_argument("--from", dest="start", type=float, required=True, help="Нижний предел")
    p.add_argument("--to", dest="end", type=float, required=True, help="Верхний предел (выше нижнего)")
    p.add_argument("--steps", type=int, required=True, help="Число прямоугольников (1...100000)")

    return parser
