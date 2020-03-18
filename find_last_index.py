"""
NOT FULLY UNDERSTOOD THE SOLUTION

find_last_index

Returns the index of the last element in the provided list that satisfies the provided testing function.

Use list comprehension, enumerate() and next() to return the index of the last element in lst for which fn returns True.

find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2

Python, List, Beginner
"""

def find_last_index(inp, fn):
    return len(inp) - 1 - next(i for i, x in enumerate(inp[::-1]) if fn(x))
    # return len(inp) - 1 - next(i for i, x in enumerate(inp[::-1]) if fn(x))
    # return inp[::-1]

print(find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1)) # 2
