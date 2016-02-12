# The squirrels in Palo Alto spend most
# of the day playing. In particular,
# they play if the temperature is between
# 60 and 90 (inclusive). Unless it is
# summer, then the upper limit is 100
# instead of 90. Given an int temperature
# and a boolean is_summer, return True if
# the squirrels play and False otherwise. 

def squirrel_play(temp, is_summer):
    # temp must be above 60, AND the temp should be below 90,
    # OR if it's summer, below 100.
    # return the result of this, true or false
    return ( temp >= 60 and ( temp <= 90 or ( is_summer and temp <= 100 ) ) )

# a function to test the logic problem
def test(function, expected):
    if function == expected:
        print "OK"
    else:
        print "Failed."

test(squirrel_play(70, False), True	)	    
test(squirrel_play(95, False), False)	    
test(squirrel_play(95, True), True	)	    
test(squirrel_play(90, False), True	)	    
test(squirrel_play(90, True), True	)	    
test(squirrel_play(50, False), False)	    
test(squirrel_play(50, True), False	)	    
test(squirrel_play(100, False), False)	    
test(squirrel_play(100, True), True	)	    
test(squirrel_play(105, True), False)	    
test(squirrel_play(59, False), False)	    
test(squirrel_play(59, True), False	)	    
test(squirrel_play(60, False), True	)
