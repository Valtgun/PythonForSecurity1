import threading
import requests
import time

# Veic http pieprasījumu un izmēra laiku
def fetch(url):
    start_time = time.time()
    response = requests.get(url) # netiek apstrādāts tālāk, tikai laika mērīšanai
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Pieprasījuma izpildes laiks {url}: {time_taken:.2f} sek")

# URL saraksts
urls = [
    "https://www.delfi.lv",
    "https://www.ss.com",
    "https://www.google.com",
    "https://www.github.com"
]

# Paralēlās apstrādes palaišana un laika mērīšana
def fetch_using_threads():
    threads = []
    
    for url in urls:
        thread = threading.Thread(target=fetch, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# MAIN
start_time = time.time()
fetch_using_threads()
end_time = time.time()

total_time = end_time - start_time
print(f"Kopējais laiks: {total_time:.2f} sek")