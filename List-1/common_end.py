"""
Given 2 arrays of ints, a and b, return True 
if they have the same first element or they 
have the same last element. Both arrays will 
be length 1 or more. 
"""

from test import Tester

def common_end(a, b):
    return (a[0]==b[0] or a[-1]==b[-1])

Tester(common_end([1, 2, 3], [7, 3]), True)
Tester(common_end([1, 2, 3], [7, 3, 2]), False)
Tester(common_end([1, 2, 3], [1, 3]), True)
Tester(common_end([1, 2, 3], [1]), True)	    
Tester(common_end([1, 2, 3], [2]), False)
