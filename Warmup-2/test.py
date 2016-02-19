class Tester:
    """A simple testing class."""
    
    def __init__(self, actual, expected):
        self.actual = actual
        self.expected = expected
        if actual == expected:
            print "Correct."
        else:
            print "Incorrect."
