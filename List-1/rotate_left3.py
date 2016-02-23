"""
Given an array of ints length 3, 
return an array with the elements 
"rotated left" so {1, 2, 3} yields 
{2, 3, 1}. 
"""

from test import Tester

def rotate_left3(nums):
    first=nums[0]
    for i in range(len(nums)-1):
        nums[i] = nums[i+1]
    nums[-1]=first
    return nums

Tester(rotate_left3([1, 2, 3]), [2, 3, 1])
Tester(rotate_left3([5, 11, 9]), [11, 9, 5])
Tester(rotate_left3([7, 0, 0]), [0, 0, 7])
Tester(rotate_left3([1, 2, 1]), [2, 1, 1])
Tester(rotate_left3([0, 0, 1]), [0, 1, 0])
