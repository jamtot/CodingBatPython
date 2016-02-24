"""
Given an array length 1 or more of ints, 
return the difference between the largest 
and smallest values in the array. 
Note: the built-in min(v1, v2) and max(v1, v2) 
functions return the smaller or larger of two values. 
"""

from test import Tester

def big_diff(nums):
    largest = smallest = nums[0]
    for elem in nums:
        smallest = min(smallest, elem)
        largest = max(largest, elem)
    return (largest - smallest)
        

Tester(big_diff([10, 3, 5, 6]), 7)
Tester(big_diff([7, 2, 10, 9]), 8)
Tester(big_diff([2, 10, 7, 2]), 8)
Tester(big_diff([2, 10]), 8)
Tester(big_diff([10, 2]), 8)
Tester(big_diff([10, 0]), 10)
Tester(big_diff([2, 3]), 1)
Tester(big_diff([2, 2]), 0)
Tester(big_diff([2]), 0)
Tester(big_diff([5, 1, 6, 1, 9, 9]), 8)
Tester(big_diff([7, 6, 8, 5]), 3)
Tester(big_diff([7, 7, 6, 8, 5, 5, 6]), 3)
