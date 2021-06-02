import string


def is_palidrom(words):
    words = words.lower()
    only_letters = ''.join(x for x in words
                           if x not in string.punctuation + " ")
    reverse = only_letters[::-1]
    return only_letters == reverse


def main():
    words = input()
    result = is_palidrom(words)
    print(result, end='')


if __name__ == '__main__':
    main()
