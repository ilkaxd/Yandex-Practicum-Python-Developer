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
from task_11 import merge as task_11_merge
from task_11 import merge_sort as task_11_merge_sort
from task_12 import main as task_12_main
from task_13 import main as task_13_main
from task_14 import main as task_14_main
from task_15 import main as task_15_main
from task_16 import main as task_16_main


class Sprint14TestCase(unittest.TestCase):
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
            (
                '3',

                '((()))\n' +
                '(()())\n' +
                '(())()\n' +
                '()(())\n' +
                '()()()\n'
            ),

            (
                '2',

                '(())\n' +
                '()()\n'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_1', [inp], task_1_main, res
            )

    def test_task_2(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            ('23', 'ad ae af bd be bf cd ce cf'),
            ('92', 'wa wb wc xa xb xc ya yb yc za zb zc'),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_2', [inp], task_2_main, res
            )

    def test_task_3(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            (
                'abc\n' +
                'ahbgdcu',
                'True'
            ),
            (
                'abcp\n' +
                'ahpc',
                'False'
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
                '2\n' +
                '1 2\n' +
                '3\n' +
                '2 1 3',
                '2'
            ),

            (
                '3\n' +
                '2 1 3\n' +
                '2\n' +
                '1 1',
                '1'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_4', inp.split('\n'), task_4_main, res
            )

    def test_task_5(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '3 300\n' +
                '999 999 999',
                '0'
            ),

            (
                '3 1000\n' +
                '350 999 200',
                '2'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_5', inp.split('\n'), task_5_main, res
            )

    def test_task_6(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '4\n' +
                '6 3 3 2',
                '8'
            ),

            (
                '6\n' +
                '5 3 7 2 8 3',
                '20'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_6', inp.split('\n'), task_6_main, res
            )

    def test_task_7(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '7\n' +
                '0 2 1 2 0 0 1',
                '0 0 0 1 1 2 2'
            ),

            (
                '5\n' +
                '2 1 2 0 1',
                '0 1 1 2 2'
            ),

            (
                '6\n' +
                '2 1 1 2 0 2',
                '0 1 1 2 2 2'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_7', inp.split('\n'), task_7_main, res
            )

    def test_task_8(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '3\n' +
                '15 56 2',
                '56215'
            ),

            (
                '3\n' +
                '1 783 2',
                '78321'
            ),

            (
                '5\n' +
                '2 4 5 2 10',
                '542210'
            ),

            (
                '38\n' +
                '82 58 66 34 64 37 40 97 93 52 28 98 90 64 19 22 21 83 ' +
                '56 70 46 17 31 51 55 41 68 18 98 89 88 74 6 6 31 36 35 8',
                '98989793908988883827470686666646458565552514641403736353' +
                '43131282221191817'
            ),

            (
                '6\n' +
                '9 10 1 1 1 6',
                '9611110'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_8', inp.split('\n'), task_8_main, res
            )

    def test_task_9(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '7\n' +
                '1 2 3 1 2 3 4\n' +
                '3',
                '1 2 3'
            ),

            (
                '6\n' +
                '1 1 1 2 2 3\n' +
                '1',
                '1'
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
                '5\n' +
                '4 3 9 2 1',

                '3 4 2 1 9\n' +
                '3 2 1 4 9\n' +
                '2 1 3 4 9\n' +
                '1 2 3 4 9\n'
            ),

            (
                '5\n' +
                '1 2 3 4 5',

                '1 2 3 4 5\n'
            ),

            (
                '5\n' +
                '12 8 9 10 11',

                '8 9 10 11 12\n'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_10', inp.split('\n'), task_10_main, res
            )

    def test_task_11(self):
        merge_tests: Tuple[
            Tuple[Tuple[List[int], int, int, int], List[int]]
            ] = (
            (
                ([1, 4, 9, 2, 10, 11], 0, 3, 6),
                [1, 2, 4, 9, 10, 11]
            ),
        )
        for (a, left, mid, right), res in merge_tests:
            with self.subTest():
                temp = task_11_merge(a, left, mid, right)
                self.assertEqual(temp, res)

        merge_sort_tests: Tuple[
            Tuple[Tuple[List[int], int, int], List[int]]
            ] = (
            (
                ([1, 4, 2, 10, 1, 2], 0, 6),
                [1, 1, 2, 2, 4, 10]
            ),
        )
        for (a, left, right), res in merge_sort_tests:
            with self.subTest():
                task_11_merge_sort(a, left, right)
                self.assertEqual(a, res)

    def test_task_12(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '6\n' +
                '1 2 4 4 6 8\n' +
                '3',
                '3 5'
            ),

            (
                '7\n' +
                '1 1 4 4 4 4 8\n' +
                '4',
                '3 7'
            ),

            (
                '6\n' +
                '1 1 4 4 4 4\n' +
                '1',
                '1 3'
            ),

            (
                '6\n' +
                '1 2 4 4 4 4\n' +
                '3',
                '3 -1'
            ),

            (
                '6\n' +
                '1 2 4 4 4 4\n' +
                '10',
                '-1 -1'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_12', inp.split('\n'), task_12_main, res
            )

    def test_task_13(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (
            (
                '10\n' +
                '2\n' +
                '3 4 5 6 7 8 9 10 11 12\n' +
                '1 2',
                '6.5'
            ),

            (
                '2\n' +
                '1\n' +
                '1 3\n' +
                '2',
                '2'
            ),

            (
                '2\n' +
                '2\n' +
                '1 2\n' +
                '3 4',
                '2.5'
            ),

            (
                '8\n' +
                '10\n' +
                '0 0 0 1 3 3 5 10\n' +
                '4 4 5 7 7 7 8 9 9 10',
                '5.0'
            ),

            (
                '72\n' +
                '8\n' +
                '0 0 3 3 3 6 6 7 7 10 11 14 15 15 16 16 ' +
                '18 20 21 23 23 26 30 32 35 36 38 39 40 ' +
                '42 44 48 48 50 50 50 52 53 55 57 58 58 ' +
                '59 60 60 66 66 67 68 68 69 70 74 76 76 ' +
                '77 78 80 83 83 83 84 86 87 88 88 90 95 ' +
                '96 96 99 100\n' +
                '7 24 33 43 54 78 80 85',
                '51.0'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_13', inp.split('\n'), task_13_main, res
            )

    def test_task_14(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (

            (
                '4\n' +
                '7 8\n' +
                '7 8\n' +
                '2 3\n' +
                '6 10',
                '2 3\n' +
                '6 10\n'
            ),

            (
                '4\n' +
                '2 3\n' +
                '5 6\n' +
                '3 4\n' +
                '3 4',
                '2 4\n' +
                '5 6\n'
            ),

            (
                '6\n' +
                '1 3\n' +
                '3 5\n' +
                '4 6\n' +
                '5 6\n' +
                '2 4\n' +
                '7 10',
                '1 6\n' +
                '7 10\n'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_14', inp.split('\n'), task_14_main, res
            )

    def test_task_15(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (

            (
                '3\n' +
                '2 3 4\n' +
                '2',
                '1'
            ),

            (
                '3\n' +
                '1 3 1\n' +
                '1',
                '0'
            ),

            (
                '3\n' +
                '1 3 5\n' +
                '3',
                '4'
            ),

            (
                '5\n' +
                '518494 998435 745611 280948 33981\n' +
                '7',
                '484513'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_15', inp.split('\n'), task_15_main, res
            )

    def test_task_16(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (

            (
                '4\n' +
                '0 1 3 2',
                '3\n'
            ),

            (
                '8\n' +
                '3 6 7 4 1 5 0 2',
                '1\n'
            ),

            (
                '5\n' +
                '1 0 2 3 4',
                '4\n'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_16', inp.split('\n'), task_16_main, res
            )

    def test_final_1(self):
        tests: Tuple[Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str],
                     Tuple[str, str]] = (
            (
                # first
                '9\n' +
                '19\n' +
                '19 21 100 101 1 4 5 7 12',

                '0'
            ),

            (
                # second
                '9\n' +
                '21\n' +
                '19 21 100 101 1 4 5 7 12',

                '1'
            ),

            (
                # mid
                '9\n' +
                '1\n' +
                '19 21 100 101 1 4 5 7 12',

                '4'
            ),

            (
                # after mid
                '9\n' +
                '4\n' +
                '19 21 100 101 1 4 5 7 12',

                '5'
            ),

            (
                # last
                '9\n' +
                '12\n' +
                '19 21 100 101 1 4 5 7 12',

                '8'
            ),

            (
                # absent
                '9\n' +
                '1000\n' +
                '19 21 100 101 1 4 5 7 12',

                '-1'
            ),

            (
                # first
                '9\n' +
                '12\n' +
                '12 19 21 100 101 1 4 5 7',

                '0'
            ),

            (
                # second
                '9\n' +
                '19\n' +
                '12 19 21 100 101 1 4 5 7',

                '1'
            ),

            (
                # mid
                '9\n' +
                '101\n' +
                '12 19 21 100 101 1 4 5 7',

                '4'
            ),

            (
                # after mid
                '9\n' +
                '1\n' +
                '12 19 21 100 101 1 4 5 7',

                '5'
            ),

            (
                # last
                '9\n' +
                '7\n' +
                '12 19 21 100 101 1 4 5 7',

                '8'
            ),

            (
                # absent
                '9\n' +
                '1000\n' +
                '12 19 21 100 101 1 4 5 7',

                '-1'
            ),

            (
                # first
                '8\n' +
                '12\n' +
                '12 19 21 100 101 1 4 5',

                '0'
            ),

            (
                # second
                '8\n' +
                '19\n' +
                '12 19 21 100 101 1 4 5',

                '1'
            ),

            (
                # after mid
                '8\n' +
                '4\n' +
                '12 19 21 100 101 1 4 5',

                '6'
            ),

            (
                # last
                '8\n' +
                '5\n' +
                '12 19 21 100 101 1 4 5',

                '7'
            ),

            (
                # absent
                '8\n' +
                '1000\n' +
                '12 19 21 100 101 1 4 5',

                '-1'
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
                '5\n' +
                'alla 4 100\n' +
                'gena 6 1000\n' +
                'gosha 2 90\n' +
                'rita 2 90\n' +
                'timofey 4 80',

                'gena\n' +
                'timofey\n' +
                'alla\n' +
                'gosha\n' +
                'rita\n'
            ),

            (
                '5\n' +
                'alla 0 0\n' +
                'gena 0 0\n' +
                'gosha 0 0\n' +
                'rita 0 0\n' +
                'timofey 0 0\n',

                'alla\n' +
                'gena\n' +
                'gosha\n' +
                'rita\n' +
                'timofey\n'
            ),

            (
                '5\n' +
                'gosha 0 0\n' +
                'alla 0 0\n' +
                'rita 0 0\n' +
                'gena 0 0\n' +
                'timofey 0 0\n',

                'alla\n' +
                'gena\n' +
                'gosha\n' +
                'rita\n' +
                'timofey\n'
            ),
        )
        for inp, res in tests:
            self._assert_correct_output(
                inp, 'final_2', inp.split('\n'), final_2_main, res
            )


if __name__ == '__main__':
    unittest.main()
