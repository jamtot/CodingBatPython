def sorta_sum(a, b):
    sum = a+b    
    if sum >= 10 and sum < 20:
        return 20
    return sum

def tester(actual, expected):
    if actual == expected:
        print "OK."
    else:
        print "Incorrect."

tester(sorta_sum(3, 4), 7  )  
tester(sorta_sum(9, 4), 20  ) 
tester(sorta_sum(10, 11), 21)
tester(sorta_sum(12, -3), 9  )
tester(sorta_sum(-3, 12), 9 )
tester(sorta_sum(4, 5), 9)
tester(sorta_sum(4, 6), 20)
tester(sorta_sum(14, 7), 21)
tester(sorta_sum(14, 6), 20)
