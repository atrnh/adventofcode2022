import re
from copy import deepcopy
from utils import get_puzzle_input_for_day

box_contents_re = r"\[(\w)\]"
move_re = r"move (\d*) from (\d*) to (\d*)"


def get_boxconfig_and_moves(input):
    return input.rstrip().split("\n\n")


def boxconfig_tokenizer(line):
    for i in range(0, len(line), 4):
        yield line[i : i + 3]


def tokenize_boxconfig(boxconfig):
    return [
        [token for token in iter(boxconfig_tokenizer(line))]
        for line in boxconfig.split("\n")[
            :-1
        ]  # ditch last line, which is just the number assigned to each stack
    ]


def translate_box_token_to_letter(token):
    letter_match = re.search(r"\[(\w)\]", token)
    return letter_match[1] if letter_match else None


def parse_box_tokens(token_lines):
    return [
        [translate_box_token_to_letter(token) for token in line] for line in token_lines
    ]


def initialize_boxes(boxes_state):
    boxes = [[] for _ in range(len(boxes_state[0]))]
    for line in boxes_state:
        for i, letter in enumerate(line):
            if letter:
                boxes[i].append(letter)

    return [list(reversed(box)) for box in boxes]


def parse_move(move):
    move_match = re.search(move_re, move)
    if move_match:
        return (int(move_match[1]), int(move_match[2]), int(move_match[3]))


def pop_n(n, stack):
    return [stack.pop() for _ in range(n)]


def pop_chunk(n, stack):
    return reversed(pop_n(n, stack))


def part1(moves, boxes):
    for n, from_, to in moves:
        boxes[to - 1].extend(pop_n(n, boxes[from_ - 1]))

    return "".join([box[-1] for box in boxes])


def part2(moves, boxes):
    for n, from_, to in moves:
        boxes[to - 1].extend(pop_chunk(n, boxes[from_ - 1]))

    return "".join([box[-1] for box in boxes])


if __name__ == "__main__":
    puzzle_input = get_puzzle_input_for_day(5)

    boxconfig, move_instructions = get_boxconfig_and_moves(puzzle_input)
    initial_boxes_state = parse_box_tokens(tokenize_boxconfig(boxconfig))

    boxes = initialize_boxes(initial_boxes_state)
    moves = [parse_move(line) for line in move_instructions.rstrip().split("\n")]

    print(f"Part 1:\t{part1(moves, deepcopy(boxes))}")
    print(f"Part 2:\t{part2(moves, deepcopy(boxes))}")
