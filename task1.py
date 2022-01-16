import threading
import multiprocessing
import os
import random
import requests
import string
from multiprocessing.pool import ThreadPool
from contexttimer import Timer


def fetch_pic(num_pic):
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    for _ in range(num_pic):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)


# S = 1 / (0.01 + ((1 - 0.01) / 100)) = 50.25
# S = 1 / (0.01 + ((1 - 0.01) / 99)) = 50
# 100 workers - 2.6623870999901555 s
# 99 workers - 2.935737200008589 s
# so optimum point == DATA_SIZE


workers = 99
DATA_SIZE = 100

with Timer() as t:
    with ThreadPool(workers) as pool:
        input_data = [DATA_SIZE // workers for _ in range(workers)]
        pool.map(fetch_pic, input_data)

print(t.elapsed)
