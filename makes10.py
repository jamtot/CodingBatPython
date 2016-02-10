# Given 2 ints, a and b, return True 
# if one if them is 10 or if their sum is 10. 

def makes10(a, b):
    # if a is 10, b is 10, or 
    # the sum of a and b is 10, return True
    return (a == 10 or b == 10 or (a+b) == 10)

# testing the function
def funcTester(answer, expected):
    # if the output is the same as the expected answer    
    if answer == expected:
        print "%r == %r Correct" % (answer, expected)
    else:
        print "%r != %r Incorrect" % (answer, expected)

funcTester(makes10(9, 10), True)
funcTester(makes10(9, 9), False)
funcTester(makes10(1, 9), True)
funcTester(makes10(10, 1), True)
funcTester(makes10(10, 10), True)
funcTester(makes10(8, 2), True)
funcTester(makes10(8, 3), False)
funcTester(makes10(10, 42), True)
funcTester(makes10(12, -2), True)
