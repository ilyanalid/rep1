import multiprocessing
import random
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


def q_dot(v1, v2, q):
    q.send(np.dot(v1, v2))
    return q


if __name__ == '__main__':
    multiprocessing.freeze_support()
    a = np.random.randint(10**3, size=10**6)
    b = np.random.randint(10**3, size=10**6)
    q, v = multiprocessing.Pipe()
    a1 = np.array_split(a, 2)
    b1 = np.array_split(b,2)
    processes = []
    for first, second, conn in zip(a1, b1, [q, v]):
        processes.append(multiprocessing.Process(target=q_dot, args=(first, second, conn)))
    for i in processes:
        i.start()
    for i in processes:
        i.join()
    s = 0
    s += q.recv()
    s += v.recv()
    print(s)
