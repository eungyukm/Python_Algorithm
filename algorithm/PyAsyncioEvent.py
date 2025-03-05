import asyncio

async def waiter(event):
    print("이벤트 대기 중...")
    await event.wait()  # 이벤트 신호 대기
    print("이벤트 발생!")

async def setter(event):
    await asyncio.sleep(3)
    print("이벤트 발생 시킴!")
    event.set()  # 이벤트 활성화

async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())