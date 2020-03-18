"""
bifurcate_by

Splits values into two groups according to a function, which specifies which group an element in the input list belongs to. If the function returns True, the element belongs to the first group; otherwise, it belongs to the second group.

bifurcate_by(
  ['beep', 'boop', 'foo', 'bar'], 
  lambda x: x[0] == 'b'
) # [ ['beep', 'boop', 'bar'], ['foo'] ]

Python, List, Function, Intermediate
""" 

def bifurcate_by(inp, fn):
    return [
        [x for x in inp if fn(x)],
        [x for x in inp if not fn(x)]
    ]  

print(bifurcate_by(
  ['beep', 'boop', 'foo', 'bar'], 
  lambda x: x[0] == 'b'
)) # [ ['beep', 'boop', 'bar'], ['foo'] ]