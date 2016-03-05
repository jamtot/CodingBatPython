def Tester(result, expected):
    if result==expected:
        print "OK."
    else:
        print Incorrect, "%r != %r" % (result, expected)
