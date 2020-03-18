"""
bifurcate

Splits the value into two groups. If an element in filter is True, the corresponding element in the collection belongs to the first group otherwise it belongs to the second group.

Use list comprehension and enumerate() to add element to the group, based on filter.

bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True]) # [ ['beep', 'boop', 'bar'], ['foo'] ]

Python, list, intermediate
"""


# def bifurcate(l1, l2):
#     r1 = []
#     r2 = []
#     for i1, i2 in zip(l1, l2):
#         if i2 == True:
#             r1.append(i1)
#         else:
#             r2.append(i1)
#     print(r1, r2)

def bifurcate(lst, filter):
    print( [ 
        [ x for i, x in enumerate(lst) if filter[i] == True],
        [ x for i, x in enumerate(lst) if filter[i] == False]
    ] )



bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True]) # [ ['beep', 'boop', 'bar'], ['foo'] ]