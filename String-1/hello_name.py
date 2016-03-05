from test import Tester

def hello_name(name):
    return "Hello %s!" % name

Tester(hello_name('Bob'), 'Hello Bob!')
Tester(hello_name('Alice'), 'Hello Alice!')
Tester(hello_name('X'), 'Hello X!')
Tester(hello_name('Dolly'), 'Hello Dolly!')
Tester(hello_name('Alpha'), 'Hello Alpha!')
Tester(hello_name('Omega'), 'Hello Omega!')
Tester(hello_name('Goodbye'), 'Hello Goodbye!')
Tester(hello_name('ho ho ho'), 'Hello ho ho ho!')
Tester(hello_name('xyz!'), 'Hello xyz!!')
Tester(hello_name('Hello'), 'Hello Hello!')
