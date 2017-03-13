import unittest

from codewars import third_kyu


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
            self.assertEquals(test[1], result)
            self.assertEquals(test[0], third_kyu.from_base_64(result))
