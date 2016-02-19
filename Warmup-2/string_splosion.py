# Given a non-empty string like "Code" return a string like "CCoCodCode". 

from test import Tester

def string_splosion(str):
    result = '' 
    # this will be the range to slice to   
    j = 1
    for i in range(len(str)):
        result += str[:j]
        j+=1
    return result


Tester(string_splosion('Code'), 'CCoCodCode')   
Tester(string_splosion('abc'), 'aababc')
Tester(string_splosion('ab'), 'aab') 
Tester(string_splosion('x'), 'x')    
Tester(string_splosion('fade'), 'ffafadfade')   
Tester(string_splosion('There'), 'TThTheTherThere') 
Tester(string_splosion('Kitten'), 'KKiKitKittKitteKitten')    
Tester(string_splosion('Bye'), 'BByBye') 
Tester(string_splosion('Good'), 'GGoGooGood')    
Tester(string_splosion('Bad'), 'BBaBad')
