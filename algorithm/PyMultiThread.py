import threading

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")

# 여러 개의 스레드 생성
threads = [threading.Thread(target=print_numbers) for _ in range(3)]

# 모든 스레드 생성
for t in threads:
    t.start()

# 모든 스레드가 종료될 때까지 대기
for t in threads:
    t.join()