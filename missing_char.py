# Given a non-empty string and an int n,
# return a new string where the char at
# index n has been removed. The value of
# n will be a valid index of a char in
# the original string (i.e. n will be
# in the range 0..len(str)-1 inclusive). 

def missing_char(str, n):
    #returns 2 slices, one up to n, and the other from the
    # letter after n, concatenating the two
    return str[:n] + str [n+1:]


# tests the function
def funcTester(answer, expected):
    # if the output is the same as the expected answer    
    if answer == expected:
        print "%r == %r Correct" % (answer, expected)
    else:
        print "%r != %r Incorrect" % (answer, expected)


funcTester(missing_char('kitten', 1), 'ktten')
funcTester(missing_char('kitten', 0), 'itten')   
funcTester(missing_char('kitten', 4), 'kittn')    
funcTester(missing_char('Hi', 0), 'i') 
funcTester(missing_char('Hi', 1), 'H')    
funcTester(missing_char('code', 0), 'ode')    
funcTester(missing_char('code', 1), 'cde')	    
funcTester(missing_char('code', 2), 'coe')	    
funcTester(missing_char('code', 3), 'cod')	    
funcTester(missing_char('chocolate', 8), 'chocolat')
