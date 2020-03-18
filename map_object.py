"""
map_object

Maps a value of a list to dictionary using a function, where key-value pair consists of original value as key and the result of function as the output

map_object([1,2,3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }

Python, List, Intermediate
"""


def map_object(l, f):
    d = {}
    for i in l:
        d[i] = f(i)     # You can call lambda function like a normal function
    print(d)


map_object([1,2,3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }