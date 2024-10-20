import threading

def print_thread_name():
    print(f"Имя потока: {threading.current_thread().name}")

threads = []
for i in range(5):  # создаём 5 потоков
    thread = threading.Thread(target=print_thread_name, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
