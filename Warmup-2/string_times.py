# Given a string and a non-negative int n,
# return a larger string that is n copies
# of the original string. 

from test import Tester

def string_times(str, n):
    return str*n

Tester(string_times('Hi', 2), 'HiHi')
Tester(string_times('Hi', 3), 'HiHiHi')
Tester(string_times('Hi', 1), 'Hi')
Tester(string_times('Hi', 0), '')
Tester(string_times('Hi', 5), 'HiHiHiHiHi')
Tester(string_times('Oh Boy!', 2), 'Oh Boy!Oh Boy!')
Tester(string_times('x', 4), 'xxxx')
Tester(string_times('', 4), '')
Tester(string_times('code', 2), 'codecode')
Tester(string_times('code', 3), 'codecodecode')
