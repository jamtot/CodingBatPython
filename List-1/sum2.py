"""
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
"""

from test import Tester

def sum2(nums):
    length = len(nums)
    if length < 1: return 0
    elif length < 2: return nums[0]
    else: return nums[0]+nums[1]

Tester(sum2([1, 2, 3]), 3)
Tester(sum2([1, 1]), 2)
Tester(sum2([1, 1, 1, 1]), 2)
Tester(sum2([1, 2]), 3)
Tester(sum2([1]), 1)
Tester(sum2([]), 0)
Tester(sum2([4, 5, 6]), 9)
Tester(sum2([4]), 4)
