"""
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "". 
"""

def first_two(str):
    # python knows not to go out of bounds with splits
    return str[:2]
    # could always add a length check for 'safety'
