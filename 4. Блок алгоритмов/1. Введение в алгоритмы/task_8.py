def add_2_to_2(a, b):
    temp = 0
    steps = max(len(a), len(b))
    a = a.zfill(steps)
    b = b.zfill(steps)

    result = [0] * (steps + 1)
    for i in range(steps - 1, -1, -1):
        int_a = int(a[i])
        int_b = int(b[i])
        all_sum = int_a + int_b + temp
        result[i + 1] = all_sum % 2
        temp = all_sum // 2
    result[0] = temp
    if result[0] == 0:
        result = result[1:]
    return ''.join(map(str, result))


def main():
    a = input()
    b = input()
    result = add_2_to_2(a, b)
    print(result, end='')


if __name__ == '__main__':
    main()
