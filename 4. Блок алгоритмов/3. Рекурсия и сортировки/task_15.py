def check_index(array, middle, k_position, s_len):
    left = count = 0
    for right in range(s_len):
        val_right = array[right]
        val_left = array[left]
        while val_right - val_left > middle:
            left += 1
            val_left = array[left]
        count += right - left
        if count >= k_position:
            return True
    return False


def diff(s_len, s, k_position):
    s.sort()
    left, right = 0, s[-1] - s[0]
    while left < right:
        middle = (left + right) // 2
        if check_index(s, middle, k_position, s_len):
            right = middle
        else:
            left = middle + 1
    return left


def main():
    n = int(input())
    arc = list(map(int, input().split()))
    k = int(input())
    result = diff(n, arc, k)
    print(result, end='')


if __name__ == '__main__':
    main()
