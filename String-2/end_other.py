"""
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string. 
"""

def end_other(a, b):
    lena, lenb = len(a), len(b)
    if (a.lower() == (b.lower())[-lena:]) or (
        (a.lower())[-lenb:] == b.lower()):
        return True
    return False

    #or
    #a, b = a.lower(), b.lower()
    # did not know about this one; makes it much easier
    #return (b.endswith(a) or a.endswith(b)) 
