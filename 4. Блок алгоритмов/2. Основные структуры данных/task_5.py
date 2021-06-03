class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node):
    current = node
    next_node = current.next
    current.next = None
    current.prev = next_node

    while next_node is not None:
        next_node.prev = next_node.next
        next_node.next = current
        current = next_node
        next_node = next_node.prev
    return current
