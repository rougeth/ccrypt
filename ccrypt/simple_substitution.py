
class SimpleSubstitution(object):

    def __init__(self, alphabet, key):
        self.alphabet = alphabet.lower()
        if key > len(alphabet):
            self.key = key % len(alphabet)
        else:
            self.key = key

    def encrypt_shift(self, char):
        index = self.alphabet.index(char)
        index = (index + self.key) % len(self.alphabet)
        return self.alphabet[index]

    def decrypt_shift(self, char):
        index = self.alphabet.index(char)
        index = (index - self.key) % len(self.alphabet)
        return self.alphabet[index]

    def encrypt(self, message):
        cryptogram = ''
        for char in message.lower():
            cryptogram = cryptogram + self.encrypt_shift(char)
        return cryptogram

    def decrypt(self, message):
        cryptogram = ''
        for char in message.lower():
            cryptogram = cryptogram + self.decrypt_shift(char)
        return cryptogram
