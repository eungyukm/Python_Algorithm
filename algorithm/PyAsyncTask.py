import asyncio

async def task(name):
    print(f"{name} 시작")
    await asyncio.sleep(2)
    print(f"{name} 완료")


async def main():
    t1 = asyncio.create_task(task("Task 1"))
    t2 = asyncio.create_task(task("Task 2"))

    print("모든 작업 시작됨")
    await t1
    await t2

asyncio.run(main())