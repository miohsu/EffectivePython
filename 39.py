from threading import Lock, Thread
from collections import deque
from time import sleep


class MyQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()


class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                sleep(0.01)
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1


def download(item):
    print('Download')


def resize(item):
    print('Resize')


def upload(item):
    print('Upload')


if __name__ == '__main__':
    download_queue = MyQueue()
    resize_queue = MyQueue()
    upload_queue = MyQueue()
    done_queue = MyQueue()
    threads = [
        Worker(download, download_queue, resize_queue),
        Worker(resize, resize_queue, upload_queue),
        Worker(upload, upload_queue, done_queue)
    ]

    for thread in threads:
        thread.start()

    for _ in range(10):
        download_queue.put(object())

    processed = len(done_queue.items)
    polled = sum(t.polled_count for t in threads)
    print('Processed', processed, 'items after polling', polled, 'times')
