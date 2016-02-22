"""
Given three ints, a b c, return True if one of b or c is
 "close" (differing from a by at most 1), while the other
 is "far", differing from both other values by 2 or more.
 Note: abs(num) computes the absolute value of a number. 
"""

from test import Tester

def close_far(a, b, c):
    check1 = close_far_checker(a,b,c)
    check2 = close_far_checker(a,c,b)
    return (check1 and not check2) or (
        not check1 and check2)
        
# checks for the 'close'ness of numbers against a,
# then checks if the remaining number is 'far'
def close_far_checker(num,num1,num2):
    if abs(num-num1)<2:
        if abs(num2-num)>1 and abs(num2-num1)>1:
            return True
    return False

Tester(close_far(1, 2, 10), True)
Tester(close_far(1, 2, 3), False)
Tester(close_far(4, 1, 3), True)
Tester(close_far(4, 5, 3), False)	    
Tester(close_far(4, 3, 5), False)	    
Tester(close_far(-1, 10, 0), True)	    
Tester(close_far(0, -1, 10), True)	    
Tester(close_far(10, 10, 8), True)	    
Tester(close_far(10, 8, 9), False)	    
Tester(close_far(8, 9, 10), False)	    
Tester(close_far(8, 9, 7), False)	    
Tester(close_far(8, 6, 9), True)
