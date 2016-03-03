"""
Given an array of ints, return True if the array contains a 2 next to a 
2 somewhere. 
"""

from test import Tester

def has22(nums):
    has2 = False
    for num in nums:
        if num is 2 and has2 is False:
            has2 = True
        elif num is 2 and has2 is True:
            return True
        else:
            has2 = False
    return False

# could also compare nums[i] to nums[i+1] if 2

Tester(has22([1, 2, 2]), True)
Tester(has22([1, 2, 1, 2]), False)
Tester(has22([2, 1, 2]), False)
Tester(has22([2, 2, 1, 2]), True)
Tester(has22([1, 3, 2]), False)
Tester(has22([1, 3, 2, 2]), True)
Tester(has22([2, 3, 2, 2]), True)
Tester(has22([4, 2, 4, 2, 2, 5]), True)
Tester(has22([1, 2]), False)
Tester(has22([2, 2]), True)
Tester(has22([2]), False)
Tester(has22([]), False)
Tester(has22([3, 3, 2, 2]), True)
Tester(has22([5, 2, 5, 2]), False)
