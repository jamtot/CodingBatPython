# We want to make a row of bricks that
# is goal inches long. We have a number
# of small bricks (1 inch each) and
# big bricks (5 inches each). Return
# True if it is possible to make the
# goal by choosing from the given bricks.
# This is a little harder than it looks
# and can be done without any loops.

from test import Tester

def make_bricks(small, big, goal):    
    bigsNeeded = goal/5 # find out how many bigs you need
    if bigsNeeded >= big:   # if you need more bigs than you have
        goal -=  (big*5)    # take what you have from the goal
    else:   # else if you have enough bigs, take them from the goal
        goal -= bigsNeeded*5

    if goal > small:    # if the goal is breater than the amount of smalls you have
        return False    # you don't have enough
    else:   # otherwise you have enough smalls to reach a goal of zero
        return True # you have enough to complete the task

Tester(make_bricks(3, 1, 8), True)	    
Tester(make_bricks(3, 1, 9), False)	    
Tester(make_bricks(3, 2, 10), True)	    
Tester(make_bricks(3, 2, 8), True)	    
Tester(make_bricks(3, 2, 9), False)	    
Tester(make_bricks(6, 1, 11), True)	    
Tester(make_bricks(6, 0, 11), False)	    
Tester(make_bricks(1, 4, 11), True)	    
Tester(make_bricks(0, 3, 10), True)	    
Tester(make_bricks(1, 4, 12), False)	    
Tester(make_bricks(3, 1, 7), True)	    
Tester(make_bricks(1, 1, 7), False)	    
Tester(make_bricks(2, 1, 7), True)	    
Tester(make_bricks(7, 1, 11), True)	    
Tester(make_bricks(7, 1, 8), True)	    
Tester(make_bricks(7, 1, 13), False)	    
Tester(make_bricks(43, 1, 46), True)	    
Tester(make_bricks(40, 1, 46), False)	    
Tester(make_bricks(40, 2, 47), True)	    
Tester(make_bricks(40, 2, 50), True)	    
Tester(make_bricks(40, 2, 52), False)	    
Tester(make_bricks(22, 2, 33), False)	    
Tester(make_bricks(0, 2, 10), True)	    
Tester(make_bricks(1000000, 1000, 1000100), True)	    
Tester(make_bricks(2, 1000000, 100003), False)	    
Tester(make_bricks(20, 0, 19), True)	    
Tester(make_bricks(20, 0, 21), False)	    
Tester(make_bricks(20, 4, 51), False)	    
Tester(make_bricks(20, 4, 39), True)
