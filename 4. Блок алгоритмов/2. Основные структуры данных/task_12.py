import sys

sys.setrecursionlimit(1000000000)


def Fibonacci(n, k):
    if n in [0, 1]:
        return 1
    a = 1
    b = 1
    coef = 10**k
    for _ in range(1, n):
        result = (a + b) % coef
        a, b = b, result
    return result


def main():
    n, k = input().rstrip().split()
    print(Fibonacci(int(n), int(k)), end='')


if __name__ == '__main__':
    main()
