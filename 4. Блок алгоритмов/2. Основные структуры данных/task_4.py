class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, value) -> None:
    idx = 0
    while True:
        if node is None:
            return -1
        if node.value == value:
            return idx
        node = node.next_item
        idx += 1
