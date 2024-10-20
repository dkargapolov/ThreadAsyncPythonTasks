import threading

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def threaded_quicksort(arr):
    sorted_arr = quicksort(arr)
    print(f"Отсортированный массив: {sorted_arr}")

arrays = [
    [33, 2, 52, 106, 73],
    [19, 42, 23, 67, 13],
    [91, 44, 55, 12, 3]
]

threads = []
for array in arrays:
    thread = threading.Thread(target=threaded_quicksort, args=(array,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
