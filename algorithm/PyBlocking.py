import asyncio
import time

def blocking_function():
    time.sleep(3)
    return "동기 작업 완료"

async def main():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, blocking_function)
    print(result)

asyncio.run(main())