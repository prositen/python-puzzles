import string


class CaesarCipher(object):
    def __init__(self, shift):
        self.encode_table = str.maketrans(string.ascii_uppercase,
                                          string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift])
        self.decode_table = str.maketrans(string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift],
                                          string.ascii_uppercase)

    def encode(self, s):
        return s.upper().translate(self.encode_table)

    def decode(self, s):
        return s.upper().translate(self.decode_table)
