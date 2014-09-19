import pytest

from ccrypt import caesar


def test_shift_a_d():
    assert caesar.shift('a') == 'd'

def test_shift_b_e():
    assert caesar.shift('b') == 'e'

def test_shift_x__():
    assert caesar.shift('x') == ' '

def test_shift_y_a():
    assert caesar.shift('x') == ' '

def test_caesar_ma_pd():
    assert caesar.caesar('ma') == 'pd'

def test_caesar_pe_sh():
    assert caesar.caesar('pe') == 'sh'

def test_freak_message():
    assert caesar.caesar('dojo iesb') == 'grmrclhve'
