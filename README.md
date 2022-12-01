# Advent of Code 2022

## Solutions

Solutions are in `__main__py` files so if you want to run my solutions, use `python3 -m`
(ex.: `python3 -m day1`).

- [Day 1](day1/README.md)

## Utilities

👀 Check out [`utils.py`](utils.py) &mdash; you might find something useful in there.
Probably the most useful function is `get_puzzle_input_for_day` which will download your
puzzle input for you and return a string. It requires a bit of setup though (instructions below).

### Setup for `get_puzzle_input_for_day`

1. Log into Advent of Code and copy your session cookie from the browser (Dev
   Tools > Application > Storage > Cookies. Then copy the value of the cookie named
   `session`).
1. Make a copy `example_env.py` and name it `env.py`.
1. Replace the `SESSION` variable in `env.py` with the session cookie you
   copied.

...or, if you're lazy, just replace **line 21** in `utils.py` with `SESSION = <your session cookie>`.
