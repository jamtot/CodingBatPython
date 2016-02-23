"""
Given an array of ints length 3, 
figure out which is larger between 
the first and last elements in the 
array, and set all the other elements 
to be that value. Return the changed array.
"""

from test import Tester

def max_end3(nums):
    max_end = max(nums[0],nums[-1])
    for i in range(len(nums)):
        nums[i] = max_end
    return nums

Tester(max_end3([1, 2, 3]), [3, 3, 3])
Tester(max_end3([11, 5, 9]), [11, 11, 11])
Tester(max_end3([2, 11, 3]), [3, 3, 3])
Tester(max_end3([11, 3, 3]), [11, 11, 11])
Tester(max_end3([3, 11, 11]), [11, 11, 11])
Tester(max_end3([2, 2, 2]), [2, 2, 2])
Tester(max_end3([2, 11, 2]), [2, 2, 2])
Tester(max_end3([0, 0, 1]), [1, 1, 1])
