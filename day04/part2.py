from __future__ import annotations

import argparse
import os.path
import numpy as np
import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def is_accessible(grid: list[list[bool]], x: int, y: int) -> bool:
    adj = 0
    for x,y in support.adjacent_8(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            if grid[x][y]:
                adj += 1
        if adj >= 4:
            return False
    return True

def compute(s: str) -> int:
    grid = support.parse_grid(s, {'@': True, '.': False})
    accessible = 0
    found = True
    while found:
        found = False
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val:
                    if is_accessible(grid, x, y):
                        grid[x][y] = False
                        found = True
                        accessible += 1
    return accessible


INPUT_S = '''\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
'''
EXPECTED = 43


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
