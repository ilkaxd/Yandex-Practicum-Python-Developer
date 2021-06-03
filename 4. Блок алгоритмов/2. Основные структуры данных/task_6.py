class StackMax:
    def __init__(self) -> None:
        self.item = []

    def push(self, x):
        self.item.append(x)

    def pop(self):
        try:
            return self.item.pop()
        except IndexError:
            return 'error'

    def get_max(self):
        if len(self.item) == 0:
            return 'None'
        return max(self.item)


def main():
    n = int(input().rstrip())
    obj = StackMax()
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
