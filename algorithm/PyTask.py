import asyncio

async def task(name, delay):
    print(f"Task {name} 시작")
    await asyncio.sleep(delay)
    print(f"Task {name} 완료")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )

asyncio.run(main())