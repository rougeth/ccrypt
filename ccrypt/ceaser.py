from ccrypt.utils import k27 as alphabet


def shift(char):
    index = alphabet.index(char)
    index = (index + 3)  % 27
    return alphabet[index]

def ceaser(message):
    cryptogram = ''
    for char in message:
        cryptogram = cryptogram + shift(char)

    return cryptogram
