"""
find_parity_outliers

Given a list, returns the items that are parity outliers.

Use collections.Counter with a list comprehension to count even and odd values in the list, use collections.Counter.most_common() to get the most common parity. Use a list comprehension to find all elements that do not match the most common parity.

find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]

Python, List, Math, Intermediate
"""

from collections import Counter

# print(Counter([1, 2, 3, 4, 6]).most_common())
# for i, c in enumerate([1, 2, 3, 4, 6]):
#     print(i, c)

def find_parity_outliers(nums):
    return [
        x for x in nums 
        if x % 2 != Counter([n % 2 for n in nums]).most_common()[0][0]
    ]

print(find_parity_outliers([1, 2, 3, 4, 6]))