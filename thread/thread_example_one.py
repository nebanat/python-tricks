import time
from threading import Thread


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


if __name__ == '__main__':
    t1 = Thread(target=countdown, args=(10,))
    t2 = Thread(target=countdown, args=(14,))
    t1.start()
    t2.start()

    if t1.is_alive() and t2.is_alive():
        pass
