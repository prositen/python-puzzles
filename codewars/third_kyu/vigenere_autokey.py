import operator


class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = abc
        self.first_char = ord(self.abc[0])

    def encode(self, text, encode=True):
        key = self.key
        encoded = []
        pos = 0
        op = operator.add if encode else operator.sub
        for c in text:
            if c in self.abc:
                index_key = self.abc.find(key[pos])
                index_char = self.abc.find(c)
                encoded_char = self.abc[op(index_char, index_key) % len(self.abc)]
                encoded.append(encoded_char)
                pos += 1
                key += c if encode else encoded_char
            else:
                encoded.append(c)
        return "".join(encoded)

    def decode(self, text):
        return self.encode(text, encode=False)
