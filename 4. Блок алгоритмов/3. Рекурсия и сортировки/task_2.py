phone_keys = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def print_sequences(s, prefix):
    if len(s) == 0:
        return prefix
    else:
        number = s[0]
        result = ''
        for ch in phone_keys[number]:
            result += print_sequences(s[1:], prefix + ch) + " "
        return result.strip(' ')


def main():
    s = input()
    result = print_sequences(s, '')
    print(result, end='')


if __name__ == '__main__':
    main()
