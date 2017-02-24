from codewars.utils import is_palindrome


def palindrome_chain_length(n, depth=0):
    if is_palindrome(str(n)):
        return depth
    else:
        s = str(n)
        next_number = n + int(s[::-1], 10)
        return palindrome_chain_length(next_number, depth + 1)
