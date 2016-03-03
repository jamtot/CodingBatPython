"""
Return the sum of the numbers in the array, except ignore sections of 
numbers starting with a 6 and extending to the next 7 (every 6 will be 
followed by at least one 7). Return 0 for no numbers. 
"""

from test import Tester

def sum67(nums):
    sum = 0   
    stop = False 
    if len(nums)>0:
        for num in nums:
            if num is 6:
                stop = True
            elif not stop:
                sum+=num
            elif num is 7:
                stop = False
    return sum    

Tester(sum67([1, 2, 2]), 5)
Tester(sum67([1, 2, 2, 6, 99, 99, 7]), 5)
Tester(sum67([1, 1, 6, 7, 2]), 4)
Tester(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]), 2)
Tester(sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]), 2)
Tester(sum67([2, 7, 6, 2, 6, 7, 2, 7]), 18)
Tester(sum67([2, 7, 6, 2, 6, 2, 7]), 9)
Tester(sum67([1, 6, 7, 7]), 8)
Tester(sum67([6, 7, 1, 6, 7, 7]), 8)
Tester(sum67([6, 8, 1, 6, 7]), 0)
Tester(sum67([]), 0)
Tester(sum67([6, 7, 11]), 11)
Tester(sum67([11, 6, 7, 11]), 22)
Tester(sum67([2, 2, 6, 7, 7]), 11)

