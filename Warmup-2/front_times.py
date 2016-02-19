# Given a string and a non-negative int n,
# we'll say that the front of the string
# is the first 3 chars, or whatever is
# there if the string is less than length 3.
# Return n copies of the front; 

from test import Tester

def front_times(str, n):
    return str[:3]*n

Tester(front_times('Chocolate', 2), 'ChoCho')	    
Tester(front_times('Chocolate', 3), 'ChoChoCho')	    
Tester(front_times('Abc', 3), 'AbcAbcAbc')
Tester(front_times('Ab', 4), 'AbAbAbAb')   
Tester(front_times('A', 4), 'AAAA')	    
Tester(front_times('', 4), '')   
Tester(front_times('Abc', 0), '')
