def find_neighbors(row, column, matrix, rows, columns):
    result = []
    for delta_row, delta_column in ((0, -1),
                                    (0, 1),
                                    (-1, 0),
                                    (1, 0)):
        current_row = row + delta_row
        current_column = column + delta_column

        if (
            0 <= current_row < rows and
            0 <= current_column < columns
        ):
            result.append(matrix[current_row][current_column])
    if result == []:
        return ""
    result = sorted(map(int, result))
    result = map(str, result)
    return ' '.join(result)


def main():
    rows = int(input())
    columns = int(input())
    matrix = []
    for _ in range(rows):
        line = input()
        matrix.append(line.split())
    target_row = int(input())
    target_column = int(input())

    print(
        find_neighbors(target_row, target_column, matrix, rows, columns),
        end=''
    )


if __name__ == '__main__':
    main()
