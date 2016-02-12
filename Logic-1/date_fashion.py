#You and your date are trying to get a table
# at a restaurant. The parameter "you" is
# the stylishness of your clothes, in the range
# 0..10, and "date" is the stylishness of your
# date's clothes. The result getting the table
# is encoded as an int value with 0=no, 1=maybe,
# 2=yes. If either of you is very stylish, 8 or
# more, then the result is 2 (yes). With the
# exception that if either of you has style of 2
# or less, then the result is 0 (no). Otherwise
# the result is 1 (maybe). 

def date_fashion(you, date):
    # with style of 2 or less being the exception,
    # check for that first     
    if you < 3 or date < 3:
        return 0  # no chance of table  
    # if you or your date has a style of 8 or more
    elif you > 7 or date > 7:
        return 2 # you will get a table
    else: # everything in between
        return 1    # maybe you'll get a table

# a function to test the logic problem
def test(function, expected):
    if function == expected:
        print "OK"
    else:
        print "Failed."

test(date_fashion(5, 10), 2) 
test(date_fashion(5, 2), 0)
test(date_fashion(5, 5), 1)    
test(date_fashion(3, 3), 1)  
test(date_fashion(10, 2), 0)
test(date_fashion(2, 9), 0)  
test(date_fashion(9, 9), 2)
test(date_fashion(10, 5), 2)
test(date_fashion(2, 2), 0)
test(date_fashion(3, 7), 1)
test(date_fashion(2, 7), 0)
test(date_fashion(6, 2), 0)
