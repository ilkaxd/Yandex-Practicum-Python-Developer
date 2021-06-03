import unittest
from io import StringIO
from typing import Callable, List, Optional, Tuple
from unittest.mock import patch

from final_1 import main as final_1_main
from final_2 import main as final_2_main
from task_1 import main as task_1_main
from task_2 import solution as task_2_main
from task_3 import solution as task_3_main
from task_4 import solution as task_4_main
from task_5 import solution as task_5_main
from task_6 import main as task_6_main
from task_7 import main as task_7_main
from task_8 import main as task_8_main
from task_9 import main as task_9_main
from task_10 import main as task_10_main
from task_11 import main as task_11_main
from task_12 import main as task_12_main


class Node:
    value: str
    next_item: Optional['Node']

    def __init__(
        self, value: str, next_item: Optional['Node'] = None
    ) -> None:
        self.value: str = value
        self.next_item: Optional['Node'] = next_item


class DoubleConnectedNode:
    value: str
    next: Optional['DoubleConnectedNode']
    prev: Optional['DoubleConnectedNode']

    def __init__(
        self,
        value: str,
        next: Optional['DoubleConnectedNode'] = None,
        prev: Optional['DoubleConnectedNode'] = None
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class Sprint13TestCase(unittest.TestCase):
    def _assert_correct_output(
        self,
        subtest_name: str,
        module: str,
        side_effect: List[str],
        test_func: Callable,
        expected_result: str
    ) -> None:
        with self.subTest(
            name=subtest_name
            ), patch(
                f'{module}.input', side_effect=side_effect
                ), patch(
                    'sys.stdout', new=StringIO()
                    ) as fake_out:
            test_func()
            self.assertEqual(
                fake_out.getvalue(),
                expected_result
                )

    def _linked_list_factory(
        self, count: int, skipped: int = None
    ) -> Tuple[Node, List[Node]]:
        '''
        Create <count> of Nodes,
        return head of linked list
        '''
        next_node: Optional[Node] = None
        nodes: List[Node] = []
        for idx in range(count - 1, -1, -1):
            if idx != skipped:
                node: Node = Node(f'item{idx}', next_item=next_node)
                next_node: Node = node
                nodes.append(node)
        return next_node, nodes

    def _double_linked_list_factory(
        self, count: int
    ) -> Tuple[DoubleConnectedNode, List[DoubleConnectedNode]]:
        '''
        Create <count> of DoubleConnectedNode,
        return head of double linked list
        '''
        next_node: Optional[DoubleConnectedNode] = None
        previous_node: Optional[DoubleConnectedNode] = None
        nodes: List[Node] = []
        for idx in range(count - 1, -1, -1):
            node: DoubleConnectedNode = DoubleConnectedNode(
                f'item{idx}',
                next=next_node,
                prev=previous_node
            )
            previous_node: Node = next_node
            next_node: Node = node
            nodes.append(node)
        return next_node, nodes

    def _take_all_values(self, q: Node) -> List[str]:
        values = []
        while q is not None:
            values.append(q.value)
            q = q.next_item
        return values

    def _take_all_values_double_connected(
        self, q: DoubleConnectedNode
    ) -> List[str]:
        values = []
        while q is not None:
            values.append(q.value)
            q = q.next
        return values

    def _compare_queues(self, q_1: Node, q_2: Node):
        values_1 = self._take_all_values(q_1)
        values_2 = self._take_all_values(q_2)
        return self.assertEqual(values_1, values_2)

    def test_task_1(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '4\n' +
                '3\n' +
                '1 2 3\n' +
                '0 2 6\n' +
                '7 4 1\n' +
                '2 7 0',

                '1 0 7 2\n' +
                '2 2 4 7\n' +
                '3 6 1 0'
            ),

            (
                '9\n' +
                '5\n' +
                '-7 -1 0 -4 -9\n' +
                '5 -1 2 2 9\n' +
                '3 1 -8 -1 -7\n' +
                '9 0 8 -8 -1\n' +
                '2 4 5 2 8\n' +
                '-7 10 0 -4 -8\n' +
                '-3 10 -7 10 3\n' +
                '1 6 -7 -5 9\n' +
                '-1 9 9 1 9',

                '-7 5 3 9 2 -7 -3 1 -1\n' +
                '-1 -1 1 0 4 10 10 6 9\n' +
                '0 2 -8 8 5 0 -7 -7 9\n' +
                '-4 2 -1 -8 2 -4 10 -5 1\n' +
                '-9 9 -7 -1 8 -8 3 9 9'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_1', inp.split('\n'), task_1_main, res
            )

    def test_task_2(self):
        cases: Tuple[Tuple[Tuple[Node, List[Node]], str],
                     Tuple[Tuple[Node, List[Node]], str],
                     Tuple[Tuple[Node, List[Node]], str]] = (
            (self._linked_list_factory(1), 'item0\n'),
            (self._linked_list_factory(2), 'item0\nitem1\n'),
            (self._linked_list_factory(3), 'item0\nitem1\nitem2\n'),
        )

        for node_factory, res in cases:
            head, _ = node_factory
            with self.subTest(
                name=f'test {res}'
                ), patch(
                    'sys.stdout', new=StringIO()) as fake_out:
                task_2_main(head)
                self.assertEqual(
                    fake_out.getvalue(),
                    res)

    def test_task_3(self):
        size = 10
        start = 0
        middle = size // 2
        end = size - 1
        cases: Tuple[Tuple[int, Tuple[Node, List[Node]]],
                     Tuple[int, Tuple[Node, List[Node]]],
                     Tuple[int, Tuple[Node, List[Node]]]] = (
            (start, self._linked_list_factory(size, start)),
            (middle, self._linked_list_factory(size, middle)),
            (end, self._linked_list_factory(size, end)),
        )

        for idx, (res, _) in cases:
            with self.subTest():
                head, _ = self._linked_list_factory(size)
                solved = task_3_main(head, idx)
                self._compare_queues(solved, res)

    def test_task_4(self):
        cases = (
            (self._linked_list_factory(20), 11),
            (self._linked_list_factory(20), 1),
            (self._linked_list_factory(20), 0),
            (self._linked_list_factory(20), 19),
            (self._linked_list_factory(20), -1),
        )

        for node_factory, res in cases:
            with self.subTest(res=res):
                head, nodes = node_factory
                if res == -1:
                    elem = Node("absent element")
                else:
                    elem = nodes[-res - 1]
                idx = task_4_main(head, elem.value)
                self.assertEqual(idx, res)

    def test_task_5(self):
        cases = (
            self._double_linked_list_factory(1),
            self._double_linked_list_factory(2),
            self._double_linked_list_factory(3),
        )

        for node_factory in cases:
            with self.subTest():
                head, nodes = node_factory
                actual = [node.value for node in nodes]
                result = task_5_main(head)
                self.assertEqual(
                    self._take_all_values_double_connected(result),
                    actual
                )

    def test_task_6(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '8\n' +
                'get_max\n' +
                'push 7\n' +
                'pop\n' +
                'push -2\n' +
                'push -1\n' +
                'pop\n' +
                'get_max\n' +
                'get_max\n',

                'None\n' +
                '-2\n' +
                '-2\n'
            ),

            (
                '7\n' +
                'get_max\n' +
                'pop\n' +
                'pop\n' +
                'pop\n' +
                'push 10\n' +
                'get_max\n' +
                'push -9\n',

                'None\n' +
                'error\n' +
                'error\n' +
                'error\n' +
                '10\n'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_6', inp.split('\n'), task_6_main, res
            )

    def test_task_7(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '10\n' +
                'pop\n' +
                'pop\n' +
                'push 4\n' +
                'push -5\n' +
                'push 7\n' +
                'pop\n' +
                'pop\n' +
                'get_max\n' +
                'pop\n' +
                'get_max\n',

                'error\n' +
                'error\n' +
                '4\n' +
                'None\n'
            ),

            (
                '10\n' +
                'get_max\n' +
                'push -6\n' +
                'pop\n' +
                'pop\n' +
                'get_max\n' +
                'push 2\n' +
                'get_max\n' +
                'pop\n' +
                'push -2\n' +
                'push -6\n',

                'None\n' +
                'error\n' +
                'None\n' +
                '2\n'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_7', inp.split('\n'), task_7_main, res
            )

    def test_task_8(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            ('{[()]}', 'True'),
            ('()', 'True')
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_8', [inp], task_8_main, res
            )

    def test_task_9(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '8\n' +
                '2\n' +
                'peek\n' +
                'push 5\n' +
                'push 2\n' +
                'peek\n' +
                'size\n' +
                'size\n' +
                'push 1\n' +
                'size',

                'None\n' +
                '5\n' +
                '2\n' +
                '2\n' +
                'error\n' +
                '2\n'
            ),

            (
                '10\n' +
                '1\n' +
                'push 1\n' +
                'size\n' +
                'push 3\n' +
                'size\n' +
                'push 1\n' +
                'pop\n' +
                'push 1\n' +
                'pop\n' +
                'push 3\n' +
                'push 3\n',

                '1\n' +
                'error\n' +
                '1\n' +
                'error\n' +
                '1\n' +
                '1\n' +
                'error\n'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_9', inp.split('\n'), task_9_main, res
            )

    def test_task_10(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '10\n' +
                'put -34\n' +
                'put -23\n' +
                'get\n' +
                'size\n' +
                'get\n' +
                'size\n' +
                'get\n' +
                'get\n' +
                'put 80\n' +
                'size',

                '-34\n' +
                '1\n' +
                '-23\n' +
                '0\n' +
                'error\n' +
                'error\n' +
                '1\n'
            ),

            (
                '6\n' +
                'put -66\n' +
                'put 98\n' +
                'size\n' +
                'size\n' +
                'get\n' +
                'get',

                '2\n' +
                '2\n' +
                '-66\n' +
                '98\n'
            ),

            (
                '9\n' +
                'get\n' +
                'size\n' +
                'put 74\n' +
                'get\n' +
                'size\n' +
                'put 90\n' +
                'size\n' +
                'size\n' +
                'size',

                'error\n' +
                '0\n' +
                '74\n' +
                '0\n' +
                '1\n' +
                '1\n' +
                '1\n'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_10', inp.split('\n'), task_10_main, res
            )

    def test_task_11(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            ('3', '3'),
            ('0', '1')
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_11', [inp], task_11_main, res
            )

    def test_task_12(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            ('3 1', '3'),
            ('10 1', '9')
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_12', [inp], task_12_main, res
            )

    def test_final_1(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '4\n' +
                '4\n' +
                'push_front 861\n' +
                'push_front -819\n' +
                'pop_back\n' +
                'pop_back',

                '861\n' +
                '-819\n'
            ),

            (
                '7\n' +
                '10\n' +
                'push_front -855\n' +
                'push_front 720\n' +
                'pop_back\n' +
                'pop_back\n' +
                'push_back 844\n' +
                'pop_back\n' +
                'push_back 823',

                '-855\n' +
                '720\n' +
                '844\n'
            ),

            (
                '6\n' +
                '6\n' +
                'push_front -201\n' +
                'push_back 959\n' +
                'push_back 102\n' +
                'push_front 20\n' +
                'pop_front\n' +
                'pop_back',

                '20\n' +
                '102\n'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'final_1', inp.split('\n'), final_1_main, res
            )

    def test_final_2(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            ('2 1 + 3 *', '9'),
            ('7 2 + 4 * 2 +', '38')
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'final_2', [inp], final_2_main, res
            )


if __name__ == '__main__':
    unittest.main()
