from collections import deque
from itertools import islice

from utils import get_puzzle_input_for_day


def sliding_window(iterable, size):
    it = iter(iterable)
    window = deque(islice(it, size), maxlen=size)

    if len(window) == size:
        yield tuple(window)

    for elem in it:
        window.append(elem)
        yield tuple(window)


def get_chars_until_start_of_packet(stream, packet_size=4):
    chars_seen = packet_size
    for chars in sliding_window(stream, packet_size):
        if len(set(chars)) == packet_size:
            return chars_seen

        chars_seen += 1


def part1(puzzle_input):
    return get_chars_until_start_of_packet(puzzle_input, packet_size=4)


def part2(puzzle_input):
    return get_chars_until_start_of_packet(puzzle_input, packet_size=14)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input_for_day(6)

    print(f"Part 1:\t{part1(puzzle_input)}")
    print(f"Part 2:\t{part2(puzzle_input)}")
