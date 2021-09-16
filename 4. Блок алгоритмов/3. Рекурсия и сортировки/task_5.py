def max_house_amount(cash, houses):
    result = 0
    for house in houses:
        if cash - house >= 0:
            cash -= house
            result += 1
        else:
            return result
    return result


def main():
    _, cash = [int(x) for x in input().split()]
    houses = sorted([int(x) for x in input().split()])
    print(max_house_amount(cash, houses), end='')


if __name__ == '__main__':
    main()
