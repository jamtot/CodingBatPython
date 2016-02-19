# Given an array of ints, return True
# if one of the first 4 elements in
# the array is a 9. The array length
# may be less than 4. 

from test import Tester

def array_front9(nums):
    num_range = len(nums)
    if num_range > 4:
        num_range = 4
    for i in range(0,num_range):
        if nums[i]  == 9:
            return True    
    return False
    

Tester(array_front9([1, 2, 9, 3, 4]), True)
Tester(array_front9([1, 2, 3, 4, 9]), False)
Tester(array_front9([1, 2, 3, 4, 5]), False)
Tester(array_front9([9, 2, 3]), True)	    
Tester(array_front9([1, 9, 9]), True)	    
Tester(array_front9([1, 2, 3]), False)	    
Tester(array_front9([1, 9]), True)	    
Tester(array_front9([5, 5]), False)	    
Tester(array_front9([2]), False)	    
Tester(array_front9([9]), True)	    
Tester(array_front9([]), False)	    
Tester(array_front9([3, 9, 2, 3, 3]), True)
