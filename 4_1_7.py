import asyncio
import json

async def handle_client(reader, writer):
    data = await reader.read(100)
    message = json.loads(data.decode())
    print(f"Получено сообщение: {message}")

    response = json.dumps({"response": "Сообщение получено!"})
    writer.write(response.encode())
    await writer.drain()

    writer.close()
    await writer.wait_closed()

async def run_server():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

async def run_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    message = json.dumps({"message": "Привет, сервер!"})
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f"Получен ответ: {data.decode()}")

    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(run_server())
