# Given 2 strings, a and b, return
# the number of the positions where
# they contain the same length 2
# substring. So "xxcaazz" and
# "xxbaaz" yields 3, since the
# "xx", "aa", and "az" substrings
# appear in the same place in both
# strings. 

from test import Tester

def string_match(a, b):
    count = 0
    #previously had an if statement, this is much simpler
    end = min(len(a), len(b)) - 1
    for i in range(end):
        if a[i:i+2] == b[i:i+2]:
            count +=1
    return count
    
   
Tester(string_match('xxcaazz', 'xxbaaz'), 3)
Tester(string_match('abc', 'abc'), 2)
Tester(string_match('abc', 'axc'), 0)
Tester(string_match('hello', 'he'), 1)
Tester(string_match('he', 'hello'), 1)
Tester(string_match('h', 'hello'), 0)
Tester(string_match('', 'hello'), 0)
Tester(string_match('aabbccdd', 'abbbxxd'), 1)
Tester(string_match('aaxxaaxx', 'iaxxai'), 3)
Tester(string_match('iaxxai', 'aaxxaaxx'), 3)
