def filtrele(predicate_fun, numbers):
    for number in numbers:
        if predicate_fun(number):
            yield number


def donustur(fun, numbers):
    for number in numbers:
        yield fun(number)


def indirge(fun, numbers, init):
    total = init
    for num in numbers:
        total = fun(total, num)
    return total


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(indirge(lambda u, v: u + v, donustur(lambda z: z * z, filtrele(lambda x: x % 2 == 1, list1)), 0))

for num in donustur(lambda x: x * x, filtrele(lambda n: n % 2 == 1, list1)):
    print(num)