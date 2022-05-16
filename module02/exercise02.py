from functools import reduce

values = [4, 8, 15, 16, 23, 42]

"""
    functional programming: function
                            i) higher-order function
                            filter/map/reduce -> generator function
                           ii) pure function
                            lambda expression?
"""


def cift_sayilarin_kubunun_toplami(sayilar):
    total = 0
    for sayi in sayilar:
        if sayi % 2 == 0:
            kup = sayi ** 3
            total = total + kup
    return total


print(cift_sayilarin_kubunun_toplami(values))


def is_even(n):
    print("is even")
    return n % 2 == 0


def cube(u):
    print("cube")
    return u * u * u


def topla(s, v):
    print("topla")
    return s + v


# 1-liner: memory-efficient, 1-pass: fast
print(reduce(topla, map(cube, filter(is_even, values)), 0))
