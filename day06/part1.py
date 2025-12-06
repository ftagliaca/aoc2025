from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_numbers_split_2d(s: str) -> list[list[int]]:
    return [[int(i) for i in x.split()]for x in s.splitlines()[:-1]]

def compute(s: str) -> int:
    numbers = parse_numbers_split_2d(s)
    numbers = list(zip(*numbers))
    ops = s.splitlines()[-1].split()
    
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
EXPECTED = 4277556


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
