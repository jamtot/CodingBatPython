"""
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count. 
"""

def count_code(str):
    times = 0
    for i in xrange(len(str)-3):
        if "co" in str[i:i+2] and 'e' in str[i+3:i+4]:
            print str[i:i+4]
            times+=1
    return times
