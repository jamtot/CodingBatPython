# Given an int n, return True if 
# it is within 10 of 100 or 200. 
# Note: abs(num) computes the 
# absolute value of a number.


def near_hundred(n):
    # if the absolute (non negitive value) of n from
    # the hundred is less than or equal to 10,
    # it is near hundred, return true
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)

# testing the function
def funcTester(answer, expected):
    # if the output is the same as the expected answer    
    if answer == expected:
        print "%r == %r Correct" % (answer, expected)
    else:
        print "%r != %r Incorrect" % (answer, expected)

funcTester(near_hundred(93), True)
funcTester(near_hundred(90), True)
funcTester(near_hundred(89), False)
funcTester(near_hundred(110), True)
funcTester(near_hundred(111), False)
funcTester(near_hundred(121), False)
funcTester(near_hundred(0), False)
funcTester(near_hundred(5), False)
funcTester(near_hundred(191), True)
funcTester(near_hundred(189), False)
funcTester(near_hundred(190), True)
funcTester(near_hundred(200), True)
funcTester(near_hundred(210), True)
funcTester(near_hundred(211), False)
funcTester(near_hundred(290), False)
