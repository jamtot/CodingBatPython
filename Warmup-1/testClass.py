# a class for the test function I am using on all the warmup programs
class TestClass:

    def __init__(self):
        print "TestClass created."

    # function tester - if the output matches the 
    # expected output, the answer is correct
    def funcTester(answer, expected):
        # if the output is the same as the expected answer    
        if answer == expected:
            print "%r == %r Correct" % (answer, expected)
        else:
            print "%r != %r Incorrect" % (answer, expected)
