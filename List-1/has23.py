"""
Given an int array length 2, return True if it contains a 2 or a 3. 
"""

from test import Tester

def has23(nums):
    for elem in nums:
        if elem is 2 or elem is 3: return True
    return False


# not working yet
#def has23(nums):
#    return all( (elem == 2 or elem == 3) for elem in nums)

Tester(has23([2, 5]), True)
Tester(has23([4, 3]), True)
Tester(has23([4, 5]), False)
Tester(has23([2, 2]), True)
Tester(has23([3, 2]), True)
Tester(has23([3, 3]), True)
Tester(has23([7, 7]), False)
Tester(has23([3, 9]), True)
Tester(has23([9, 5]), False)
