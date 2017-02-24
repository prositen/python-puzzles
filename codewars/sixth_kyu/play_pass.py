from string import ascii_lowercase, digits


def play_pass(s, n):
    """
    https://www.codewars.com/kata/playing-with-passphrases
    :param s: Passphrase
    :param n: Number of steps to rotate each letter
    :return: "Encrypted" passphrase
    """
    n %= 26
    translate = str.maketrans(ascii_lowercase + digits,
                              ascii_lowercase[n:] + ascii_lowercase[:n] + digits[::-1])
    s = s.lower().translate(translate)
    output = [c if (i % 2) else c.upper() for i, c in enumerate(s)]
    return "".join(output[::-1])
