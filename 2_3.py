import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Путь для сохранения изображений
DOWNLOAD_DIR = "images"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Семафор для ограничения числа одновременно работающих потоков
semaphore = threading.Semaphore(3)  # Например, максимум 3 потока одновременно

# Функция для скачивания изображения
def download_image(url):
    image_name = os.path.join(DOWNLOAD_DIR, url.split("/")[-1])
    
    with semaphore:
        try:
            print(f"Downloading {url}...")
            response = requests.get(url)
            response.raise_for_status()  # Проверяем успешность запроса
            with open(image_name, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {url} and saved as {image_name}")
            return f"{url} downloaded successfully"
        except requests.RequestException as e:
            print(f"Failed to download {url}: {e}")
            return f"Failed to download {url}"

# Список реальных URL изображений для загрузки
image_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/320px-PNG_transparency_demonstration_1.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/640px-JavaScript-logo.png",
    "https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Tux.png/300px-Tux.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Gnuplot_logo.svg/200px-Gnuplot_logo.svg.png"
]

# Функция для асинхронной загрузки изображений с использованием ThreadPoolExecutor
def download_images_async(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(download_image, url) for url in urls]
        
        for future in as_completed(futures):
            print(future.result())  # Выводим результат загрузки каждого изображения

if __name__ == "__main__":
    download_images_async(image_urls)
