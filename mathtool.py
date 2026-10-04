import sys
from calc import equation
from cli import build_parser
from calc import stats
from calc import series
from calc import integrate

def hand_solve(args):
    given = [args.a, args.b, args.c]
    mis = given.count(None)

    if mis == 3:
        try:
            a = int(input("Введите А: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            raise ValueError("Коэффициент не является целым числом")
    elif mis == 0:
        a, b, c = args.a, args.b, args.c
    else:
        raise ValueError("Укажите или все три коэффициента, или ни одного")

    equation.solve_check({"A": a, "B": b, "C": c})
    kind, d, roots = equation.solve(a, b, c)
    print(f"Уравнение {kind}")
    if d is not None:
        print(f"Дискриминант: {d}")
    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print("Действительных корней нет")
    return 0

def read_num(source):

    values = []
    for line in source:
        for word in line.split():
            try:
                values.append(float(word))
            except ValueError:
                raise ValueError(f"{word} не является числом")
    return values

def hand_stats(args):
    if args.input is not None:
        try:
            with open(args.input, encoding="utf-8-sig") as handle:
                values = read_num(handle)
        except OSError:
            raise OSError(f"Файл {args.input} не открывается")
    else:
        values = read_num(sys.stdin)
    stats.stats_check(values)

    for lable, function, form in stats.REPORT:
        value = function(values)
        if value is None:
            print(f"{lable}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{lable}: {value:{form}}")
    return 0

def hand_series(args):
    series.check_params(args.terms, args.eps)
    term, formula = series.FORMULAS[args.func]
    if args.terms is not None:
        res = series.sum_terms(term, args.terms)
        count = args.terms
    else:
        res, count = series.sum_eps(term, args.eps)
    print(formula)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {res:.4f}")
    return 0

def hand_integrate(args):
    integrate.check_params(args.func, args.start, args.end, args.steps)
    f, formula, low, high, closed = integrate.FUNCTIONS[args.func]
    res = integrate.integrate(f, args.start, args.end, args.steps)

    print(formula)
    print(f"Значение интеграла: {res:.4f}")
    return 0

HANDLERS = {
    "solve": hand_solve,
    "stats": hand_stats,
    "series": hand_series,
    "integrate": hand_integrate
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
        return 1
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
