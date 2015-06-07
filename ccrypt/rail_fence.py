from itertools import cycle

class RailFence(object):

    def __init__(self, alphabet, rails):
        self.alphabet = alphabet.lower()
        if rails > len(alphabet):
            self.rails = rails % len(alphabet)
        else:
            self.rails = rails

    def offset(self, even, rail):
        if rail == 0 or rail == self.rails - 1:
            return (self.rails - 1) * 2

        if even:
            return rail * 2
        else:
            return (self.rails - rail - 1) * 2


    def decrypt(self, cryptogram):
        matrix = [[' ' for col in range(len(cryptogram))]
                  for i in range(self.rails)]
        read = 0

        for rail in range(self.rails):
            position = self.offset(True, rail)
            even_rail = False

            if rail == 0:
                position = 0
            else:
                position = int(position/2)

            while position < len(cryptogram):
                if read == len(cryptogram):
                    break

                matrix[rail][position] = cryptogram[read]
                read += 1
                position += self.offset(even_rail, rail)
                even_rail = not even_rail

        decoded = ''

        for x in range(len(cryptogram)):
            for y in range(self.rails):
                if matrix[y][x] != " ":
                    decoded += matrix[y][x]

        return decoded

    def encrypt(self, message):

        read = 0
        cryptogram = ''
        matrix = ['' for rail in range(self.rails)]
        rails = range(self.rails - 1) + range(self.rails - 1, 0, -1)
        for rail in cycle(rails):
            if len(message) <= read:
                break
            matrix[rail] += message[read]
            read += 1
        for line in matrix:
            cryptogram += line

        return cryptogram




