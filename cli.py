import argparse
from calc import series

def build_parser():
    parser=argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool - расчеты над уравнениями и числовыми последовательностями",
        allow_abbrev=False)

    commands = parser.add_subparsers(dest="command", title="команды")

    p = commands.add_parser("solve", allow_abbrev=False, help="Решение квадратного уравнения")
    p.add_argument("-a", type=int, help="Коэфицент А (целое, по модулю не более 10000)")
    p.add_argument("-b", type=int, help="Коэфицент B (целое, по модулю не более 10000)")
    p.add_argument("-c", type=int, help="Коэфицент C (целое, по модулю не более 10000)")

    p = commands.add_parser("stats", allow_abbrev=False, help="Показатели последовательности")
    p.add_argument("--input", help="Файл с числами")

    p = commands.add_parser("series", allow_abbrev=False, help="Сумма ряда")
    p.add_argument("--func", required=True, choices=sorted(series.FORMULAS), help="Какой ряд суммировать")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="Скольуо слагаемых сложить")
    group.add_argument("--eps", type=float, help="Точность: до слагаемого меньше eps")



    return parser
