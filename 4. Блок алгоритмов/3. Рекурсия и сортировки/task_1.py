def print_brackets(n, start, stop, prefix):
    if len(prefix) == 2 * n and start == stop:
        print(prefix)
    else:
        if start >= stop and start <= n:
            print_brackets(n, start + 1, stop, prefix + '(')
        if stop < start:
            print_brackets(n, start, stop + 1, prefix + ')')


def main():
    n = int(input())
    print_brackets(n, 0, 0, '')


if __name__ == '__main__':
    main()
