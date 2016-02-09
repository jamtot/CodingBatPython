# Given two int values, return their sum. 
# Unless the two values are the same, 
# then return double their sum. 

def sum_double(a, b):
    # if the values are the same, 
    if a==b:    
        # double the sum 
        return (a+b)*2
    else:
        # return the sum
        return (a+b)

# tests the function
def funcTester(answer, expected):
    # if the output is the same as the expected answer    
    if answer == expected:
        print "%r == %r Correct" % (answer, expected)
    else:
        print "%r != %r Incorrect" % (answer, expected)

funcTester(sum_double(1, 2), 3)
funcTester(sum_double(3, 2), 5)
funcTester(sum_double(2, 2), 8)
funcTester(sum_double(-1, 0), -1)
funcTester(sum_double(3, 3), 12)
funcTester(sum_double(0, 0), 0)
funcTester(sum_double(0, 1), 1)
funcTester(sum_double(3, 4), 7)

# the sample solution
def sample_sum_double(a, b):
    #store the sum
    sum_ = a+b
    #check for a and b being the same
    if a==b:
        # if so, double sum
        sum_*=2
    # return the sum
    return sum_
