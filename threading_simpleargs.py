import threading


def worker(n):
    print(f'Worker {n}')


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()

