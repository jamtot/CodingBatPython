"""
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0). 
"""

def combo_string(a, b):
    #if (len(a) > len(b)):
    #    return "%s%s%s" % (b,a,b)
    #else:
    #    return "%s%s%s" % (a,b,a)

    #or
    if (len(a) > len(b)):
        a,b = b,a # this is so cool
    return "%s%s%s" % (a,b,a)
