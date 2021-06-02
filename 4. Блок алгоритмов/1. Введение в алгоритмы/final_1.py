def distance(n, street):
    result = [-1] * n

    for i, house in enumerate(street):

        if house == '0':
            result[i] = 0
        else:
            previous = i - 1
            if previous >= 0 and result[previous] != -1:
                result[i] = result[previous] + 1

    for i, house in enumerate(street[::-1]):
        if house != '0':
            current = n - i - 1
            next_i = current + 1
            if 0 <= next_i <= n - 1:
                if result[current] == -1:
                    result[current] = result[next_i] + 1
                else:
                    result[current] = min(result[current],
                                          result[next_i] + 1)
    return result


def main():
    n = int(input().rstrip())
    street = input().rstrip().split()
    print(*distance(n, street), end='')


if __name__ == '__main__':
    main()
