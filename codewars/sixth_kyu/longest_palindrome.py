def longest_palindrome(s):
    ls = len(s)
    for l in range(ls, -1, -1):
        for n in range(ls - l):
            slice = s[n:l + n + 1]
            if slice[::-1] == slice:
                return len(slice)
    return 0