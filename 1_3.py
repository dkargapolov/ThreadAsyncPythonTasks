import threading
import requests

def make_request(url):
    response = requests.get(url)
    print(f"{url}: статус {response.status_code}")

urls = [
    'https://example.com',
    'https://google.com',
    'https://yahoo.com'
]

threads = []
for url in urls:
    thread = threading.Thread(target=make_request, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
