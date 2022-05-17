import threading
from random import randint

lottery_numbers = []


def draw_lottery_numbers(max, size):
    numbers = set()
    while len(numbers) < size:
        numbers.add(randint(1, max))
    numbers = list(numbers)
    numbers.sort()
    lottery_numbers.append(numbers)


threads = []
for i in range(0, 2_048):
    thread = threading.Thread(target=draw_lottery_numbers, args=(60, 6))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for numbers in lottery_numbers:
    print(numbers)

print(f"There are {len(lottery_numbers)} numbers in lottery_numbers.")
