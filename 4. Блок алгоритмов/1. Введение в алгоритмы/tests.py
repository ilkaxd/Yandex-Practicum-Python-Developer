import unittest
from io import StringIO
from typing import Callable, List, Tuple
from unittest.mock import patch

from final_1 import main as final_1_main
from final_2 import main as final_2_main
from task_1 import main as task_1_main
from task_2 import main as task_2_main
from task_3 import main as task_3_main
from task_4 import main as task_4_main
from task_5 import main as task_5_main
from task_6 import main as task_6_main
from task_7 import main as task_7_main
from task_8 import main as task_8_main
from task_9 import main as task_9_main
from task_10 import main as task_10_main
from task_11 import main as task_11_main
from task_12 import main as task_12_main


class Sprint12TestCase(unittest.TestCase):
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

    def test_task_1(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            ('-8 -5 -2 7', '-183'),
            ('8 2 9 -10', '40'),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_1', [inp], task_1_main, res
            )

    def test_task_2(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (
            ('1 2 -3', 'FAIL'),
            ('7 11 7', 'WIN'),
            ('6 -2 0', 'WIN'),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_2', [inp], task_2_main, res
            )

    def test_task_3(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
                (
                    '4\n' +
                    '3\n' +
                    '1 2 3\n' +
                    '0 2 6\n' +
                    '7 4 1\n' +
                    '2 7 0\n' +
                    '3\n' +
                    '0', '7 7'
                ),

                (
                    '4\n' +
                    '3\n' +
                    '1 2 3\n' +
                    '0 2 6\n' +
                    '7 4 1\n' +
                    '2 7 0\n' +
                    '0\n' +
                    '0', '0 2'
                ),
            )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_3', inp.split('\n'), task_3_main, res
            )

    def test_task_4(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
                (
                    '7\n' +
                    '-1 -10 -8 0 2 0 5', '3'
                ),

                (
                    '5\n' +
                    '1 2 5 4 8', '2'
                ),
            )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_4', inp.split('\n'), task_4_main, res
            )

    def test_task_5(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (
                (
                    '19\n' +
                    'i love segment tree', 'segment\n7'
                ),

                (
                    '21\n' +
                    'frog jumps from river', 'jumps\n5'
                ),

                (
                    '17\n' +
                    ' sybtbv jxqwbu cj', 'sybtbv\n6'
                ),
            )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_5', inp.split('\n'), task_5_main, res
            )

    def test_task_6(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
                ('A man, a plan, a canal: Panama', 'True'),
                ('zo', 'False'),
            )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_6', [inp], task_6_main, res
            )

    def test_task_7(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
                ('5', '101'),
                ('14', '1110'),
            )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_7', [inp], task_7_main, res
            )

    def test_task_8(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
                ('1010\n1011', '10101'),
                ('1\n1', '10'),
            )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_8', inp.split('\n'), task_8_main, res
            )

    def test_task_9(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
                ('15', 'False'),
                ('16', 'True'),
            )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_9', [inp], task_9_main, res
            )

    def test_task_10(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (
                ('8', '2 2 2'),
                ('13', '13'),
                ('100', '2 2 5 5'),
            )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_10', [inp], task_10_main, res
            )

    def test_task_11(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
                (
                    '4\n' +
                    '1 2 0 0\n' +
                    '34', '1 2 3 4'
                ),

                (
                    '2\n' +
                    '9 5\n' +
                    '17', '1 1 2'
                ),
            )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_11', inp.split('\n'), task_11_main, res
            )

    def test_task_12(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (
                (
                    'abcd\n' +
                    'abcde', 'e'
                ),

                (
                    'go\n' +
                    'ogg', 'g'
                ),

                (
                    'xtkpx\n' +
                    'xkctpx', 'c'
                ),
            )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_12', inp.split('\n'), task_12_main, res
            )

    def test_final_1(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
                (
                    '5\n' +
                    '0 1 4 9 0', '0 1 2 1 0'
                ),

                (
                    '6\n' +
                    '0 7 9 4 8 20', '0 1 2 3 4 5'
                ),
            )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'final_1', inp.split('\n'), final_1_main, res
            )

    def test_final_2(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (
                (
                    '3\n' +
                    '1231\n' +
                    '2..2\n' +
                    '2..2\n' +
                    '2..2', '2'
                ),

                (
                    '4\n' +
                    '1111\n' +
                    '9999\n' +
                    '1111\n' +
                    '9911', '1'
                ),

                (
                    '4\n' +
                    '1111\n' +
                    '1111\n' +
                    '1111\n' +
                    '1111', '0'
                ),
            )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'final_2', inp.split('\n'), final_2_main, res
            )


if __name__ == '__main__':
    unittest.main()
