"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.
"""

def cat_dog(str):
    cats, dogs = 0, 0
    for i in xrange(len(str)-2):
        curstr = str[i:i+3]
        if curstr == 'cat': cats+=1
        elif curstr == 'dog': dogs+=1
    return dogs==cats
