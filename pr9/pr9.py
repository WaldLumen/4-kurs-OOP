import math
from functools import singledispatch

def print_info(surname="Ivanov", course=1, group="CS-11"):
    print(f"Фамилия: {surname}, Курс: {course}, Группа: {group}")

print_info("Petrenko", 2, "IT-21")
print_info("Shevchenko")
print_info(course=3)

print()


def count_even(*args):
    return sum(1 for x in args if x % 2 == 0)

print("Четных (2 параметра):", count_even(2, 5))
print("Четных (5 параметров):", count_even(1, 2, 3, 4, 6))
print()


@singledispatch
def maximum(value):
    raise TypeError("Неподдерживаемый тип")

@maximum.register
def _(value: list):
    return max(value)

@maximum.register
def _(value: tuple):
    return max(value)

print("Максимум списка:", maximum([3, 7, 1, 9]))
print("Максимум кортежа:", maximum((4, 2, 8, 6)))
print()

def generic_max(container):
    return max(container)

print("Шаблон max (list):", generic_max([5, 1, 4]))
print("Шаблон max (tuple):", generic_max((7, 3, 9)))
print()

def bisection(func, a, b, eps=1e-4):
    while abs(b - a) > eps:
        mid = (a + b) / 2
        if func(a) * func(mid) <= 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2

def equation(x):
    return 3 * math.sin(math.sqrt(x)) + 0.35 * x - 3.8

root = bisection(equation, 2, 3)
print("Корень уравнения:", round(root, 4))
print("Точное значение: 2.2985")
