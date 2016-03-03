"""
Return the sum of the numbers in the array, returning 0 for an empty 
array. Except the number 13 is very unlucky, so it does not count and 
numbers that come immediately after a 13 also do not count. 
"""

from test import Tester

def sum13(nums):
    sum = 0
    unlucky = False    
    if len(nums) > 0:
        for num in nums:
            if num is 13:
                unlucky = True
            elif not unlucky:
                sum+=num
            else:
                unlucky = False  
    return sum

Tester(sum13([1, 2, 2, 1]), 6)
Tester(sum13([1, 1]), 2)
Tester(sum13([1, 2, 2, 1, 13]), 6)
Tester(sum13([1, 2, 13, 2, 1, 13]), 4)
Tester(sum13([13, 1, 2, 13, 2, 1, 13]), 3)
Tester(sum13([]), 0)
Tester(sum13([13]), 0)
Tester(sum13([13, 13]), 0)
Tester(sum13([13, 0, 13]), 0)
Tester(sum13([13, 1, 13]), 0)
Tester(sum13([5, 7, 2]), 14)
Tester(sum13([5, 13, 2]), 5)
Tester(sum13([0]), 0)
Tester(sum13([13, 0]), 0)
Tester(sum13([1,1,13,1,1,13,13,13,1,1,1,1,13,1,1,13,13,1,1]), 8)
