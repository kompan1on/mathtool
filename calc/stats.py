import math

MAX_COUNT = 20
MAX_VALUE = 10000

def stats_check(values):
    if len(values) == 0:
        raise ValueError("Пустая последовательность")
    if len(values) > MAX_COUNT:
        raise ValueError(f"Чесел больше чем {MAX_COUNT}")
    for value in values:
        if not math.isfinite:
            raise ValueError(f"{value} не является конечным числом")
        if abs(value) > MAX_VALUE:
            raise ValueError(f"{value} вне допустимого диапазона")



def count(values):
    return len(values)

def total(values):
    res = 0
    for value in values:
        res += value
    return res

def mean(values):
    return total(values)/len(values)

def sq_sum(values):
    res = 0
    for value in values:
        res = res + value ** 2
    return res

def root_mean_sq(values):
    return math.sqrt(sq_sum(values) / len(values))

def variance(values):
    return sq_sum_dev(values)/len(values)

def sko(values):
    return math.sqrt(variance(values))

def min_val(values):
    res = values[0]
    for value in values:
        if res > value:
            res = value
    return res

def max_val(values):
    res = values[0]
    for value in values:
        if res < value:
            res = value
    return res

def negative_count(values):
    res = 0
    for value in values:
        if value < 0:
            res += 1
    return res

def positive_count(values):
    res = 0
    for value in values:
        if value > 0:
            res += 1
    return res

def sq_sum_dev(values):
    M = mean(values)
    res = 0
    for value in values:
        res = res + (value - M)**2
    return res



def st_dev(values):
    if len(values)<2:
        return None
    return math.sqrt(sq_sum_dev(values)/(len(values)-1))

REPORT = [
    ("Количество",    count,            "d"),
    ("Сумма",         total,            ".3f"),
    ("Ср. арифм.",    mean,             ".3f"),
    ("Сумма кв.",     sq_sum,       ".3f"),
    ("Ср. кв.",       root_mean_sq, ".3f"),
    ("Дисперсия",     variance,         ".3f"),
    ("СКО",           sko,              ".3f"),
    ("Станд. откл.",  st_dev,          ".3f"),
    ("Наименьшее",    min_val,          ".3f"),
    ("Наибольшее",    max_val,          ".3f"),
    ("Положительных", positive_count,   "d"),
    ("Отрицательных", negative_count,   "d"),
]
