"""
Return the number of times that the string "hi" appears anywhere in the given string. 
"""

def count_hi(str):
    times = 0
    for i in xrange(len(str)-1):
        if str[i:i+2] == 'hi': times+=1
    return times
