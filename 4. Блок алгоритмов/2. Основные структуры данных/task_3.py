class Node:
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(node, idx) -> None:
    next_node = get_node_by_index(node, idx + 1)
    if idx == 0:
        node = next_node
        return node
    previous_node = get_node_by_index(node, idx - 1)
    previous_node.next_item = next_node
    return node
