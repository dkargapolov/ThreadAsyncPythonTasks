import threading

class Queue:
    def __init__(self):
        self.queue = []
        self.lock = threading.RLock()

    def enqueue(self, item):
        with self.lock:
            self.queue.append(item)
            print(f"Элемент {item} добавлен в очередь.")

    def dequeue(self):
        with self.lock:
            if len(self.queue) == 0:
                print("Очередь пуста.")
                return None
            item = self.queue.pop(0)
            print(f"Элемент {item} удален из очереди.")
            return item

def producer(queue, items):
    for item in items:
        queue.enqueue(item)
        threading.Event().wait(1)

def consumer(queue):
    while True:
        item = queue.dequeue()
        if item is None:
            break
        threading.Event().wait(1)

if __name__ == "__main__":
    q = Queue()

    producer_items = [1, 2, 3, 4, 5]

    producer_thread = threading.Thread(target=producer, args=(q, producer_items))
    consumer_thread = threading.Thread(target=consumer, args=(q,))

    producer_thread.start()
    producer_thread.join()

    consumer_thread.start()
    consumer_thread.join()
