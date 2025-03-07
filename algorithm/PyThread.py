import threading

def print_hello():
    print("Hello, World!")

# 스레드 생성
thread = threading.Thread(target=print_hello)

# 스레드 시작
thread.start()

# 메인 스레드가 종료될 때까지 기다림
thread.join()