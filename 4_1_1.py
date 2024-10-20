import asyncio
from datetime import datetime

async def show_time():
    while True:
        print(f"Текущее время: {datetime.now().strftime('%H:%M:%S')}")
        await asyncio.sleep(1)

# Запуск асинхронной функции
async def main():
    try:
        await show_time()
    except asyncio.CancelledError:
        print("Завершение программы.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Программа остановлена через Ctrl+C.")
