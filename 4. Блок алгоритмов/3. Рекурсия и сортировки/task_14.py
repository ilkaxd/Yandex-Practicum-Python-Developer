def merge_flowerbeds(x, y):
    if x[1] < y[0]:
        return [y[0], y[1]]
    else:
        return [min(x[0], y[0]), max(x[1], y[1])]


def find_flowerbeds(array, n):
    array.sort(key=lambda x: int(x[0]))
    result = [f'{array[0][0]} {array[0][1]}']
    current = array[0]
    for i in range(1, n):
        merge_item = merge_flowerbeds(current, array[i])
        if merge_item == array[i]:
            result.append(f'{merge_item[0]} {merge_item[1]}')
        else:
            result[-1] = f'{merge_item[0]} {merge_item[1]}'
        current = merge_item
    return result


def main():
    n = int(input())
    gardeners = []
    for _ in range(n):
        gardeners.append([int(x) for x in input().split()])
    r = find_flowerbeds(gardeners, n)
    print(*r, sep='\n')


if __name__ == '__main__':
    main()
