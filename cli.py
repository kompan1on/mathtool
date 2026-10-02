import argparse

def build_parser():
    parser=argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool - расчеты над уравнениями и числовыми последовательностями",
        allow_abbrev=False)

    commands = parser.add_subparsers(dest="command", title="команды")

    p = commands.add_parser("solve", allow_abbrev=False,
                            help="Решение квадратного уравнения")
    p.add_argument("-a", type=int, help="Коэфицент А (целое, по модулю не более 10000)")
    p.add_argument("-b", type=int, help="Коэфицент B (целое, по модулю не более 10000)")
    p.add_argument("-c", type=int, help="Коэфицент C (целое, по модулю не более 10000)")

    return parser
