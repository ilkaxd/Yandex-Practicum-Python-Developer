def is_substring(s, t, idx_1, idx_2, max_len_1, max_len_2):
    if idx_1 == max_len_1:
        return True
    if idx_2 == max_len_2:
        return False
    if s[idx_1] == t[idx_2]:
        return is_substring(s, t, idx_1 + 1, idx_2 + 1, max_len_1, max_len_2)
    else:
        return is_substring(s, t, idx_1, idx_2 + 1, max_len_1, max_len_2)


def is_substring_for(s, t):
    i = 0
    ie = len(s)

    if ie > 0:
        for c in t:
            if c == s[i]:
                i += 1
                if i >= ie:
                    break
    return i >= ie


def main():
    s = input()
    t = input()
    result = is_substring(s, t, 0, 0, len(s), len(t))
    print(result, end='')


if __name__ == '__main__':
    main()
