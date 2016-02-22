"""
For this problem, we'll round an int value up to the 
next multiple of 10 if its rightmost digit is 5 or more, 
so 15 rounds up to 20. Alternately, round down to the 
previous multiple of 10 if its rightmost digit is less 
than 5, so 12 rounds down to 10. Given 3 ints, a b c, 
return the sum of their rounded values. To avoid code 
repetition, write a separate helper "def round10(num):" 
and call it 3 times. Write the helper entirely below and 
at the same indent level as round_sum().
"""

from test import Tester

def round_sum(a, b, c):
    return round10(a)+round10(b)+round10(c)
    
def round10(num):
    diff = num%10
    if (diff>=5):return (num-diff)+10
    else: return num-diff

Tester(round_sum(16, 17, 18), 60)
Tester(round_sum(12, 13, 14), 30)
Tester(round_sum(6, 4, 4), 10)
Tester(round_sum(4, 6, 5), 20)
Tester(round_sum(4, 4, 6), 10)
Tester(round_sum(9, 4, 4), 10)
Tester(round_sum(0, 0, 1), 0)
Tester(round_sum(0, 9, 0), 10)
Tester(round_sum(10, 10, 19), 40)
Tester(round_sum(20, 30, 40), 90)
Tester(round_sum(45, 21, 30), 100)
Tester(round_sum(23, 11, 26), 60)
Tester(round_sum(23, 24, 25), 70)
Tester(round_sum(25, 24, 25), 80)
Tester(round_sum(23, 24, 29), 70)
Tester(round_sum(11, 24, 36), 70)
Tester(round_sum(24, 36, 32), 90)
Tester(round_sum(14, 12, 26), 50)
Tester(round_sum(12, 10, 24), 40)
