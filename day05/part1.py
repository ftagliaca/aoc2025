from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def is_fresh(available_id: int, ranges: list[range]) -> bool:
    for r in ranges:
        if available_id in r:
            return True
    return False

def compute(s: str) -> int:
    r, d = support.parse_blocks(s)
    ranges = support.parse_numbers_couple_split(r)
    availabe_ids = support.parse_numbers_split(d)

    fresh_ranges = []
    for range_start, range_end in ranges:
        fresh_ranges.append(range(range_start, range_end + 1))
    fresh_ids = []
    for aid in availabe_ids:
        if is_fresh(aid, fresh_ranges):
            fresh_ids.append(aid)
    
    # fresh_availabe = availabe_ids_set.intersection(fresh_ranges)
    return len(fresh_ids)


INPUT_S = '''\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''
EXPECTED = 3



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
