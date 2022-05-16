# Press the green button in the gutter to run the script.
from exercise01 import Time

if __name__ == '__main__':
    time1 = Time(11, 20, 0)
    time2 = Time()
    time2.hour = 11
    time2.minute = 22
    time2.second = 45
    print(f"{time2.hour}:{time2.minute}:{time2.second}")
    print(time2)
