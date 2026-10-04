import math

MAX_TERMS = 10000
MAX_EPS=0.0001
MAX_IT=100000

def check_params(terms, eps):
    if terms is not None:
        if not (1 <= terms <= MAX_TERMS):
            raise ValueError("Колличество слагаемых вне диапазона")
    else:
        if not (math.isfinite(eps) and 0 < eps <= MAX_EPS):
            raise ValueError("Точность вне диапазона")

def sign(n):
    if n%2==0:
        return-1
    else:
        return 1

def term_third(n):
    return sign(n) / (3*n)

def term_sqplus(n):
    return sign(n) / (n*n+1)

FORMULAS = {
    "third": (term_third, "S = 1/3 - 1/6 + 1/9 - 1/12 + ..."),
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + ...")

}

def sum_terms(term, terms):
    res = 0
    for n in range(1, terms+1):
        res=res+term(n)
    return res

def sum_eps(term, eps):
    res = 0
    n = 0
    while True:
        n = n+1
        value = term(n)
        res = res+value
        if abs(value)<eps:
            return res, n
        if n >= MAX_IT:
            raise ValueError("Точность не достигнута")
