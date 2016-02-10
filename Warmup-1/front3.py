# Given a string, we'll say that the
# front is the first 3 chars of the string.
# If the string length is less than 3,
# the front is whatever is there.
# Return a new string which is 3 copies of the front. 

def front3(str):
    # knowing that a split will never
    # return out of bounds
    return str[:3]*3

# the sample solution on CodingBat
def example_front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front 

# tests the function
def funcTester(answer, expected):
    # if the output is the same as the expected answer    
    if answer == expected:
        print "%r == %r Correct" % (answer, expected)
    else:
        print "%r != %r Incorrect" % (answer, expected)

funcTester(front3('Java'), 'JavJavJav')
funcTester(front3('Chocolate'), 'ChoChoCho')  
funcTester(front3('abc'), 'abcabcabc')   
funcTester(front3('abcXYZ'), 'abcabcabc')  
funcTester(front3('ab'), 'ababab') 
funcTester(front3('a'), 'aaa')
funcTester(front3(''), '')
