# Given a number n, return True
# if n is in the range 1..10,
# inclusive. Unless "outsideMode"
# is True, in which case return
# True if the number is less or
# equal to 1, or greater or equal
# to 10. 

def in1to10(n, outside_mode):
    return (n in range(1,11) and not outside_mode) or (
            n not in range(2,10) and outside_mode)

def tester(actual, expected):
    if actual == expected:
        print "OK."
    else:
        print "Incorrect."

tester(in1to10(5, False), True)	    
tester(in1to10(11, False), False)	    
tester(in1to10(11, True), True)	    
tester(in1to10(10, False), True)	    
tester(in1to10(10, True), True)	    
tester(in1to10(9, False), True)	    
tester(in1to10(9, True), False)	    
tester(in1to10(1, False), True)	    
tester(in1to10(1, True), True)	    
tester(in1to10(0, False), False)	    
tester(in1to10(0, True), True)	    
tester(in1to10(-1, False), False)
