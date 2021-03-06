# Given 3 int values, a b c,
# return their sum. However,
# if one of the values is 13
# then it does not count
# towards the sum and values
# to its right do not count.
# So for example, if b is 13,
# then both b and c do not count. 

from test import Tester

def lucky_sum_1(a, b, c):
    sum = 0
    if (a != 13): sum+=a
    else: return sum
    if (b != 13): sum+=b
    else: return sum
    if (c != 13): sum+=c
    else: return sum
    return sum

#rewrote it to be a lot more efficient
def lucky_sum(a, b, c):
    if (a==13): return 0
    elif (b==13): return a
    elif (c==13): return a+b
    else: return a+b+c
    

Tester(lucky_sum(1, 2, 3), 6)
Tester(lucky_sum(1, 2, 13), 3)
Tester(lucky_sum(1, 13, 3), 1)
Tester(lucky_sum(1, 13, 13), 1)    
Tester(lucky_sum(6, 5, 2), 13)    
Tester(lucky_sum(13, 2, 3), 0)
Tester(lucky_sum(13, 2, 13), 0)
Tester(lucky_sum(13, 13, 2), 0)
Tester(lucky_sum(9, 4, 13), 13)
Tester(lucky_sum(8, 13, 2), 8)
Tester(lucky_sum(7, 2, 1), 10)
Tester(lucky_sum(3, 3, 13), 6)
