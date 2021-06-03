def Fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return Fibonacci(n-2) + Fibonacci(n-1)


def main():
    n = int(input().rstrip())
    print(Fibonacci(n), end='')


if __name__ == '__main__':
    main()
