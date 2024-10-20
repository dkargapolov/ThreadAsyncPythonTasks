import threading
import time

class Server:
    def __init__(self, barrier):
        self.barrier = barrier

    def start(self):
        print("Сервер запускается...")
        time.sleep(2)  # Имитируем время инициализации сервера
        print("Сервер готов к работе.")
        self.barrier.wait()  # Ожидание клиента

class Client:
    def __init__(self, barrier):
        self.barrier = barrier

    def request(self):
        print("Клиент ожидает готовности сервера...")
        self.barrier.wait()  # Ожидание готовности сервера
        print("Клиент отправляет запрос серверу.")

if __name__ == "__main__":
    barrier = threading.Barrier(2)  # Создаем барьер на 2 потока

    server = Server(barrier)
    client = Client(barrier)

    server_thread = threading.Thread(target=server.start)
    client_thread = threading.Thread(target=client.request)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()
