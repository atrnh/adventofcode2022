""" utils.py

How to use `get_puzzle_input_for_day`:

1. Log into Advent of Code and copy your session cookie from the browser (Dev
   Tools > Application > Storage > Cookies > Copy the value of the cookie named
   "session").
2. Make a copy `example_env.py` and name it `env.py`.
3. Replace the `SESSION` variable in `env.py` with the session cookie you
   copied.

...or, if you're lazy, just replace `SESSION = None` with `SESSION = <your session cookie>`.
"""

from typing import Optional, Tuple
from urllib import request

try:
    from env import SESSION
except ModuleNotFoundError:
    SESSION = None
    print("HEY, so you probably want to create an env.py file")

AOC_URL = "https://adventofcode.com/2022"


def build_aoc_request(url: str, session: Optional[str] = None) -> request.Request:
    return request.Request(url, headers={"Cookie": f"session={session}"})


def get_puzzle_input_for_day(day: int) -> str:
    req = build_aoc_request(f"{AOC_URL}/day/{day}/input", session=SESSION)
    res = request.urlopen(req)

    puzzle_input = res.read().decode("utf-8")

    return puzzle_input[:-1]  # remove trailing newline


def group_input_by_blank_lines(input: str) -> List[Tuple[str, str]]:
    return [tuple(group.split("\n")) for group in input.split("\n\n")]


def int_transformer(seq):
    return type(seq)([int(x) for x in seq])
