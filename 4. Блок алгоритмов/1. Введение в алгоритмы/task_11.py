def main():
    _ = input()
    a = int("".join([letter for letter in input() if letter != " "]))
    b = int(input())

    result = a + b
    result = [i for i in str(result)]

    print(" ".join(result), end='')


if __name__ == '__main__':
    main()
