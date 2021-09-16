import random


class Participant:
    def __init__(self, name, solutions, errors):
        self.solutions = int(solutions)
        self.errors = int(errors)
        self.name = name

    def __lt__(self, other):
        if self.solutions > other.solutions:
            return True
        if self.solutions == other.solutions:
            if self.errors < other.errors:
                return True
            if self.errors == other.errors:
                if self.name < other.name:
                    return True
        return False

    def __gt__(self, other):
        if self.solutions < other.solutions:
            return True
        if self.solutions == other.solutions:
            if self.errors > other.errors:
                return True
            if self.errors == other.errors:
                if self.name > other.name:
                    return True
        return False

    def __str__(self):
        return self.name


def partition(a, left, right):
    pivot_idx = random.choice(range(left, right + 1))
    pivot = a[pivot_idx]

    i = left - 1
    j = right + 1

    while True:
        i += 1
        while a[i] < pivot:
            i += 1

        j -= 1
        while a[j] > pivot:
            j -= 1

        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]


def quicksort(array, n):
    def _quicksort(array, left, right):
        if right > left:
            pivot = partition(array, left, right)
            _quicksort(array, left, pivot)
            _quicksort(array, pivot + 1, right)
    _quicksort(array, 0, n - 1)


def main():
    participants = []

    n = int(input())
    for _ in range(n):
        name, solutions, errors = input().split()
        participants.append(Participant(name, solutions, errors))

    quicksort(participants, n)

    print(*participants, sep='\n')


if __name__ == '__main__':
    main()
