"""
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done. 
"""

from test import Tester

def make_chocolate(small, big, goal):
    bigsNeeded = goal/5 # find out how many bigs you need
    if bigsNeeded >= big:   # if you need more bigs than you have
        goal -=  (big*5)    # take what you have from the goal
    else:   # else if you have enough bigs, take them from the goal
        goal -= bigsNeeded*5

    if goal > small:    # if the goal is breater than the amount of smalls you have
        return -1    # you don't have enough
    else:   # otherwise you have enough smalls to reach a goal
        return goal # return the amount of smalls needed

Tester(make_chocolate(4, 1, 9), 4)  
Tester(make_chocolate(4, 1, 10), -1)   
Tester(make_chocolate(4, 1, 7), 2)    
Tester(make_chocolate(6, 2, 7), 2)   
Tester(make_chocolate(4, 1, 5), 0)   
Tester(make_chocolate(4, 1, 4), 4)    
Tester(make_chocolate(5, 4, 9), 4)   
Tester(make_chocolate(9, 3, 18), 3)   
Tester(make_chocolate(3, 1, 9), -1)   
Tester(make_chocolate(1, 2, 7), -1)
Tester(make_chocolate(1, 2, 6), 1)
Tester(make_chocolate(1, 2, 5), 0)
Tester(make_chocolate(6, 1, 10), 5)
Tester(make_chocolate(6, 1, 11), 6)
Tester(make_chocolate(6, 1, 12), -1)
Tester(make_chocolate(6, 1, 13), -1) 
Tester(make_chocolate(6, 2, 10), 0) 
Tester(make_chocolate(6, 2, 11), 1)
Tester(make_chocolate(6, 2, 12), 2)  
Tester(make_chocolate(60, 100, 550), 50) 
Tester(make_chocolate(1000, 1000000, 5000006), 6)
Tester(make_chocolate(7, 1, 12), 7)
Tester(make_chocolate(7, 1, 13), -1)
Tester(make_chocolate(7, 2, 13), 3)
