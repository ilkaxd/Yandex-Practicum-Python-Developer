import sys

sys.setrecursionlimit(10000000)


def sort_color(s, dictionary):
    if len(s) == 0:
        return ' '.join(
            ['0'] * dictionary[0] +
            ['1'] * dictionary[1] +
            ['2'] * dictionary[2]
        )
    dictionary[s[0]] += 1
    return sort_color(s[1:], dictionary)


def main():
    _ = int(input())
    s = [int(x) for x in input().split()]
    max_perimeter = sort_color(s, {0: 0, 1: 0, 2: 0})
    print(max_perimeter, end='')


if __name__ == '__main__':
    main()
