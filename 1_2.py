import threading
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"{filename} скачан.")

urls = [
    ('https://example.com/image1.jpg', 'image1.jpg'),
    ('https://example.com/image2.jpg', 'image2.jpg'),
    ('https://example.com/image3.jpg', 'image3.jpg')
]

threads = []
for url, filename in urls:
    thread = threading.Thread(target=download_file, args=(url, filename))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
