# 51879067
def binary_search(array, left, right, key):
    if left > right:
        return -1

    mid = (left + right) // 2

    left_value = array[left]
    mid_value = array[mid]
    right_value = array[right]

    if mid_value == key:
        return mid

    # array is sorted
    if left_value <= mid_value:
        # subarray is sorted
        if key >= left_value and key <= mid_value:
            return binary_search(array, left, mid - 1, key)
        return binary_search(array, mid + 1, right, key)
    if key >= mid_value and key <= right_value:
        return binary_search(array, mid + 1, right, key)
    return binary_search(array, left, mid - 1, key)


def main():
    n = int(input())
    k = int(input())
    array = [int(i) for i in input().split()]
    print(binary_search(array, 0, n - 1, k), end='')


if __name__ == '__main__':
    main()
