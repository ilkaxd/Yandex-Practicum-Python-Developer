class MyQueueSized:
    def __init__(self, n) -> None:
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.current_size = 0

    def push(self, x):
        if self.current_size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.current_size += 1
        else:
            return 'error'

    def pop(self):
        if self.current_size == 0:
            return 'None'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.current_size -= 1
        return x

    def peek(self):
        if self.current_size == 0:
            return 'None'
        return self.queue[self.head]

    def size(self):
        return self.current_size


def main():
    n = int(input().rstrip())
    size = int(input().rstrip())
    obj = MyQueueSized(size)
    for _ in range(n):
        function = input().rstrip()
        if function == 'size':
            print(obj.size())

        if function.startswith('push'):
            if obj.push(int(function.split()[1])) == 'error':
                print('error')

        if function == 'pop':
            print(obj.pop())
        if function == 'peek':
            print(obj.peek())


if __name__ == '__main__':
    main()
