import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(f"Thread {self.name}: {i}")

# 스레드 생성 및 실행
thread1 = MyThread()
thread2 = MyThread()

thread1.start()
thread2.start()

thread1.join()
thread2.join()