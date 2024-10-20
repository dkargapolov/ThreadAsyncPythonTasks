import os
import threading

class FileSearcher:
    def __init__(self, directory, filename_pattern, num_threads):
        self.directory = directory
        self.filename_pattern = filename_pattern
        self.found = False
        self.lock = threading.Lock()
        self.threads = []
        self.chunk_size = len(os.listdir(directory)) // num_threads

    def search_files(self, start, end):
        for i in range(start, end):
            if self.found:
                return
            file_name = os.listdir(self.directory)[i]
            if self.filename_pattern in file_name:
                with self.lock:
                    if not self.found:  # Двойная проверка
                        self.found = True
                        print(f"Файл найден: {file_name}")
                        break

    def start_search(self):
        files = os.listdir(self.directory)
        num_files = len(files)

        for i in range(0, num_files, self.chunk_size):
            start = i
            end = min(i + self.chunk_size, num_files)
            thread = threading.Thread(target=self.search_files, args=(start, end))
            self.threads.append(thread)
            thread.start()

        for thread in self.threads:
            thread.join()

if __name__ == "__main__":
    directory_path = "your_directory_path"  # Укажите путь к директории
    search_pattern = "file_to_search"  # Укажите шаблон имени файла
    number_of_threads = 4  # Укажите количество потоков

    file_searcher = FileSearcher(directory_path, search_pattern, number_of_threads)
    file_searcher.start_search()
