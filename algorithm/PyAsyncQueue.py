import asyncio

async def producer(queue):
    """비동기 생산자: 0~4까지 값을 생산하여 큐에 추가"""
    for i in range(5):
        await queue.put(i)
        print(f"생산: {i}")
        await asyncio.sleep(1)  # 1초 대기

async def consumer(queue):
    """비동기 소비자: 큐에서 값을 가져와 소비"""
    while True:
        item = await queue.get()
        print(f"소비: {item}")
        queue.task_done()  # 작업 완료 표시

async def main():
    queue = asyncio.Queue()

    # 생산자 및 소비자 태스크 생성
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task  # 생산자 종료 대기
    await queue.join()   # 모든 작업이 끝날 때까지 대기

    consumer_task.cancel()  # 소비자 종료

asyncio.run(main())