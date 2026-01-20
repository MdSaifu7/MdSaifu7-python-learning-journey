import threading
import time


def take_order():
    for i in range(1, 4):
        print(f"Preparing order for #{i}")
        time.sleep(1)


def making_order():
    for i in range(1, 4):
        print(f"Making order for #{i}")
        time.sleep(2)


# create thread

take_order_thread = threading.Thread(target=take_order)
make_order_thread = threading.Thread(target=making_order)

take_order_thread.start()
make_order_thread.start()
take_order_thread.join()

make_order_thread.join()

print("Chai shop closed")
