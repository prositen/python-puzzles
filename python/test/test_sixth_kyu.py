import unittest
from python import sixth_kyu


class Test6Kyu(unittest.TestCase):
    def test_play_pass(self):
        self.assertEquals("!!!vPz fWpM J", sixth_kyu.play_pass("I LOVE YOU!!!", 1))
        self.assertEquals("4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO",
                          sixth_kyu.play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2))

    def test_letter_pattern(self):
        self.assertEquals('*a*',
                          sixth_kyu.letter_pattern(['war', 'rad', 'dad']))
        self.assertEquals('*******',
                          sixth_kyu.letter_pattern(['general', 'admiral', 'piglets', 'secrets']))
        self.assertEquals('family',
                          sixth_kyu.letter_pattern(['family']))

    def test_balance(self):
        self.assertTrue(sixth_kyu.balance(["a", "a", "a", "a", "a", "b", "b", "b"],
                                          ["c", "c", "c", "c", "c", "d", "d", "d"]))

        self.assertFalse(sixth_kyu.balance(["a", "a"], ["c"]))

        self.assertTrue(sixth_kyu.balance(["a", "b", "c", "d", "e", "f", "g", "g"],
                                          ["h", "h", "i", "j", "k", "l", "m", "n"]))

        self.assertTrue(sixth_kyu.balance(["a"], ["c"]))

        self.assertFalse(sixth_kyu.balance(["a", "b", "c", "d", "e", "f", "g", "g"],
                                           ["h", "h", "i", "j", "k", "l", "m", "m"]))

    def test_alphabet_position(self):
        from random import randint
        self.assertEquals("20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
                          sixth_kyu.alphabet_position("The sunset sets at twelve o' clock."))
        self.assertEquals("20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20",
                          sixth_kyu.alphabet_position("The narwhal bacons at midnight."))
        number_test = ""
        for item in range(10):
            number_test += str(randint(1, 9))
        self.assertEquals("", sixth_kyu.alphabet_position(number_test))

    def test_longest_palindrome(self):
        self.assertEquals(9, sixth_kyu.longest_palindrome("baablkj12345432133d"))
        self.assertEquals(1, sixth_kyu.longest_palindrome("a"))
        self.assertEquals(2, sixth_kyu.longest_palindrome("aa"))
        self.assertEquals(2, sixth_kyu.longest_palindrome("baa"))
        self.assertEquals(2, sixth_kyu.longest_palindrome("aab"))
        self.assertEquals(1, sixth_kyu.longest_palindrome("abcdefghba"))
        self.assertEquals(9, sixth_kyu.longest_palindrome("baablkj12345432133d"))

    def test_namelist(self):
        self.assertEquals('Bart, Lisa, Maggie, Homer & Marge',
                          sixth_kyu.namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'},
                                              {'name': 'Marge'}]),
                          "Must work with many names")
        self.assertEquals('Bart, Lisa & Maggie',
                          sixth_kyu.namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]),
                          "Must work with many names")

        self.assertEquals('Bart & Lisa', sixth_kyu.namelist([{'name': 'Bart'}, {'name': 'Lisa'}]),
                          "Must work with two names")

        self.assertEquals('Bart', sixth_kyu.namelist([{'name': 'Bart'}]), "Wrong output for a single name")

        self.assertEquals('', sixth_kyu.namelist([]), "Must work with no names")

    def test_comp(self):
        self.assertTrue(sixth_kyu.comp([121, 144, 19, 161, 19, 144, 19, 11],
                                       [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144,
                                        19 * 19]))

        self.assertFalse(sixth_kyu.comp([121, 144, 19, 161, 19, 144, 19, 11],
                                        [132, 14641, 20736, 361, 25921, 361, 20736, 361]))

        self.assertFalse(sixth_kyu.comp([121, 144, 19, 161, 19, 144, 19, 11],
                                        [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
                                        ))
