from threading import Thread
from time import time
import select

numbers = [2139079, 1214759, 1852285, 15166375]


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


def test_1():
    start = time()
    for num in numbers:
        list(factorize(num))
    end = time()
    print('Took %.3f seconds.(No thread)' % (end - start))


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


def test_2():
    start = time()
    threads = []
    for number in numbers:
        thread = FactorizeThread(number)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end = time()
    print('Took %.3f seconds.(Threading)' % (end - start))


def slow_systemcall():
    select.select([], [], [], 0.1)


def test_3():
    start = time()
    threads = []
    for _ in range(5):
        thread = Thread(target=slow_systemcall)
        thread.start()
        threads.append(thread)

    # do some thing
    for i in range(5):
        print(i)

    for thread in threads:
        thread.join()
    end = time()
    print('Took %.3f seconds' % (end - start))


if __name__ == '__main__':
    # test_1()
    # test_2()
    test_3()
