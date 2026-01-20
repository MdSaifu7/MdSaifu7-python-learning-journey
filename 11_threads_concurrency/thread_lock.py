import threading

count = 0
lock = threading.Lock()


def increment():
    global count
    for _ in range(100000):
        with lock:
            count += 1


threads = [threading.Thread(target=increment) for _ in range(7)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Total count: {count}")
