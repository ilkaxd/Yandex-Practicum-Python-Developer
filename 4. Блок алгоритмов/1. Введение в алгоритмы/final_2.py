import collections


def play_game(n, matrix):
    buttons = collections.defaultdict(int)
    for ch in matrix:
        if ch != '.':
            buttons[ch] += 1
    points = 0
    for value in buttons.values():
        if value <= n * 2:
            points += 1
    return points


def main():
    n = int(input().rstrip())
    matrix = ""
    for _ in range(4):
        matrix += input().rstrip()
    print(play_game(n, matrix), end='')


if __name__ == '__main__':
    main()
