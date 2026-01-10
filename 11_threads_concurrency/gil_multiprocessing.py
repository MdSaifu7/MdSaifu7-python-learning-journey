import multiprocessing
import time


def make_chai():
    print(f"Start brewing chai...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"End brewing chai...")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=make_chai)
    p2 = multiprocessing.Process(target=make_chai)
    start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print(f"Total time taken : {end-start:.2f} seconds")
