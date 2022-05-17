import threading
import time


def task(name, delay):
    print(f"{name} has just started...")
    counter = 0  # stack
    while counter < 3:
        time.sleep(delay)
        counter += 1
        print(f"{name} is running {counter}...")
    print(f"{name} is about to finish...")


t1 = threading.Thread(target=task, args=('thread-1', 3))
t2 = threading.Thread(target=task, args=('thread-2', 3))

t1.start()
t2.start()

t1.join()
print("thread-1 has just finished!")
t2.join()
print("thread-2 has just finished!")
print("python process is about to finish!")