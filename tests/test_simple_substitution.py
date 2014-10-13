import string

from ccrypt.simple_substitution import SimpleSubstitution
from ccrypt.utils import k27


params = {
    'alphabet': k27,
    'key': 3
}


def test_params():
    s = SimpleSubstitution(k27, 28)
    assert s.key == 1

def test_key_bigger_than_alphabet():
    s = SimpleSubstitution(**params)
    assert s.alphabet == params['alphabet']
    assert s.key == params['key']

def test_encrypt_shift():
    s = SimpleSubstitution(**params)
    assert s.encrypt_shift('a') == 'd'

def test_decrypt_shift():
    s = SimpleSubstitution(**params)
    assert s.decrypt_shift('d') == 'a'

def test_encrypt_message():
    s = SimpleSubstitution(**params)
    cryptogram = s.encrypt('Hello World')
    assert cryptogram == 'khoorczruog'
