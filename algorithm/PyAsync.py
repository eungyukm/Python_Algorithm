import asyncio

async def say_hello():
    print("Hello")
    # 1초 동안 비동기 대기
    await asyncio.sleep(1)
    print("World")

# 이벤트 루프 실행
asyncio.run(say_hello())