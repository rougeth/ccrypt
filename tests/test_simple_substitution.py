import string

from ccrypt.simple_substitution import SimpleSubstitution
from ccrypt.utils import k27


params = {
    'alphabet': k27,
    'key': 3
}

def test_ss_params():
    s = SimpleSubstitution(**params)
    assert s.alphabet == params['alphabet']
    assert s.key == params['key']

def test_ss_encrypt_shift():
    s = SimpleSubstitution(**params)
    assert s.encrypt_shift('a') == 'd'

def test_ss_decrypt_shift():
    s = SimpleSubstitution(**params)
    assert s.decrypt_shift('d') == 'a'

def test_ss_encrypt_message():
    s = SimpleSubstitution(**params)
    cryptogram = s.encrypt('Hello World')
    assert cryptogram == 'khoorczruog'
