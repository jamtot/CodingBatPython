"""
Return the number of even ints in the given array.
"""

from test import Tester

def count_evens(nums):
    evens = 0
    for elem in nums:
        if elem % 2 == 0:
            evens+=1
    return evens

Tester(count_evens([2, 1, 2, 3, 4]), 3)
Tester(count_evens([2, 2, 0]), 3)
Tester(count_evens([1, 3, 5]), 0)
Tester(count_evens([]), 0)    
Tester(count_evens([11, 9, 0, 1]), 1)
Tester(count_evens([2, 11, 9, 0]), 2)
Tester(count_evens([2]), 1)
Tester(count_evens([2, 5, 12]), 2)
