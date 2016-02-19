# Given an array of ints, return
# the number of 9's in the array. 

from test import Tester

def array_count9(nums):
    count = 0    
    for num in nums:
        if num == 9:
            count += 1
    return count

Tester(array_count9([1, 2, 9]), 1)
Tester(array_count9([1, 9, 9]), 2)
Tester(array_count9([1, 9, 9, 3, 9]), 3)
Tester(array_count9([1, 2, 3]), 0)
Tester(array_count9([]), 0) 
Tester(array_count9([4, 2, 4, 3, 1]), 0)
Tester(array_count9([9, 2, 4, 3, 1]), 1)
