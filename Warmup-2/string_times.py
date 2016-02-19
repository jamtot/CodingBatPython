# Given a string and a non-negative int n,
# return a larger string that is n copies
# of the original string. 

def string_times(str, n):
    return str*n

def tester(actual, expected):
    if actual == expected:
        print "OK."
    else:
        print "Incorrect."

tester(string_times('Hi', 2), 'HiHi')
tester(string_times('Hi', 3), 'HiHiHi')
tester(string_times('Hi', 1), 'Hi')
tester(string_times('Hi', 0), '')
tester(string_times('Hi', 5), 'HiHiHiHiHi')
tester(string_times('Oh Boy!', 2), 'Oh Boy!Oh Boy!')
tester(string_times('x', 4), 'xxxx')
tester(string_times('', 4), '')
tester(string_times('code', 2), 'codecode')
tester(string_times('code', 3), 'codecodecode')
