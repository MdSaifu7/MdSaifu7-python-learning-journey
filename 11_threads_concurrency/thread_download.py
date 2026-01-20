import requests
import threading
import time


def dowload(url):
    print(f"Start downloading from {url}")
    res = requests.get(url)
    print(f"Finished downloading from {url}, size {len(res.content)} bytes")


urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

threads = []
start = time.time()
for url in urls:
    t = threading.Thread(target=dowload, args=(url,))
    t.start()
    threads.append(t)


for t in threads:
    t.join()

end = time.time()

print(f"Total downloading time : {end-start:.2f} seconds")
