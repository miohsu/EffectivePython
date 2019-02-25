from queue import Queue
from threading import Thread
from time import sleep

queue = Queue(1)


def consumer():
    sleep(1)
    queue.get()
    print('Consumer got 1')
    queue.get()
    print('Consumer got 2')


if __name__ == '__main__':
    thread = Thread(target=consumer)
    thread.start()
    queue.put(object())
    print('Producer put 1')
    queue.put(object())
    print('Producer put 2')
    thread.join()
    print('Producer done')
