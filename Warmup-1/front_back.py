# Given a string, return a new string where
# the first and last chars have been exchanged. 

def front_back(str):  
    #store the length of the string    
    length = len(str)
    # if the length is greater than 1
    if length > 1:
        # store the first leter of the string using a split
        start = str[:1]
        # store the last letter of the string
        end = str[-1:]
        # get the middle of the string by going from the
        # second index (1) to the second from last (length - 1)
        middle = str[1:length-1] #str[1:-1] works too
        # concatenate these into a new string
        newStr = end + middle + start
    # if not greater than 1    
    else:
        # just copy the string
        newStr = str
    return newStr

# tests the function
def funcTester(answer, expected):
    # if the output is the same as the expected answer    
    if answer == expected:
        print "%r == %r Correct" % (answer, expected)
    else:
        print "%r != %r Incorrect" % (answer, expected)

funcTester(front_back('code'), 'eodc')
funcTester(front_back('a'), 'a')
funcTester(front_back('ab'), 'ba')
funcTester(front_back('abc'), 'cba')
funcTester(front_back(''), '')   
funcTester(front_back('Chocolate'), 'ehocolatC')    
funcTester(front_back('aavJ'), 'Java')    
funcTester(front_back('hello'), 'oellh')
