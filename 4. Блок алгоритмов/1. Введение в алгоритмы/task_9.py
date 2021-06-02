import math


def is_quarter(n):
    result = str(math.log(n, 4))
    rest = result.split('.')[1]
    if rest == '0':
        return True
    return False


def main():
    n = int(input())
    result = is_quarter(n)
    print(result, end='')


if __name__ == '__main__':
    main()
