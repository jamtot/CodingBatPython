# Given 3 int values, a b c,
# return their sum. However,
# if any of the values is a
# teen -- in the range 13..19
# inclusive -- then that
# value counts as 0, except
# 15 and 16 do not count as a
# teens. Write a separate
# helper "def fix_teen(n):"that
# takes in an int value and
# returns that value fixed for
# the teen rule. In this way,
# you avoid repeating the teen
# code 3 times (i.e. "decomposition").
# Define the helper below and at the
# same indent level as the main
# no_teen_sum(). 

from test import Tester

def no_teen_sum(a, b, c):
    return fix_teen(a)+fix_teen(b)+fix_teen(c)

def fix_teen(n):
    if n in range(13,20) and n != 15 and n != 16:
        return 0
    else:
        return n
        
Tester(no_teen_sum(1, 2, 3), 6)	    
Tester(no_teen_sum(2, 13, 1), 3)
Tester(no_teen_sum(2, 1, 14), 3)
Tester(no_teen_sum(2, 1, 15), 18)
Tester(no_teen_sum(2, 1, 16), 19)
Tester(no_teen_sum(2, 1, 17), 3)
Tester(no_teen_sum(17, 1, 2), 3)
Tester(no_teen_sum(2, 15, 2), 19)
Tester(no_teen_sum(16, 17, 18), 16) 
Tester(no_teen_sum(17, 18, 19), 0)
Tester(no_teen_sum(15, 16, 1), 32)
Tester(no_teen_sum(15, 15, 19), 30)
Tester(no_teen_sum(15, 19, 16), 31)
Tester(no_teen_sum(5, 17, 18), 5)
Tester(no_teen_sum(17, 18, 16), 16)   
Tester(no_teen_sum(17, 19, 18), 0)
