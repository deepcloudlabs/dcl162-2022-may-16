import os
from concurrent.futures import ThreadPoolExecutor
from random import randint

num_of_cpus = os.cpu_count()

print(f"num_of_cpus: {num_of_cpus}")


def draw_lottery_numbers(max, size):
    numbers = set()
    while len(numbers) < size:
        numbers.add(randint(1, max))
    numbers = list(numbers)
    numbers.sort()
    return numbers


futures = []
lottery_numbers = []

with ThreadPoolExecutor(max_workers=num_of_cpus) as tp:
    for i in range(0, 2_048):
        future = tp.submit(draw_lottery_numbers, 60, 6)
        futures.append(future)
    for future in futures:
        lottery_numbers.append(future.result())
    for numbers in lottery_numbers:
        print(numbers)
