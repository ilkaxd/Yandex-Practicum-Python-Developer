def find_excess_letter(s, t):
    s_letters = {}
    t_letters = {}
    for s_word in s:
        value = s_letters.get(s_word)
        if value is None:
            value = 0
        value += 1
        s_letters[s_word] = value

    for t_word in t:
        value = t_letters.get(t_word)
        if value is None:
            value = 0
        value += 1
        t_letters[t_word] = value

    for key, value_t in t_letters.items():
        value_s = s_letters.get(key)
        if value_s is None or value_s != value_t:
            return key


def main():
    s = input()
    t = input()
    result = find_excess_letter(s, t)
    print(result, end='')


if __name__ == '__main__':
    main()
