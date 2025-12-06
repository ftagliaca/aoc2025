from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def check_overlap(r1: tuple[int, int], r2: tuple[int, int]) -> bool:
    if r1[0] > r2[1] or r2[0] > r1[1]:
        return False
    return True    

def merge_overlap(r1: tuple[int, int], rs: list[tuple[int,int]]) -> list[tuple[int, int]]:
    # 1. Check if given range overlaps with any of the ranges in list
    # print(f'Checking range: {r1}')
    overlap_found = False
    for i, r in enumerate(rs):
        # print(f'  Against range: {r}')
        if check_overlap(r1, r):
            # print('    Overlap found, merging')
            new_start = min(r1[0], r[0])
            new_end = max(r1[1], r[1])
            rs[i] = (new_start, new_end)
            overlap_found = True
            # print(f'    Merged range: {rs[i]}')
            
    if not overlap_found:
        # print('    No overlap found, adding new range')
        rs.append(r1)
            
    return rs
            

def compute(s: str) -> int:
    r, _ = support.parse_blocks(s)
    ranges = support.parse_numbers_couple_split(r)
    ranges = sorted(ranges, key=lambda x: x[0])

    ranges_merged = []
    for r in ranges:
        merge_overlap(r, ranges_merged)
    fresh_ids = 0
    for r in ranges_merged:
        fresh_ids += r[1] - r[0] + 1
    return fresh_ids

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
EXPECTED = 14



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
