def merge(arr, begin, mid, end) -> list:
    left = arr[begin:mid]
    right = arr[mid:end]

    left_size = len(left)
    right_size = len(right)

    left_i, right_i, k = 0, 0, begin
    while left_i < left_size and right_i < right_size:
        if left[left_i] <= right[right_i]:
            arr[k] = left[left_i]
            left_i += 1
        else:
            arr[k] = right[right_i]
            right_i += 1
        k += 1
    while left_i < left_size:
        arr[k] = left[left_i]
        left_i += 1
        k += 1
    while right_i < right_size:
        arr[k] = right[right_i]
        right_i += 1
        k += 1
    return arr


def merge_sort(arr: list, left: int, right: int) -> None:
    if right - left <= 1:
        return
    pivot = (left + right) // 2
    merge_sort(arr, left, pivot)
    merge_sort(arr, pivot, right)
    merge(arr, left, pivot, right)
