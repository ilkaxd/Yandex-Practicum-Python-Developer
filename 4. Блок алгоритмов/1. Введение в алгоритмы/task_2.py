def is_even(a):
    if a % 2 == 0:
        return True
    return False


def same_parity(a, b, c):
    resul = is_even(a) + is_even(b) + is_even(c)
    if resul == 3 or resul == 0:
        return 'WIN'
    return 'FAIL'


def main():
    line = input().rstrip()
    a, b, c = [int(t) for t in line.split()]

    result = same_parity(a, b, c)
    print(result, end='')


if __name__ == '__main__':
    main()
