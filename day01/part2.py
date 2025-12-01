from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def parse_data(s: str) -> list[int]:
    l = []
    for line in s.split("\n"):
        if line:
            mul = 1 if line.startswith("R") else -1
            l.append(mul * int(line[1:]))
    return l


def compute(s: str) -> int:
    pswd = 0
    start = 50
    numbers = parse_data(s)
    for n in numbers:
        # print("=" * 30)
        # print(f"At {start}")
        # print(f"Moving by {n}")
        new = start + n
        # print(f"Ended at {new}")
        add = abs(new // 100)
        if (start == 0) and (new < 0):
            add -= 1
        if new == 0:
            add += 1
        if (n < -100) and (new % 100 == 0):
            add += 1
        # print(f"Passed by 100 {add}")
        pswd += add
        start = new % 100
    return pswd


INPUT_S = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
EXPECTED = 6


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
