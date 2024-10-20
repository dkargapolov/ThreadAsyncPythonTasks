import asyncio

async def task1():
    await asyncio.sleep(2)
    return "Результат задачи 1"

async def task2():
    await asyncio.sleep(3)
    return "Результат задачи 2"

async def process_results():
    result1, result2 = await asyncio.gather(task1(), task2())
    print(f"Задача 1: {result1}")
    print(f"Задача 2: {result2}")

async def main():
    await process_results()

if __name__ == "__main__":
    asyncio.run(main())
