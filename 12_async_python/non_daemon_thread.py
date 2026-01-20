import time
import threading


def monitor_tea():
    while True:
        print(f"Monitoring tea temparature...")
        time.sleep(3)


t = threading.Thread(target=monitor_tea, daemon=True)
t.start()
print("Main program done...")
