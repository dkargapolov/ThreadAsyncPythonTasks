import threading
from timeit import default_timer as timer
import math

def f(x):
    return math.sin(x)

def integrate(f, a, b, *, n_iter=1000):
    step = (b - a) / n_iter
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n_iter):
        result += f(a + i * step)
    return result * step

def thread_integration(f, a, b, n_iter, num_threads):
    step = (b - a) / num_threads
    threads = []
    result = 0
    lock = threading.Lock()

    def integrate_on_interval(start, end, n_intervals):
        nonlocal result
        partial_result = integrate(f, start, end, n_iter=n_intervals)
        with lock:
            result += partial_result

    for i in range(num_threads):
        start = a + i * step
        end = a + (i + 1) * step
        thread = threading.Thread(target=integrate_on_interval, args=(start, end, n_iter // num_threads))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result

start_seq = timer()
result_seq = integrate(f, 0, math.pi, n_iter=1000000)
end_seq = timer()
seq_time = end_seq - start_seq

start_mt = timer()
result_mt = thread_integration(f, 0, math.pi, 1000000, 4)
end_mt = timer()
mt_time = end_mt - start_mt

print(f"Последовательный результат: {result_seq}, время: {seq_time:.6f} сек")
print(f"Многопоточный результат: {result_mt}, время: {mt_time:.6f} сек")
