import concurrent.futures
import math
from functools import partial


def integrate(y, a, b, *, n_iter=1000):
    h = (b - a) / n_iter
    x = a + h
    s = 0
    while x <= (b - h):
        s += y(x)
        x += h
    res = h * ((y(a) + y(b)) / 2 + s)
    return round(res, 8)


def integrate_async(f, a, b, *, n_jobs=2, n_iter=1000):
    with concurrent.futures.ThreadPoolExecutor(n_jobs) as executor:
        spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)
        step = (b - a) / n_jobs
        fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
        sum_not_round = sum(f.result() for f in concurrent.futures.as_completed(fs))
        return round(sum_not_round, 8)
    

import timeit

print("Time 1: ", timeit.timeit("integrate_async(f1, 0, 5, n_iter=100)", setup="from main import integrate_async; from tests import math, f1", number=1000))
print("Time 2: ", timeit.timeit("integrate_async(f2, 0, 7, n_iter=50)", setup="from main import integrate_async; from tests import math, f2", number=1000))
print("Time 3: ", timeit.timeit("integrate_async(f3, 0, 0.01, n_iter=10)", setup="from main import integrate_async; from tests import math, f3", number=1000))
