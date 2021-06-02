def find_nearest_power_of_2(n):
    if n < 2:
        return str(n)
    degree = 1
    while True:
        if 2 ** (degree + 1) > n:
            break
        degree += 1
    remain = n - 2 ** degree
    return str(degree) + " " + find_nearest_power_of_2(remain)


def convert_10_to_2(n):
    sequence = find_nearest_power_of_2(n)
    array = sequence.split()
    value_len = int(array[0])
    result = ['0'] * (value_len + 1)
    result[-1] = array[-1]
    reversed_array = [(value_len - int(x)) for x in array[:-1]]
    for i in reversed_array:
        result[i] = '1'
    return ''.join(result)


def main():
    n = int(input())
    result = convert_10_to_2(n)
    print(result, end='')


if __name__ == '__main__':
    main()
