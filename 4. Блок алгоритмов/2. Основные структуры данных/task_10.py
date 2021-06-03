class Node:
    def __init__(self, value=None, next_item=None, previous_item=None):
        self.value = value
        self.next_item = next_item
        self.previous_item = previous_item


class MyQueueSized:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.current_size = 0

    def put(self, x):
        obj = Node(value=x)
        if self.tail is None:
            self.tail = obj
            self.queue = obj
            self.head = obj
        else:
            obj.previous_item = self.tail
            self.tail.next_item = obj
            self.tail = obj
        self.current_size += 1

    def get(self):
        if self.tail is None:
            return 'error'
        result = self.head.value
        self.head = self.head.next_item
        if self.head is None:
            self.tail = None
        self.current_size -= 1
        return result

    def size(self):
        return self.current_size


def main():
    n = int(input().rstrip())
    obj = MyQueueSized()
    for _ in range(n):
        function = input().rstrip()
        if function == 'get':
            print(obj.get())

        if function.startswith('put'):
            if obj.put(int(function.split()[1])) == 'error':
                print('error')

        if function == 'size':
            print(obj.size())


if __name__ == '__main__':
    main()
