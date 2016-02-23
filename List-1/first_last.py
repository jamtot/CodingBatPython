"""
Given an array of ints, return True if 6 
appears as either the first or last element 
in the array. The array will be length 1 or more.
"""

from test import Tester

def first_last6(nums):
    return (nums[0]==6 or nums[-1]==6)

Tester(first_last6([1, 2, 6]), True)	    
Tester(first_last6([6, 1, 2, 3]), True)	    
Tester(first_last6([13, 6, 1, 2, 3]), False)	    
Tester(first_last6([13, 6, 1, 2, 6]), True)	    
Tester(first_last6([3, 2, 1]), False)	    
Tester(first_last6([3, 6, 1]), False)	    
Tester(first_last6([3, 6]), True)	    
Tester(first_last6([6]), True)	    
Tester(first_last6([3]), False)	    
Tester(first_last6([5, 6]), True)	    
Tester(first_last6([5, 5]), False)	    
Tester(first_last6([1, 2, 3, 4, 6]), True)	    
Tester(first_last6([1, 2, 3, 4]), False)
