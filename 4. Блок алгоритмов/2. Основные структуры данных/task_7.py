class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_items = []

    def pop(self):
        if len(self.items) == 0:
            return 'error'
        x = self.items.pop()
        if x == self.max_items[-1]:
            self.max_items.pop()

    def push(self, x):
        if (len(self.max_items) < 1) or (self.max_items[-1] <= x):
            self.max_items.append(x)
        self.items.append(x)

    def get_max(self):
        if len(self.max_items) == 0:
            return 'None'
        return self.max_items[-1]


def main():
    n = int(input().rstrip())
    obj = StackMaxEffective()
    for _ in range(n):
        function = input().rstrip()
        if function == 'get_max':
            print(obj.get_max())
        if function.startswith('push'):
            obj.push(int(function.split()[1]))
        if function == 'pop':
            if obj.pop() == 'error':
                print('error')


if __name__ == '__main__':
    main()
