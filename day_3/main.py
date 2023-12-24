import re
from typing import Dict, Iterator, Match, Tuple

from utils import open_file


def solution():
    input = open_file("3")
    solution_1 = __solution_1(input)
    solution_2 = __solution_2(input)
    return (solution_1, solution_2)


def get_symbol_positions(input: str) -> set[int]:
    symbols = re.finditer(r"[^\d\n\.]", input)
    return set([x.start() for x in symbols])


def get_star_positions(input: str) -> set[int]:
    symbols = re.finditer(r"\*", input)
    return set([x.start() for x in symbols])


def __solution_1(input: str):
    line_length = input.find("\n")
    symbol_positions = get_symbol_positions(input)
    numbers = re.finditer(r"\d+", input)
    part_numbers = get_part_numbers(numbers, symbol_positions, line_length)
    return sum(part_numbers)


def __solution_2(input: str):
    line_length = input.find("\n")
    numbers = re.finditer(r"\d+", input)
    star_positions = get_star_positions(input)
    stars_with_number_info = get_stars_with_number_info(
        numbers, star_positions, line_length
    )
    return get_sum_of_gear_ratios(stars_with_number_info)


def get_sum_of_gear_ratios(stars_with_number_info: Dict[int, list[int]]) -> int:
    sum = 0
    for _, number_info in stars_with_number_info.items():
        if len(number_info) == 2:
            sum += number_info[0] * number_info[1]
    return sum


def get_stars_with_number_info(
    numbers: Iterator[Match[str]], star_positions: set[int], line_length: int
) -> Dict[int, list[int]]:
    stars_with_number_info = {}
    for number in numbers:
        surrounding_positions = get_surrounding_positions(number.span(), line_length)
        surrounding_stars = star_positions.intersection(surrounding_positions)
        for star_position in surrounding_stars:
            if star_position in stars_with_number_info:
                stars_with_number_info[star_position].append(int(number.group()))
            else:
                stars_with_number_info[star_position] = [int(number.group())]

    return stars_with_number_info


def get_surrounding_positions(span: Tuple[int, int], line_length: int) -> list[int]:
    max_length_away = line_length + 2
    return (
        [*range(span[0] - max_length_away, span[1] - line_length)]
        + [span[0] - 1, span[1]]
        + [*range(span[0] + line_length, span[1] + max_length_away)]
    )


def get_part_numbers(
    numbers: Iterator[Match[str]], symbol_positions: set[int], line_length: int
) -> list[int]:
    part_numbers = list()
    for number in numbers:
        surrounding_positions = get_surrounding_positions(number.span(), line_length)
        for position in surrounding_positions:
            if position in symbol_positions:
                part_numbers.append(int(number.group()))
                break

    return part_numbers


# 24-25 has 12 13 14 15 23 26 34 35 36 37
# initial-12 -> final-10
# initial-1
# final+1
# initial+10 -> final+12
