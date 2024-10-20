import asyncio
import json

async def handle_client(reader, writer):
    data = await reader.read(100)
    
    try:
        message = json.loads(data.decode())
        print(f"Получено сообщение: {message}")

        response = json.dumps({"response": "Сообщение получено!"})
        writer.write(response.encode())
        await writer.drain()
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
    
    writer.close()
    await writer.wait_closed()

async def run_server():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)

    async with server:
        print("Сервер запущен, ждет подключений...")
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(run_server())
