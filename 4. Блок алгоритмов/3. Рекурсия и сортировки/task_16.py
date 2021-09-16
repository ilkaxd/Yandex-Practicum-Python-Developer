from typing import DefaultDict


def block_count(s, n):
    result = 0
    min_value = 0
    max_value = 0
    conditions = DefaultDict(bool)
    for i in range(0, n):
        ch = s[i]
        max_value = max(max_value, ch)

        conditions[ch] = True

        subset_condition = []
        for j in range(min_value, max_value + 1):
            subset_condition.append(conditions[j])
        if all(subset_condition):
            min_value = max_value
            result += 1
    return result


def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    print(block_count(s, n))


if __name__ == '__main__':
    main()
