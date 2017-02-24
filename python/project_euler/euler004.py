__author__ = 'anna'
"""
A palindromic number reads the same both ways. The smallest 6 digit palindrome made from the product of two 3-digit
numbers is 101101 = 143 * 707.

Find the largest palindrome made from the product of two 3-digit numbers which is less than M.
"""


def find_palindrome(n):
    """
    Let's bruteforce
    """
    max_found = 0
    for a in range(999, 99, -1):
        for b in range(999, 99, -1):
            prod = a * b
            if n > prod > max_found:
                prod_str = str(a * b)
                if prod_str[:3] == prod_str[-1:-4:-1]:
                    max_found = prod
                    break
    return max_found


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(find_palindrome(n))

if __name__ == '__main__':
    main()