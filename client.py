import asyncio
import json

async def run_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    message = json.dumps({"message": "Привет, сервер!"})
    writer.write(message.encode())
    await writer.drain()

    # Используем readuntil для чтения данных до закрытия соединения
    try:
        data = await reader.read(100)  # Это может быть изменено на более длинный буфер
        response = json.loads(data.decode())
        print(f"Получен ответ: {response}")
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
        print(f"Полученные данные: {data.decode()}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(run_client())
