import subprocess, time


def test1():
    proc = subprocess.Popen(['echo', 'Hello from the child'], stdout=subprocess.PIPE)
    out, err = proc.communicate()
    print(out.decode('utf8'))


def test2():
    proc = subprocess.Popen(['sleep', '0.3'])
    while proc.poll() is None:
        print('Working...')
    print('Exit status: ', proc.poll())


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


def test3():
    start = time.time()
    procs = []
    for _ in range(10):
        procs.append(run_sleep(0.1))
    for proc in procs:
        proc.communicate()
    end = time.time()
    print('Finished in %.3f seconds' % (end - start))


if __name__ == '__main__':
    test3()
