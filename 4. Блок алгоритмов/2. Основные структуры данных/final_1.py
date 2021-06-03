class CustomDeque:
    def __init__(self, size):
        self.__deque = [None] * size
        self.head = 0
        self.tail = 0
        self.size = 0
        self.max_size = size

    def check_deque(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            print("\nfunction result:", result)
            print(self.__deque)
            print(f"Head: {self.head}; Tail: {self.tail}")
            print(f'Deck size: {self.size}')
            print("".center(60, '-'))
            print()
        return wrapper

    def right_index(self, n):
        if n < 0:
            return self.max_size + n
        return n % self.max_size

    def push_back(self, value):
        if self.size == self.max_size:
            raise MemoryError

        if self.size != 0:
            self.tail = self.right_index(self.tail + 1)
        self.__deque[self.tail] = value
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_size:
            raise MemoryError

        if self.size != 0:
            self.head = self.right_index(self.head - 1)
        self.__deque[self.head] = value
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise IndexError

        result = self.__deque[self.head]
        self.__deque[self.head] = None
        self.size -= 1

        if self.size != 0:
            self.head = self.right_index(self.head + 1)
        return result

    def pop_back(self):
        if self.size == 0:
            raise IndexError

        result = self.__deque[self.tail]
        self.__deque[self.tail] = None
        self.size -= 1
        if self.size != 0:
            self.tail = self.right_index(self.tail - 1)
        return result


def main():
    n = int(input().rstrip())
    size = int(input().rstrip())
    obj = CustomDeque(size)

    for _ in range(n):
        try:
            commands = input().rstrip().split()
            if commands[0] == 'push_back':
                r = obj.push_back(commands[1])
            elif commands[0] == 'push_front':
                r = obj.push_front(commands[1])
            elif commands[0] == 'pop_front':
                r = obj.pop_front()
            else:
                r = obj.pop_back()
            if r is not None:
                print(r)
        except MemoryError:
            print('error')
        except IndexError:
            print('error')


if __name__ == '__main__':
    main()
