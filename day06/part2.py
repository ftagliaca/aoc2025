from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_numbers_split_2d(s: str) -> list[list[int]]:
    s_split = s.splitlines()
    line_len = len(s_split[0])
    n_rows = len(s_split) - 1
    nums = []
    nums_col = []
    for i in range(line_len - 1, -1, -1):
        num = 0
        for j in range(n_rows):
            if (n := s_split[j][i]) != ' ':
                if num == 0:
                    num = int(n)
                else:
                    num = int(n) + (num * 10)
        if num == 0:
            nums.append(nums_col)
            nums_col = []
        else:
            nums_col.append(num)
    if len(nums_col) > 0:
        nums.append(nums_col)
    return nums

def compute(s: str) -> int:
    numbers = parse_numbers_split_2d(s)
    ops = s.splitlines()[-1].split()
    ops = ops[::-1]
    # print(numbers)
    # print(ops) 
    grand_total = 0
    for number_set, op in zip(numbers, ops):
        if op == '*':
            op_tot = 1
            for n in number_set:
                op_tot *= n
            grand_total += op_tot    
        elif op == '+':
            grand_total += sum(number_set)

    return grand_total


INPUT_S = '''\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
'''
EXPECTED = 3263827


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
