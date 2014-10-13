import pytest

from ccrypt.caesar import Caesar


c = Caesar()


def test_encrypt_shift_a_d():
    assert c.encrypt_shift('a') == 'd'

def test_encrypt_shift_b_e():
    assert c.encrypt_shift('b') == 'e'

def test_encrypt_shift_x_a():
    assert c.encrypt_shift('x') == 'a'

def test_caesar_ma_pd():
    assert c.encrypt('ma') == 'pd'

def test_caesar_pe_sh():
    assert c.encrypt('pe') == 'sh'

def test_freak_message():
    assert c.encrypt('dojoiesb') == 'grmrlhve'
