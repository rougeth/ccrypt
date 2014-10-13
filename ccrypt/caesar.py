from ccrypt.simple_substitution import SimpleSubstitution
from ccrypt.utils import k27 as alphabet


class Caesar(SimpleSubstitution):

    def __init__(self):
        super().__init__(alphabet, 3)
