"""Test code for TIL Python programming jupyter notebook Lab 2 - Fundamentals I"""
import re
import pytest
from testbook import testbook

@pytest.fixture(scope='module')
def tb():
    with testbook('lab2_2025.ipynb', execute=True) as tb:
        yield tb

# Q1
def test_string_operations(tb):
    assert callable(tb.ref("string_operations"))

def test_string_operations_1(tb):
    assert tb.ref("string_operations")(1) == 3

def test_string_operations_2(tb):
    assert tb.ref("string_operations")(2) == 72

def test_string_operations_3(tb):
    assert tb.ref("string_operations")(3) == 78

def test_string_operations_4(tb):
    assert tb.ref("string_operations")(4) == True

def test_string_operations_5(tb):
    assert tb.ref("string_operations")(5) == 'in computer programming,  a string is traditionally  a sequence of characters.  '

def test_string_operations_6(tb):
    assert tb.ref("string_operations")(6) == ['In computer programming', '  a string is traditionally  a sequence of characters.  ']

def test_string_operations_7(tb):
    assert tb.ref("string_operations")(7) == 'In computer programming, a string is traditionally a sequence of characters. '

def test_string_operations_8(tb):
    assert tb.ref("string_operations")(8) == 'In computer programming,  a string is  a sequence of characters.  '


# Q2
def test_string_formatting(tb):
    assert callable(tb.ref("string_formatting"))

def test_string_formatting_1(tb):
    assert tb.ref("string_formatting")(1) == '2'

def test_string_formatting_2(tb):
    assert tb.ref("string_formatting")(2) == '1.7'

def test_string_formatting_3(tb):
    assert tb.ref("string_formatting")(3) == '1.73'

def test_string_formatting_4(tb):
    assert tb.ref("string_formatting")(4) == '   1.73'

def test_string_formatting_5(tb):
    assert tb.ref("string_formatting")(5) == '0001.73'

def test_string_formatting_6(tb):
    assert tb.ref("string_formatting")(6) == '+1.73'

def test_string_formatting_7(tb):
    assert tb.ref("string_formatting")(7) == '+001.73'

def test_string_formatting_8(tb):
    assert tb.ref("string_formatting")(8) == '1.73e+00'


# Q3
def test_regexp_string(tb):
    regexp_string = tb.ref("regexp_string")
    assert callable(regexp_string)
    assert type(regexp_string()) == str

def test_regexp_string_1(tb):
    assert re.search(tb.ref("regexp_string")(), '0001,2345').span() == (0, 9)

def test_regexp_string_2(tb):
    assert re.search(tb.ref("regexp_string")(), '1,2345').span() == (0, 6)

def test_regexp_string_3(tb):
    assert re.search(tb.ref("regexp_string")(), '1,23').span() == (0, 4)

def test_regexp_string_4(tb):
    assert re.search(tb.ref("regexp_string")(), ',2345').span() == (0, 5)

def test_regexp_string_5(tb):
    assert re.search(tb.ref("regexp_string")(), '1,').span() == (0, 2)

def test_regexp_string_6(tb):
    assert re.search(tb.ref("regexp_string")(), '001.2345').span() == (0, 8)

def test_regexp_string_7(tb):
    assert re.search(tb.ref("regexp_string")(), '1.2345').span() == (0, 6)

def test_regexp_string_8(tb):
    assert re.search(tb.ref("regexp_string")(), '1.23').span() == (0, 4)

def test_regexp_string_9(tb):
    assert re.search(tb.ref("regexp_string")(), '.2345').span() == (0, 5)

def test_regexp_string_10(tb):
    assert re.search(tb.ref("regexp_string")(), '1.').span() == (0, 2)

def test_regexp_string_11(tb):
    assert re.search(tb.ref("regexp_string")(), '1') == None

def test_regexp_string_12(tb):
    assert re.search(tb.ref("regexp_string")(), 'thisisnotanumber') == None


