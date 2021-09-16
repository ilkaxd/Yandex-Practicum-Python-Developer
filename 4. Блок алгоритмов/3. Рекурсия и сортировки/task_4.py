import sys

sys.setrecursionlimit(10000000)


def happy_count_r(ego, cakes, happy, idx_1, idx_2, n, m):
    if idx_1 == n or idx_2 == m:
        return happy
    child = ego[idx_1]
    cake = cakes[idx_2]

    if cake >= child:
        happy += 1
        return happy_count_r(ego, cakes, happy, idx_1 + 1, idx_2 + 1, n, m)
    return happy_count_r(ego, cakes, happy, idx_1 + 1, idx_2, n, m)


def main():
    children = int(input())
    children_ego = sorted([int(x) for x in input().split()], reverse=True)
    cakes = int(input())
    cakes_size = sorted([int(x) for x in input().split()], reverse=True)
    result = happy_count_r(children_ego, cakes_size, 0, 0, 0, children, cakes)
    print(result, end='')


if __name__ == '__main__':
    main()
