def bigger(x, y):
    return int(str(x) + str(y)) > int(str(y) + str(x))


def find_bigger_value(s, n, idx):
    if idx == n:
        return ''.join(str(x) for x in s)
    item_to_insert = s[idx]
    j = idx
    while j > 0 and bigger(item_to_insert, s[j - 1]):
        s[j] = s[j - 1]
        j -= 1
    s[j] = item_to_insert
    return find_bigger_value(s, n, idx + 1)


def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    result = find_bigger_value(s, n, 1)
    print(result, end='')


if __name__ == '__main__':
    main()
