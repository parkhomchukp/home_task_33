import threading
import multiprocessing
import os
import random
import requests
import string
from multiprocessing.pool import ThreadPool
from contexttimer import Timer

DATA_SIZE = 1_000_000
workers = 8
lst = []


def fill_data(n):
    while n > 0:
        n -= 1
        lst.append(random.randint(1, 100))


if __name__ == "__main__":
    with Timer() as t:
        with multiprocessing.Pool(workers) as pool:
            input_data = [DATA_SIZE // workers for _ in range(workers)]
            pool.map(fill_data, input_data)

    print(t.elapsed)
