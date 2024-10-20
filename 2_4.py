import os
from concurrent.futures import ThreadPoolExecutor
import time

FILE_PATH = "example.txt"

def write_to_file():
    print("Запись данных в файл началась...")
    with open(FILE_PATH, 'w') as f:
        for i in range(1, 6):
            f.write(f"Строка данных {i}\n")
            time.sleep(1)
    print("Запись данных в файл завершена.")
    return FILE_PATH

def read_from_file(file_path):
    print("Чтение данных из файла началось...")
    if not os.path.exists(file_path):
        print("Файл не найден.")
        return
    
    with open(file_path, 'r') as f:
        data = f.read()
        print("Прочитанные данные:")
        print(data)
    print("Чтение данных из файла завершено.")

def main():
    with ThreadPoolExecutor() as executor:
        future_write = executor.submit(write_to_file)
        future_read = executor.submit(read_from_file, future_write.result())

if __name__ == "__main__":
    main()
