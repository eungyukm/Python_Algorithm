import threading

counter = 0
lock = threading.Lock()

def increase_counter():
    global counter
    for _ in range(100000):
        with lock:  # 임계 영역 보호
            counter += 1

threads = [threading.Thread(target=increase_counter) for _ in range(3)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Final counter:", counter)
