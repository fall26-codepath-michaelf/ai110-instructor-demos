import timeit
import random


random.seed(42)  # same data every run, so numbers are comparable
large_list = [random.randint(0, 100000) for _ in range(100000)]
queries = [random.randint(0, 100000) for _ in range(10000)]


def slow_lookup():
    found = []
    for q in queries:
        if q in large_list:
            found.append(q)
    return found


runs = 1
t = timeit.timeit(slow_lookup, number=runs)
print(f"slow_lookup: {t / runs:.4f} sec per run")
