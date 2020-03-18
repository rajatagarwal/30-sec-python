"""
difference

Returns the difference between 2 iterables.

Python, List, Beginner
"""
import time

start_time = time.time()

def difference(a, b):
    _b = set(b)
    print([item for item in a if item not in b])

difference([1, 2, 3], [1, 2, 4])

print(f"---- {time.time() - start_time} seconds ----")