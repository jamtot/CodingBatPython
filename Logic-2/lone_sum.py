# Given 3 int values, a b c,
# return their sum. However,
# if one of the values is the
# same as another of the
# values, it does not count
# towards the sum.

from test import Tester

def lone_sum(a, b, c): 
    if (a==b and b==c):
        return 0
    if (a==b): 
        a = 0
        b = 0
    if (b==c):
        b = 0
        c = 0
    if (a==c):
        a = 0
        c = 0
    return a+b+c

#example solution checks each number against the others
def ex_lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  
  return sum
        

Tester(lone_sum(1, 2, 3), 6)
Tester(lone_sum(3, 2, 3), 2)
Tester(lone_sum(3, 3, 3), 0)
Tester(lone_sum(9, 2, 2), 9)	    
Tester(lone_sum(2, 2, 9), 9)
Tester(lone_sum(2, 9, 2), 9)
Tester(lone_sum(2, 9, 3), 14)
Tester(lone_sum(4, 2, 3), 9)
Tester(lone_sum(1, 3, 1), 3)
