"""
frequencies

Returns a dictionary with unique values of a list as keys and their frequecies as values.

Python, list, intermediate

(['a', 'b', 'a', 'c', 'a', 'a', 'b']) # { 'a': 4, 'b': 2, 'c': 1 }
"""

def frequecies(l):
    d = {}
    for i in l:
        d[i] = d[i] + 1 if i in d else 1
    print(d)


frequecies(['a', 'b', 'a', 'c', 'a', 'a', 'b'])