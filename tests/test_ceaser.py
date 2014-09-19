import pytest

from ccrypt import ceaser


def test_shift_a_d():
    assert ceaser.shift('a') == 'd'

def test_shift_b_e():
    assert ceaser.shift('b') == 'e'

def test_shift_x__():
    assert ceaser.shift('x') == ' '

def test_shift_y_a():
    assert ceaser.shift('x') == ' '

def test_ceaser_ma_pd():
    assert ceaser.ceaser('ma') == 'pd'

def test_ceaser_pe_sh():
    assert ceaser.ceaser('pe') == 'sh'

def test_freak_message():
    assert ceaser.ceaser('dojo iesb') == 'grmrclhve'
