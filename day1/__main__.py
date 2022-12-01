from utils import get_puzzle_input_for_day, group_input_by_blank_lines, int_transformer


def parse_input(input: str) -> list:
    return [
        int_transformer(g) for g in group_input_by_blank_lines(input)
    ]  # calories by elf


def sum_each(elf_calories: list) -> list:
    return [sum(cals) for cals in elf_calories]


def part1(input: str) -> int:
    return max(sum_each(parse_input(input)))


def part2(input: str) -> int:
    return sum(sorted(sum_each(parse_input(input)), reverse=True)[:3])


if __name__ == "__main__":
    test_input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
    assert part1(test_input) == 24000
    assert part2(test_input) == 45000

    puzzle_input = get_puzzle_input_for_day(1)
    print(f"Part 1:\t{part1(puzzle_input)}")
    print(f"Part 2:\t{part2(puzzle_input)}")
