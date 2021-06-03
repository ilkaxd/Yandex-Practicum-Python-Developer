def transpose(matrix, rows, columns):
    result = [[-1 for _ in range(rows)]
              for _ in range(columns)]
    for row in range(rows):
        for column in range(columns):
            result[column][row] = matrix[row][column]
    return "\n".join([' '.join(map(str, row)) for row in result])


def main():
    rows = int(input())
    columns = int(input())
    matrix = []
    for _ in range(rows):
        matrix.append(input().split())

    result = transpose(matrix, rows, columns)
    print(result, end='')


if __name__ == '__main__':
    main()
