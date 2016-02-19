# Given a string, return a new string
# made of every other char starting
# with the first, so "Hello" yields "Hlo". 

from test import Tester

def string_bits(str):
    newstr = ''    
    i = 0
    length = len(str)
    while i < length:
        if i%2 == 0:
            newstr += str[i]
        i+=1
    return newstr
            

Tester(string_bits('Hello'), 'Hlo')    
Tester(string_bits('Hi'), 'H')    
Tester(string_bits('Heeololeo'), 'Hello')
Tester(string_bits('HiHiHi'), 'HHH')
Tester(string_bits(''), '')
Tester(string_bits('Greetings'), 'Getns')
Tester(string_bits('Chocoate'), 'Coot')
Tester(string_bits('pi'), 'p')
Tester(string_bits('Hello Kitten'), 'HloKte')
Tester(string_bits('hxaxpxpxy'), 'happy')

# the example solution uses a for loop instead of a while loop. This is better because no while loop.
def string_bits(str):
  result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
