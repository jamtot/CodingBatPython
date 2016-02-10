# We have a loud talking parrot. 
# The "hour" parameter is the current 
# hour time in the range 0..23. We are 
# in trouble if the parrot is talking 
# and the hour is before 7 or after 20. 
# Return True if we are in trouble. 

def parrot_trouble(talking, hour):
    # if talking is true AND the hour is before 7, or after 20
    # return true, otherwise it is false
    return (talking and (hour < 7 or hour > 20))

# testing the function
def funcTester(answer, expected):
    # if the output is the same as the expected answer    
    if answer == expected:
        print "%r == %r Correct" % (answer, expected)
    else:
        print "%r != %r Incorrect" % (answer, expected)

funcTester(parrot_trouble(True, 6), True)
funcTester(parrot_trouble(True, 7), False)
funcTester(parrot_trouble(False, 6), False)
funcTester(parrot_trouble(True, 21), True)
funcTester(parrot_trouble(False, 21), False)
funcTester(parrot_trouble(False, 20), False)
funcTester(parrot_trouble(True, 23), True)
funcTester(parrot_trouble(False, 23), False)
funcTester(parrot_trouble(True, 20), False)
funcTester(parrot_trouble(False, 12), False)
