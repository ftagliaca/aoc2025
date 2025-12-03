from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def get_max_joltage(s: str, n: int) -> int:
    l = list(s)
    digits = []
    start_index = 0
    max_index = len(l) - n + 1
    # print(l)
    for _ in range(n):
        # print(f'Start: d: {digits}, start_index: {start_index}, max_index: {max_index}')
        digits.append(max(l[start_index:max_index]))
        start_index = l[start_index:].index(digits[-1]) + 1 + start_index
        max_index += 1
        # print(f'End:   d: {digits}, start_index: {start_index}, max_index: {max_index}')
    # print(digits)
    return int(''.join(digits))

def compute(s: str) -> int:
    total_joltage = 0
    for l in s.splitlines():
        total_joltage += get_max_joltage(l, 12)

    return total_joltage


INPUT_S = '''\
987654321111111
811111111111119
234234234234278
818181911112111
'''
EXPECTED = 3121910778619


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
