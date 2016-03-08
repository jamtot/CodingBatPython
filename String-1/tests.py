from nose.tools import *
from hello_name import *
from make_abba import *
from make_tags import *
from make_out_word import *
from extra_end import *
from first_two import *
from first_half import *
from without_end import *
from combo_string import *
from non_start import *
from left2 import *

def test_hello_name():
    assert_equal(hello_name('Bob'),'Hello Bob!')
    assert_equal(hello_name('Alice'), 'Hello Alice!')
    assert_equal(hello_name('X'), 'Hello X!')
    assert_equal(hello_name('Dolly'), 'Hello Dolly!')
    assert_equal(hello_name('Alpha'), 'Hello Alpha!')
    assert_equal(hello_name('Omega'), 'Hello Omega!')
    assert_equal(hello_name('Goodbye'), 'Hello Goodbye!')
    assert_equal(hello_name('ho ho ho'), 'Hello ho ho ho!')
    assert_equal(hello_name('xyz!'), 'Hello xyz!!')
    assert_equal(hello_name('Hello'), 'Hello Hello!')

def test_make_abba():
    assert_equal(make_abba('Hi', 'Bye'), 'HiByeByeHi')
    assert_equal(make_abba('Yo', 'Alice'), 'YoAliceAliceYo')
    assert_equal(make_abba('What', 'Up'), 'WhatUpUpWhat')
    assert_equal(make_abba('aaa', 'bbb'), 'aaabbbbbbaaa')    
    assert_equal(make_abba('x', 'y'), 'xyyx')
    assert_equal(make_abba('x', ''), 'xx')
    assert_equal(make_abba('', 'y'), 'yy')
    assert_equal(make_abba('Bo', 'Ya'), 'BoYaYaBo') 
    assert_equal(make_abba('Ya', 'Ya'), 'YaYaYaYa')

def test_make_tags():
    assert_equal(make_tags('i', 'Yay'), '<i>Yay</i>')
    assert_equal(make_tags('i', 'Hello'), '<i>Hello</i>')
    assert_equal(make_tags('cite', 'Yay'), '<cite>Yay</cite>')
    assert_equal(make_tags('address', 'here'), '<address>here</address>') 
    assert_equal(make_tags('body', 'Heart'), '<body>Heart</body>')
    assert_equal(make_tags('i', 'i'), '<i>i</i>')   
    assert_equal(make_tags('i', ''), '<i></i>')

def test_make_out_word():
    assert_equal(make_out_word('<<>>', 'Yay'), '<<Yay>>')
    assert_equal(make_out_word('<<>>', 'WooHoo'), '<<WooHoo>>')
    assert_equal(make_out_word('[[]]', 'word'), '[[word]]')
    assert_equal(make_out_word('HHoo', 'Hello'), 'HHHellooo')
    assert_equal(make_out_word('abyz', 'YAY'), 'abYAYyz')
    
def test_extra_end():
    assert_equal(extra_end('Hello'), 'lololo')
    assert_equal(extra_end('ab'), 'ababab')
    assert_equal(extra_end('Hi'), 'HiHiHi')
    assert_equal(extra_end('Candy'), 'dydydy')    
    assert_equal(extra_end('Code'), 'dedede')

def test_first_two():
    assert_equal(first_two('Hello'), 'He')
    assert_equal(first_two('abcdefg'), 'ab')
    assert_equal(first_two('ab'), 'ab')
    assert_equal(first_two('a'), 'a')
    assert_equal(first_two(''), '')
    assert_equal(first_two('Kitten'), 'Ki')
    assert_equal(first_two('hi'), 'hi')
    assert_equal(first_two('hiya'), 'hi')

def test_first_half():
    assert_equal(first_half('WooHoo'), 'Woo')
    assert_equal(first_half('HelloThere'), 'Hello')
    assert_equal(first_half('abcdef'), 'abc')
    assert_equal(first_half('ab'), 'a')
    assert_equal(first_half(''), '')   
    assert_equal(first_half('0123456789'), '01234')
    assert_equal(first_half('kitten'), 'kit')

def test_without_end():
    assert_equal(without_end('Hello'), 'ell')
    assert_equal(without_end('python'), 'ytho')
    assert_equal(without_end('coding'), 'odin')
    assert_equal(without_end('coding'), 'odin')
    assert_equal(without_end('code'), 'od')
    assert_equal(without_end('ab'), '')
    assert_equal(without_end('Chocolate!'), 'hocolate')
    assert_equal(without_end('kitten'), 'itte')
    assert_equal(without_end('woohoo'), 'ooho')

def test_combo_string():
    assert_equal(combo_string('Hello', 'hi'), 'hiHellohi')
    assert_equal(combo_string('hi', 'Hello'), 'hiHellohi')
    assert_equal(combo_string('aaa', 'b'), 'baaab')
    assert_equal(combo_string('b', 'aaa'), 'baaab')
    assert_equal(combo_string('aaa', ''), 'aaa')
    assert_equal(combo_string('', 'bb'), 'bb')
    assert_equal(combo_string('aaa', '1234'), 'aaa1234aaa')
    assert_equal(combo_string('aaa', 'bb'), 'bbaaabb')
    assert_equal(combo_string('a', 'bb'), 'abba')
    assert_equal(combo_string('bb', 'a'), 'abba')
    assert_equal(combo_string('xyz', 'ab'), 'abxyzab')

def test_non_start():
    assert_equal(non_start('Hello', 'There'), 'ellohere')
    assert_equal(non_start('python', 'code'), 'ythonode')
    assert_equal(non_start('shotl', 'java'), 'hotlava')
    assert_equal(non_start('ab', 'xy'), 'by')
    assert_equal(non_start('ab', 'x'), 'b')
    assert_equal(non_start('x', 'ac'), 'c')
    assert_equal(non_start('a', 'x'), '')
    assert_equal(non_start('kit', 'kat'), 'itat')   
    assert_equal(non_start('mart', 'dart'), 'artart')

def test_left2():
    assert_equal(left2('Hello'), 'lloHe')
    assert_equal(left2('python'), 'thonpy')
    assert_equal(left2('Hi'), 'Hi')
    assert_equal(left2('code'), 'deco')
    assert_equal(left2('cat'), 'tca')
    assert_equal(left2('12345'), '34512')    
    assert_equal(left2('Chocolate'), 'ocolateCh')    
    assert_equal(left2('bricks'), 'icksbr')
