import threading
import time

def background_task():
    while True:
        print("Running in background...")
        time.sleep(1)

# 데몬 스레드 생성
daemon_thread = threading.Thread(target=background_task, daemon=True)

# 실행
daemon_thread.start()

# 메인 스레드 종료 (데몬 스레드는 메인 종료 시 자동 종료)
time.sleep(3)
print("Main thread exits")
