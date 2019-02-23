import subprocess, time, os


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


def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'\xe24U\n\xd0Q13S\x11'
    proc = subprocess.Popen(['openssl', 'enc', '-des3', '-pass', 'env:password'], env=env, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc


def test4():
    procs = []
    for _ in range(3):
        data = os.urandom(10)
        procs.append(run_openssl(data))
    for proc in procs:
        out, err = proc.communicate()
        print(out)


def run_md5(input_stdin):
    proc = subprocess.Popen(['md5sum'], stdin=input_stdin, stdout=subprocess.PIPE)
    return proc


def test5():
    input_procs = []
    hash_procs = []
    for _ in range(3):
        data = os.urandom(10)
        proc = run_openssl(data)
        input_procs.append(proc)
        hash_proc = run_md5(proc.stdout)
        hash_procs.append(hash_proc)

    for proc in input_procs:
        proc.communicate()
    for proc in hash_procs:
        out, err = proc.communicate()
        print(out.strip())


if __name__ == '__main__':
    test5()
