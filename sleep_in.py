# The parameter weekday is True if it is a weekday, 
# and the parameter vacation is True if we are on vacation. 
# We sleep in if it is not a weekday or we're on vacation. 
# Return True if we sleep in. 

def orig_sleep_in(weekday, vacation):
    # if it's a weekday    
    if weekday:
        # if it's a vacation day
        if vacation:
            # you can sleep in :D
            return True
        # if it's not a vacation day        
        else:
            # you can't sleep in :(
            return False
    # if it's not a weekday    
    else:
        # you can sleep in :D
        return True

# rewote to be a lot shorter
# this is why I need practice
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

# testing the function
def funcTester(answer, expected):
    # if the output is the same as the expected answer    
    if answer == expected:
        print "%r == %r Correct" % (answer, expected)
    else:
        print "%r != %r Incorrect" % (answer, expected)

funcTester(sleep_in(True,True), True)
funcTester(sleep_in(False,True), True)
funcTester(sleep_in(True,False), False)
funcTester(sleep_in(False,False), True)
