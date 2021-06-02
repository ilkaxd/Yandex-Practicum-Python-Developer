def quadratic_equation(a, x, b, c):
    return a * x**2 + b * x + c


def main():
    line = input()
    a, x, b, c = [int(t) for t in line.split()]

    result = quadratic_equation(a, x, b, c)
    print(result, end='')


if __name__ == '__main__':
    main()
