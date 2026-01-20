from multiprocessing import Process
import time


def order_chai(n):
    print(f"Preparing chai for costumer : #{n}")
    time.sleep(2)
    print(f"Serving chai for costumer : #{n}")


if __name__ == "__main__":
    chai_order = [
        Process(target=order_chai, args=(i+1,))
        for i in range(3)
    ]

    for p in chai_order:
        p.start()
    for p in chai_order:
        p.join()
    print("All Chai servered")
