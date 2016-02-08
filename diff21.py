# Given an int n, return the 
# absolute difference between n and 21, 
# except return double the absolute 
# difference if n is over 21. 

def diff21(n):
    # take and store the number 
    # subtracted from 21    
    diff = 21-n
    # if diff is negative,
    # number is greater than 21
    if diff < 0:
        # multiplying by -2 will double,
        # and make number positive
        diff *= -2
    return diff

#sample solution
def samp_diff21(n):
    if n <= 21:
        return 21-n
    else:
        return (n-21)*2

# testing the function
def funcTester(answer, expected):
    # if the output is the same as the expected answer    
    if answer == expected:
        print "%r == %d Correct" % (answer, expected)
    else:
        print "%r != %d Incorrect" % (answer, expected)

funcTester(diff21(19), 2)
funcTester(diff21(10), 11)
funcTester(diff21(21), 0)
funcTester(diff21(22), 2)
funcTester(diff21(25), 8)
funcTester(diff21(30), 18)
funcTester(diff21(0), 21)
funcTester(diff21(1), 20)
funcTester(diff21(2), 19)
funcTester(diff21(-1), 22)
funcTester(diff21(-2), 23)
funcTester(diff21(50), 58)
