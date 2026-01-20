import threading
import time

count = 0


def brew_chai():
    print(f"{threading.current_thread().name} Starts brewing chai...")
    global count
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} Ends brewing chai...")


thread1 = threading.Thread(target=brew_chai, name="Barista_1")
thread2 = threading.Thread(target=brew_chai, name="Barista_2")
thread1.start()
thread2.start()
start = time.time()
thread1.join()
thread2.join()
end = time.time()
print(f"Total time taken : {end-start:.2f}")
print(f"{count}")
