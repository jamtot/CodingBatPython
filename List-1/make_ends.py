"""
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more. 
"""

from test import Tester

def make_ends(nums):
    endList = [nums[0],nums[-1]]    
    return endList

Tester(make_ends([1, 2, 3]), [1, 3])
Tester(make_ends([1, 2, 3, 4]), [1, 4])
Tester(make_ends([7, 4, 6, 2]), [7, 2])
Tester(make_ends([1, 2, 2, 2, 2, 2, 2, 3]), [1, 3])
Tester(make_ends([7, 4]), [7, 4]) 
Tester(make_ends([7]), [7, 7]) 
Tester(make_ends([5, 2, 9]), [5, 9])  
Tester(make_ends([2, 3, 4, 1]), [2, 1])
