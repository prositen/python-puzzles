__author__ = 'anna'


def sum_even_fib(n):
    """
    Every third fibonacci number is even, which leads to the formula
    E(n) = 4E(n-1) + E(n-2)
    """
    a,b = 0, 2
    fib_sum = 0
    while b < n:
        fib_sum += b
        a, b = b, 4*b +a
    return fib_sum


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(sum_even_fib(n))

if __name__ == '__main__':
    main()
