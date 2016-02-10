# Given 2 int values, return True
# if one is negative and one is positive.
# Except if the parameter "negative" is True,
# then return True only if both are negative. 

def pos_neg(a, b, negative):
    # negative isn't true, and a and b are pos and neg
    return (not negative and (a < 0) != (b < 0) ) or (
        # if negative is true, and a and b are negative       
        negative and (a < 0) and (b < 0) )

def pos_neg2(a, b, negative):
    #a bit less messy solution   
    if negative:
        return a<0 and b<0
    else:
        return (a<0) != (b<0)

# the solution given by CodingBat
def samp_pos_neg(a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))


# tests the function
def funcTester(answer, expected):
    # if the output is the same as the expected answer    
    if answer == expected:
        print "%r == %r Correct" % (answer, expected)
    else:
        print "%r != %r Incorrect" % (answer, expected)

funcTester(pos_neg(1, -1, False), True)
funcTester(pos_neg(-1, 1, False), True)
funcTester(pos_neg(-4, -5, True), True)
funcTester(pos_neg(-4, -5, False), False)
funcTester(pos_neg(-4, 5, False), True)
funcTester(pos_neg(-4, 5, True), False)
funcTester(pos_neg(1, 1, False), False)
funcTester(pos_neg(-1, -1, False), False)
funcTester(pos_neg(1, -1, True), False)
funcTester(pos_neg(-1, 1, True), False)  
funcTester(pos_neg(1, 1, True), False)
funcTester(pos_neg(-1, -1, True), True)    
funcTester(pos_neg(5, -5, False), True)    
funcTester(pos_neg(-6, 6, False), True)
funcTester(pos_neg(-5, -6, False), False)
funcTester(pos_neg(-2, -1, False), False)   
funcTester(pos_neg(1, 2, False), False)
funcTester(pos_neg(-5, 6, True), False) 
funcTester(pos_neg(-5, -5, True), True)
