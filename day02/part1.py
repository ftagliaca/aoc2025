from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_data(s: str) -> list[tuple[int, int]]:
    ranges = []
    for part in s.split(','):
        a, b = part.split('-')
        ranges.append((int(a), int(b)))
    return ranges

def generate_invalid():
    pass

def is_invalid(n: int) -> bool:
    ns = str(n)
    if len(ns) % 2 != 0:
        return False
    half = len(ns) // 2
    return ns[:half] == ns[half:]
    

def compute(s: str) -> int:
    ranges = parse_data(s)
    sum_invalid = 0
    for r_start, r_stop in ranges:
        for n in range(r_start, r_stop + 1):
            if is_invalid(n):
                sum_invalid += n
    
    return sum_invalid


INPUT_S = '''\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
'''
EXPECTED = 1227775554


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
