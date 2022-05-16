values = [4, 8, 15, 16, 23, 42]


def topla(sayilar):
    total = 0
    for sayi in sayilar:
        total = total + sayi
    return total


print(topla(values))
print(min(values))
print(max(values))


def for_each(numbers, action):  # higher-order function
    for number in numbers:
        action(number)


for_each(values, print)
