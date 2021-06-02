def find_longest_word(string, n):
    array = string.split()
    longest = ""
    for word in array:
        if len(word) > len(longest):
            longest = word
    return longest


def main():
    n = int(input())
    string = input()
    result = find_longest_word(string, n)

    print(result)
    print(len(result), end='')


if __name__ == '__main__':
    main()
