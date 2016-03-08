"""
Given a string, return a string where for every char in the original, there are two chars. 
"""

def double_char(str):
    result = ''
    for letter in str:
        result+=letter+letter
    return result
