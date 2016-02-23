"""
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
"""

from test import Tester

def same_first_last(nums):
    return len(nums)>0 and nums[0]==nums[-1]    

Tester(same_first_last([1, 2, 3]), False)
Tester(same_first_last([1, 2, 3, 1]), True)
Tester(same_first_last([1, 2, 1]), True)
Tester(same_first_last([7]), True)	    
Tester(same_first_last([]), False)	    
Tester(same_first_last([1, 2, 3, 4, 5, 1]), True)	    
Tester(same_first_last([1, 2, 3, 4, 5, 13]), False)	    
Tester(same_first_last([13, 2, 3, 4, 5, 13]), True)	    
Tester(same_first_last([7, 7]), True)
