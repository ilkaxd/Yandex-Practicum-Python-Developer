from collections import defaultdict


def find_most_popular_universities(s, max_number, dictionary):
    if len(s) == 0:
        rating = dictionary.items()
        result = sorted(rating, reverse=True, key=lambda x: x[1])[:max_number]
        return ' '.join(str(x[0]) for x in result)
    dictionary[s[0]] += 1
    return find_most_popular_universities(s[1:], max_number, dictionary)


def main():
    dictionary = defaultdict(int)
    _ = int(input())
    s = [int(x) for x in input().split()]
    n = int(input())
    universities = find_most_popular_universities(s, n, dictionary)
    print(universities, end='')


if __name__ == '__main__':
    main()
