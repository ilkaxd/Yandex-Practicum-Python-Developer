def is_correct_bracket_seq(s):
    input_ch = []
    for ch in s:
        if ch in ['{', '[', '(']:
            input_ch.append(ch)
        else:
            if len(input_ch) == 0:
                return False
            x = input_ch.pop()
            if x == '{' and ch != '}':
                return False
            if x == '(' and ch != ')':
                return False
            if x == '[' and ch != ']':
                return False
    if len(input_ch) != 0:
        return False
    return True


def main():
    s = input().rstrip()
    print(is_correct_bracket_seq(s), end='')


if __name__ == '__main__':
    main()
