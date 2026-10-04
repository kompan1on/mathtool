import math

MAX_STEPS = 100000

def f_ratio(x):
    return x / (x+1)

def f_root(x):
    return math.sqrt(x * x+1)

FUNCTIONS = {
    "ratio": (f_ratio, "F(x) = x / (x+1)", 0, 20, True),
    "root": (f_root, "F(x) = sqrt(x^2+1)", -5, 5, False)
}
def check_params(name, a, b, steps):
    f, formula, low, high, closed = FUNCTIONS[name]
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("Предел не является конечным числом")
    if a>=b:
        raise ValueError("Начальный предел не меньше конечного")

    for value in (a,b):
        if closed:
            outside = value <= low or value > high
        else:
            outside = value <= low or value >= high
        if outside:
            raise ValueError("Предел вне промежутка")
    if not (1<=steps<=MAX_STEPS):
        raise ValueError("Количество шагов вне диапазона")

def integrate(f, a, b, steps):
    dx = (b - a) / steps
    res=0
    for i in range(steps):
        x = a + i*dx
        res = res + f(x)*dx
    return res