# Q4
def test_count_character(tb):
    assert callable(tb.ref("count_character"))

def test_count_character_a(tb):
    assert tb.ref("count_character")('a') == 3

def test_count_character_b(tb):
    assert tb.ref("count_character")('b') == 0

def test_count_character_c(tb):
    assert tb.ref("count_character")('c') == 1

def test_count_character_d(tb):
    assert tb.ref("count_character")('d') == 2

def test_count_character_e(tb):
    assert tb.ref("count_character")('e') == 12

def test_count_character_f(tb):
    assert tb.ref("count_character")('f') == 3

def test_count_character_g(tb):
    assert tb.ref("count_character")('g') == 2

def test_count_character_h(tb):
    assert tb.ref("count_character")('h') == 8

def test_count_character_i(tb):
    assert tb.ref("count_character")('i') == 3

def test_count_character_j(tb):
    assert tb.ref("count_character")('j') == 2

def test_count_character_k(tb):
    assert tb.ref("count_character")('k') == 0

def test_count_character_l(tb):
    assert tb.ref("count_character")('l') == 1

def test_count_character_m(tb):
    assert tb.ref("count_character")('m') == 3

def test_count_character_n(tb):
    assert tb.ref("count_character")('n') == 8

def test_count_character_o(tb):
    assert tb.ref("count_character")('o') == 12

def test_count_character_p(tb):
    assert tb.ref("count_character")('p') == 1

def test_count_character_q(tb):
    assert tb.ref("count_character")('q') == 0

def test_count_character_r(tb):
    assert tb.ref("count_character")('r') == 4

def test_count_character_s(tb):
    assert tb.ref("count_character")('s') == 5

def test_count_character_t(tb):
    assert tb.ref("count_character")('t') == 6

def test_count_character_u(tb):
    assert tb.ref("count_character")('u') == 1

def test_count_character_v(tb):
    assert tb.ref("count_character")('v') == 3

def test_count_character_w(tb):
    assert tb.ref("count_character")('w') == 0

def test_count_character_x(tb):
    assert tb.ref("count_character")('x') == 0

def test_count_character_y(tb):
    assert tb.ref("count_character")('y') == 2

def test_count_character_z(tb):
    assert tb.ref("count_character")('z') == 0


# Q5
def test_good_day(tb):
    assert callable(tb.ref("good_day"))

def test_good_day_1(tb):
    assert tb.ref("good_day")(1, 2) == 'Good night, the time is 01:02'

def test_good_day_2(tb):
    assert tb.ref("good_day")(3, 4) == 'Good night, the time is 03:04'

def test_good_day_3(tb):
    assert tb.ref("good_day")(5, 6) == 'Good night, the time is 05:06'

def test_good_day_4(tb):
    assert tb.ref("good_day")(7, 8) == 'Good morning, the time is 07:08'

def test_good_day_5(tb):
    assert tb.ref("good_day")(9, 10) == 'Good morning, the time is 09:10'

def test_good_day_6(tb):
    assert tb.ref("good_day")(10, 11) == 'Good morning, the time is 10:11'

def test_good_day_7(tb):
    assert tb.ref("good_day")(12, 13) == 'Good afternoon, the time is 12:13'

def test_good_day_8(tb):
    assert tb.ref("good_day")(14, 15) == 'Good afternoon, the time is 14:15'

def test_good_day_9(tb):
    assert tb.ref("good_day")(16, 17) == 'Good afternoon, the time is 16:17'

def test_good_day_10(tb):
    assert tb.ref("good_day")(18, 19) == 'Good evening, the time is 18:19'

def test_good_day_11(tb):
    assert tb.ref("good_day")(20, 21) == 'Good evening, the time is 20:21'

def test_good_day_12(tb):
    assert tb.ref("good_day")(22, 23) == 'Good evening, the time is 22:23'

def test_good_day_13(tb):
    assert tb.ref("good_day")(23, 24) == 'Good evening, the time is 23:24'