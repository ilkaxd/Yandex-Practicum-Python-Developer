def binary_search(s, price, left, right):
    if right < left:
        return -1

    if s[left] >= price:
        return left + 1

    mid = (left + right) // 2

    if s[left] < price <= s[mid]:
        temp = binary_search(s, price, left, mid)
        if temp == -1:
            return mid + 1
        return temp
    return binary_search(s, price, mid + 1, right)


def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    price = int(input())

    result = binary_search(s, price, 0, n - 1)
    if result == -1:
        result_2 = -1
    else:
        result_2 = binary_search(s, price * 2, 0, n - 1)
    print(result, result_2, end='')


if __name__ == '__main__':
    main()
