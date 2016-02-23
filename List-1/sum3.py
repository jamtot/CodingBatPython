"""
Given an array of ints length 3, return the sum of all the elements. 
"""

from test import Tester

def sum3(nums):
    sum = 0 
    # allows for more elements than simply
    # returning nums[0]+nums[1]+nums[2]   
    for elem in nums: 
        sum+=elem
    return sum

Tester(sum3([1, 2, 3]), 6)
Tester(sum3([5, 11, 2]), 18)
Tester(sum3([7, 0, 0]), 7)
Tester(sum3([1, 2, 1]), 4)
Tester(sum3([1, 1, 1]), 3)
Tester(sum3([2, 7, 2]), 11)
