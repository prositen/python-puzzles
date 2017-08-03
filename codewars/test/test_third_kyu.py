import unittest

from codewars import third_kyu
from codewars.third_kyu.vigenere_autokey import VigenereAutokeyCipher


class Test3kyu(unittest.TestCase):
    def test_to_base_64(self):
        tests = [["this is a string!!", "dGhpcyBpcyBhIHN0cmluZyEh"],
                 ["this is a test!", "dGhpcyBpcyBhIHRlc3Qh"],
                 ["now is the time for all good men to come to the aid of their country.",
                  "bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"],
                 ["1234567890  ", "MTIzNDU2Nzg5MCAg"],
                 ["ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"],
                 ["the quick brown fox jumps over the white fence. ",
                  "dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"],
                 ["dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4",
                  "ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"],
                 ["VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna", "VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"],
                 ["TVRJek5EVTJOemc1TUNBZyAg", "VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"],
                 [" LN7Fq4OsoK", "IExON0ZxNE9zb0s"]]

        for test in tests:
            result = third_kyu.to_base_64(test[0])
            self.assertEqual(test[1], result)
            self.assertEqual(test[0], third_kyu.from_base_64(result))

    def test_vigenere_autokey_site_example(self):
        key = 'PASSWORD'
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        c = VigenereAutokeyCipher(key, abc)
        self.assertEqual('PASSWORDPASSWORDPASSWORD', c.encode('AAAAAAAAPASSWORDAAAAAAAA'))
        self.assertEqual('AAAAAAAAPASSWORDAAAAAAAA', c.decode('PASSWORDPASSWORDPASSWORD'))

    def test_vigenere_autokey_encode(self):
        key2 = 'password'
        abc2 = 'abcdefghijklmnopqrstuvwxyz'
        c2 = VigenereAutokeyCipher(key2, abc2)
        self.assertEqual('rovwsoiv', c2.encode('codewars'))
        self.assertEqual('pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib',
                         c2.encode('amazingly few discotheques provide jukeboxes'))
    def test_vigenere_autokey_decode(self):
        key = 'password'
        abc = 'abcdefghijklmnopqrstuvwxyz'
        c = VigenereAutokeyCipher(key, abc)

        self.assertEqual('waffles', c.decode('laxxhsj'))
        self.assertEqual('amazingly few discotheques provide jukeboxes',
                         c.decode('pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib'))

    def test_vigenere_autokey_untouched(self):
        key = 'password'
        abc = 'abcdefghijklmnopqrstuvxyz'
        c = VigenereAutokeyCipher(key, abc)
        self.assertEqual('CODEWARS', c.encode('CODEWARS'))