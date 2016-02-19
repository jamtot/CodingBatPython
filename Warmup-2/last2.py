# Given a string, return the count of
# the number of times that a substring
# length 2 appears in the string and
# also as the last 2 chars of the
# string, so "hixxxhi" yields 1 (we
# won't count the end substring). 

from test import Tester

def last2(str):
    count = 0
    substr = str[-2:]
    for i in range(len(str)-2):
        if str[i:i+2] == substr:
            count+=1
    return count 

Tester(last2("hixxhi"), 1)
Tester(last2("xaxxaxaxx"), 1)
Tester(last2("axxxaaxx"), 2)
Tester(last2('xxaxxaxxaxx'), 3)
Tester(last2('xaxaxaxx'), 0)
Tester(last2('xxxx'), 2)
Tester(last2('13121312'), 1)
Tester(last2('11212'), 1)
Tester(last2('13121311'), 0)
Tester(last2('1717171'), 2)
Tester(last2('hi'), 0)
Tester(last2('h'), 0)
Tester(last2(''), 0)
