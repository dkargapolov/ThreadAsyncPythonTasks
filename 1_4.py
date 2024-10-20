import threading

def calculate_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"Факториал {n} = {result}")

numbers = [5, 7, 10, 12]

threads = []
for num in numbers:
    thread = threading.Thread(target=calculate_factorial, args=(num,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
