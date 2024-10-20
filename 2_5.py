import threading
import time

event = threading.Event()

def set_event():
    while True:
        time.sleep(1)
        print("Устанавливаю событие.")
        event.set()

def wait_for_event():
    while True:
        event.wait()
        print("Событие произошло!")
        event.clear()

def event_not_occurred():
    while not event.is_set():
        print("Событие не произошло.")
        time.sleep(1)

if __name__ == "__main__":
    thread1 = threading.Thread(target=set_event)
    thread2 = threading.Thread(target=wait_for_event)
    thread3 = threading.Thread(target=event_not_occurred)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
