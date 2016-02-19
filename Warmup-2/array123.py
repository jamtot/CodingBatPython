# Given an array of ints, return True
# if .. 1, 2, 3, .. appears in the
# array somewhere. 

from test import Tester

def array123(nums):
    end = len(nums) - 2
    for i in range(end):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

Tester(array123([1, 1, 2, 3, 1]), True)
Tester(array123([1, 1, 2, 4, 1]), False)
Tester(array123([1, 1, 2, 1, 2, 3]), True)
Tester(array123([1, 1, 2, 1, 2, 1]), False)
Tester(array123([1, 2, 3, 1, 2, 3]), True)
Tester(array123([1, 2, 3]), True)
Tester(array123([1, 1, 1]), False)
Tester(array123([1, 2]), False)
Tester(array123([1]), False)
Tester(array123([]), False)
