import sys
from calc import equation
from cli import build_parser

def hand_solve(args):
    given = [args.a, args.b, args.c]
    mis = given.count(None)

    if mis == 3:
        try:
            a = int(input("Введите А: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            raise ValueError("Коэффицент не является целым числом")
    elif mis == 0:
        a, b, c = args.a, args.b, args.c
    else:
        raise ValueError("Укажите или все три коэффицента, или ни одного")

    equation.check({"A": a, "B": b, "C": c})
    kind, d, roots = equation.solve(a, b, c)
    print(f"Уравнение {kind}")
    if d is not None:
        print(f"Дискриминант {d}")
    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print("Действительных корней нет")
    return 0





HANDLERS = {
    "solve": hand_solve
}
def main(argv):
    parser = build_parser()

    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    try:
        return HANDLERS[args.command](args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
