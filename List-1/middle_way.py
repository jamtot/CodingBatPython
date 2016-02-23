"""
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements. 
"""

from test import Tester

def middle_way(a, b):
    middle_list = []
    middle_list.append(a[1])
    middle_list.append(b[1])
    return middle_list

# made to suit variable sizes of arrays/lists
def middle_way2(a, b):
    middle_list = []
    # dividing an uneven int truncates,
    # suiting the middle, due to 0 index 
    # which side is the middle of an even number
    # is up to interpretation
    halfa = ( len(a) / 2 ) 
    halfb = ( len(b) / 2 ) 
    middle_list.append(a[halfa])
    middle_list.append(b[halfb])
    return middle_list


Tester(middle_way([1, 2, 3], [4, 5, 6]), [2, 5])
Tester(middle_way([7, 7, 7], [3, 8, 0]), [7, 8])
Tester(middle_way([5, 2, 9], [1, 4, 5]), [2, 4])
Tester(middle_way([1, 9, 7], [4, 8, 8]), [9, 8])
Tester(middle_way([1, 2, 3], [3, 1, 4]), [2, 1])
Tester(middle_way([1, 2, 3], [4, 1, 1]), [2, 1])
