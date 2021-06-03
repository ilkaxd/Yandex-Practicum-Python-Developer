class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()


operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}


def main():
    string = input().rstrip().split()
    obj = Stack()
    for ch in string:
        if ch in operations.keys():
            y = obj.pop()
            x = obj.pop()
            result = operations[ch](x, y)
            obj.push(result)
        else:
            obj.push(int(ch))
    print(obj.pop(), end='')


if __name__ == '__main__':
    main()
