# You are driving a little too fast,
# and a police officer stops you.
# Write code to compute the result,
# encoded as an int value: 0=no ticket,
# 1=small ticket, 2=big ticket. If
# speed is 60 or less, the result is 0.
# If speed is between 61 and 80 inclusive,
# the result is 1. If speed is 81 or more,
# the result is 2. Unless it is your birthday
# -- on that day, your speed can be 5 higher
# in all cases.

def caught_speeding(speed, is_birthday):
    if speed <= 60 or (is_birthday and speed <= 65):
        return 0 # no ticket
    elif speed <= 80 or (is_birthday and speed <= 85):
        return 1 # small ticket
    else:
        return 2 # big ticket
    # could perhaps run check for is_birthday at the start and
    # just take 5 from speed and check as normal

# a function to test the logic problem
def test(function, expected):
    if function == expected:
        print "OK"
    else:
        print "Failed."

test(caught_speeding(60, False), 0)
test(caught_speeding(65, False), 1)
test(caught_speeding(65, True), 0)
test(caught_speeding(80, False), 1)
test(caught_speeding(85, False), 2)
test(caught_speeding(85, True), 1)
test(caught_speeding(70, False), 1)
test(caught_speeding(75, False), 1)
test(caught_speeding(75, True), 1)
test(caught_speeding(40, False), 0)
test(caught_speeding(40, True), 0)
test(caught_speeding(90, False), 2)
