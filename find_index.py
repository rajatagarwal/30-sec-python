"""
find_index

Returns the index of the first element in the provided list that satisfies the provided testing function.

find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0

Python, List, Beginner
"""

# def find_index(inp, fn):
#     r = [ x for x in inp if fn(x) ]     # Get list that satisfies the function
#     return inp.index(r[0])

def find_index(inp, fn):
    return next(i for i, x in enumerate(inp) if fn(x))

print(find_index([1, 2, 3, 4], lambda n: n % 2 == 1)) # 0

print(enumerate([1,2,3]))