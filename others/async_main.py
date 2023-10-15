from concurrent.futures import ThreadPoolExecutor
import requests
import random
import time
URL = "https://httpbin.org/delay"


def fetch_with_delay(delay):
    response = requests.get('/'.join([URL, str(delay)]))
    print(f"Ran with delay of {delay}")
    return response.json()


if __name__=='__main__':
    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(fetch_with_delay, [random.randint(1, 6) for _ in range(10)])
        executor.shutdown(wait=True)

    print(f"Thread finished in {time.time()-start} s")

    for result in results:
        print(result)

