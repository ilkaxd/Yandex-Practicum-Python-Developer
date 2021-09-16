def find_common_median(a, b, a_len, b_len):
    size = (a_len + b_len) // 2
    if (a_len + b_len) % 2 == 0:
        even_size = True
    else:
        size += 1
        even_size = False

    counter_a = 0
    counter_b = 0
    median = 0

    for i in range(size):
        # Остались элементы только в массиве b
        if (counter_a >= a_len):
            counter_b = counter_b + (size - i)
            median = b[counter_b - 1]
            break
        # Остались элементы только в массиве a
        if (counter_b >= b_len):
            counter_a = counter_a + (size - i)
            median = a[counter_a - 1]
            break
        a_i = a[counter_a]
        b_i = b[counter_b]
        if a_i <= b_i:
            median = a_i
            counter_a += 1
        else:
            median = b_i
            counter_b += 1

    if even_size:
        if counter_a < a_len:
            next_a = a[counter_a]
        else:
            next_a = a[counter_a - 2]
        if counter_b < b_len:
            next_b = b[counter_b]
        else:
            next_b = b[counter_b - 2]

        if next_a < median:
            next_a = float('+inf')
        if next_b < median:
            next_b = float('+inf')

        median = (median + min(next_a, next_b)) / 2
    return median


def main():
    n = int(input())
    m = int(input())
    north = [int(x) for x in input().split()]
    south = [int(x) for x in input().split()]
    r = find_common_median(north, south, n, m)
    print(r, end='')


if __name__ == '__main__':
    main()
