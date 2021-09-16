def bubble_sort(s, checked):
    is_sorted = True
    for i in range(1, len(s)):
        if s[i - 1] > s[i]:
            is_sorted = False
            break

    if is_sorted:
        if not checked:
            print(*s)
        return s
    checked = True
    for i in range(1, len(s)):
        if s[i - 1] > s[i]:
            s[i], s[i - 1] = s[i - 1], s[i]
    print(*s)
    return bubble_sort(s, checked)


def main():
    _ = int(input())
    s = [int(x) for x in input().split()]
    bubble_sort(s, False)


if __name__ == '__main__':
    main()
