from nose.tools import *
from double_char import *
from count_hi import *
from cat_dog import *
from count_code import *
from end_other import *
from xyz_there import *

def test_double_char():
    assert_equal(double_char('The'), 'TThhee')
    assert_equal(double_char('AAbb'), 'AAAAbbbb')
    assert_equal(double_char('Hi-There'), 'HHii--TThheerree')
    assert_equal(double_char('Word!'), 'WWoorrdd!!')
    assert_equal(double_char('!!'), '!!!!')
    assert_equal(double_char(''), '')
    assert_equal(double_char('a'), 'aa')
    assert_equal(double_char('.'), '..')
    assert_equal(double_char('aa'), 'aaaa')

def test_count_hi():
    assert_equal(count_hi('abc hi ho'), 1)
    assert_equal(count_hi('ABChi hi'), 2)
    assert_equal(count_hi('hihi'), 2)
    assert_equal(count_hi('hiHIhi'), 2)
    assert_equal(count_hi(''), 0)
    assert_equal(count_hi('h'), 0)
    assert_equal(count_hi('hi'), 1)
    assert_equal(count_hi('Hi is no HI on ahI'), 0)
    assert_equal(count_hi('hiho not HOHIhi'), 2)

def test_cat_dog():
    assert_equal(cat_dog('catdog'), True)
    assert_equal(cat_dog('catcat'), False)
    assert_equal(cat_dog('1cat1cadodog'), True)
    assert_equal(cat_dog('catxxdogxxxdog'), False)
    assert_equal(cat_dog('catxdogxdogxcat'), True)
    assert_equal(cat_dog('catxdogxdogxca'), False)
    assert_equal(cat_dog('dogdogcat'), False)
    assert_equal(cat_dog('dogogcat'), True)
    assert_equal(cat_dog('dog'), False)
    assert_equal(cat_dog('cat'), False)
    assert_equal(cat_dog('ca'), True)
    assert_equal(cat_dog('c'), True)
    assert_equal(cat_dog(''), True)

def test_count_code():
    assert_equal(count_code('aaacodebbb'), 1)
    assert_equal(count_code('codexxcode'), 2)
    assert_equal(count_code('cozexxcope'), 2)
    assert_equal(count_code('cozfxxcope'), 1)
    assert_equal(count_code('xxcozeyycop'), 1)
    assert_equal(count_code('cozcop'), 0)
    assert_equal(count_code('abcxyz'), 0)
    assert_equal(count_code('code'), 1)
    assert_equal(count_code('ode'), 0)
    assert_equal(count_code('c'), 0)
    assert_equal(count_code(''), 0)
    assert_equal(count_code('AAcodeBBcoleCCccoreDD'), 3)
    assert_equal(count_code('AAcodeBBcoleCCccorfDD'), 2)
    assert_equal(count_code('coAcodeBcoleccoreDD'), 3)

def test_end_other():
    assert_equal(end_other('Hiabc', 'abc'), True)
    assert_equal(end_other('AbC', 'HiaBc'), True)
    assert_equal(end_other('abc', 'abXabc'), True)
    assert_equal(end_other('Hiabc', 'abcd'), False)
    assert_equal(end_other('Hiabc', 'bc'), True)
    assert_equal(end_other('Hiabcx', 'bc'), False)
    assert_equal(end_other('abc', 'abc'), True)
    assert_equal(end_other('xyz', '12xyz'), True)
    assert_equal(end_other('yz', '12xz'), False)
    assert_equal(end_other('Z', '12xz'), True)
    assert_equal(end_other('12', '12'), True)
    assert_equal(end_other('abcXYZ', 'abcDEF'), False)
    assert_equal(end_other('ab', 'ab12'), False)
    assert_equal(end_other('ab', '12ab'), True)

def test_xyz_there():
    assert_equal(xyz_there('abcxyz'), True)
    assert_equal(xyz_there('abc.xyz'), False)
    assert_equal(xyz_there('xyz.abc'), True)
    assert_equal(xyz_there('abcxy'), False)
    assert_equal(xyz_there('xyz'), True)
    assert_equal(xyz_there('xy'), False)
    assert_equal(xyz_there('x'), False)
    assert_equal(xyz_there(''), False)
    assert_equal(xyz_there('abc.xyzxyz'), True)
    assert_equal(xyz_there('abc.xxyz'), True)
    assert_equal(xyz_there('.xyz'), False)
    assert_equal(xyz_there('12.xyz'), False)
    assert_equal(xyz_there('12xyz'), True)
    assert_equal(xyz_there('1.xyz.xyz2.xyz'), False)
