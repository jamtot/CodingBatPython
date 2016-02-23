"""
Given an array of ints length 3, 
return a new array with the 
elements in reverse order, so 
{1, 2, 3} becomes {3, 2, 1}. 
"""

from test import Tester

def reverse3(nums):
    reverse = [] # or list()
    for i in range(len(nums)-1, -1, -1):
        reverse.append(nums[i])
    #print reverse
    return reverse

Tester(reverse3([1, 2, 3]), [3, 2, 1])
Tester(reverse3([5, 11, 9]), [9, 11, 5])
Tester(reverse3([7, 0, 0]), [0, 0, 7])
Tester(reverse3([2, 1, 2]), [2, 1, 2])
Tester(reverse3([1, 2, 1]), [1, 2, 1])
Tester(reverse3([2, 11, 3]), [3, 11, 2])
Tester(reverse3([0, 6, 5]), [5, 6, 0])
Tester(reverse3([7, 2, 3]), [3, 2, 7])
