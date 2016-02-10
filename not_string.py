# Given a string, return 
# a new string where "not "
# has been added to the front.
# However, if the string already
# begins with "not",
# return the string unchanged. 

def not_string(str):
    # if the string isn't tood short to start with 'not'    
    if len(str) > 2 and (str[0] == 'n' and str[1] == 'o' and str[2] == 't'):
        return str
    # if not, add not
    return ("not " + str)

# the example solution uses a slice of the string, 
# taking up to but not including the 3rd index
def example_not_string(str):
    if len(str) >= 3 and str[:3] == 'not':
        return str
    return "not " + str

# testing the function
def funcTester(answer, expected):
    # if the output is the same as the expected answer    
    if answer == expected:
        print "%r == %r Correct" % (answer, expected)
    else:
        print "%r != %r Incorrect" % (answer, expected)

funcTester(not_string('candy'), 'not candy') 
funcTester(not_string('x'), 'not x')  
funcTester(not_string('not bad'), 'not bad')   
funcTester(not_string('bad'), 'not bad')
funcTester(not_string('not'), 'not')  
funcTester(not_string('is not'), 'not is not')  
funcTester(not_string('no'), 'not no')
