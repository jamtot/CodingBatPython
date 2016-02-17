# Given a non-negative number "num",
# return True if num is within 2 of
# a multiple of 10. Note: (a % b)
# is the remainder of dividing a by
# b, so (7 % 5) is 2.

def near_ten(num):
    return (num % 10) not in range (3,8)

def tester(actual, expected):
    if actual == expected:
        print "OK."
    else:
        print "Incorrect."

tester(near_ten(12), True)	    
tester(near_ten(17), False)	    
tester(near_ten(19), True)	    
tester(near_ten(31), True)	    
tester(near_ten(6), False)	    
tester(near_ten(10), True)	    
tester(near_ten(11), True)	    
tester(near_ten(21), True)	    
tester(near_ten(22), True)	    
tester(near_ten(23), False)	    
tester(near_ten(54), False)	    
tester(near_ten(155), False)	    
tester(near_ten(158), True)	    
tester(near_ten(3), False)	    
tester(near_ten(1), True)
