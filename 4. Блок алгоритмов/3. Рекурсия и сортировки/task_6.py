def find_max_perimeter_r(s, prefix):
    if len(prefix) == 3:
        a, b, c = prefix
        if (
            a + b > c and
            a + c > b and
            b + c > a
        ):
            return a + b + c
        return
    for i in range(len(s)):
        t = find_max_perimeter_r(s[i + 1:], prefix + [s[i]])
        if t is not None:
            return t


def main():
    _ = int(input())
    s = [int(x) for x in input().split()]
    s.sort(reverse=True)
    max_perimeter = find_max_perimeter_r(s, [])
    print(max_perimeter, end='')


if __name__ == '__main__':
    main()
