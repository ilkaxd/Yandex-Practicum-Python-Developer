def find_randomness(array, n):
    count = 0
    for i in range(n):
        current_day = array[i]
        if i == 0:
            previous_day = current_day - 1
        else:
            previous_day = array[i - 1]
        if i == n - 1:
            next_day = current_day - 1
        else:
            next_day = array[i + 1]
        if current_day > next_day and current_day > previous_day:
            count += 1
    return count


def main():
    n = int(input())
    array = [int(x) for x in input().split()]
    result = find_randomness(array, n)
    print(result, end='')


if __name__ == '__main__':
    main()
