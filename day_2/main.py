import re

from utils import open_file


def solution():
    values = open_file("2").split("\n")
    solution_1 = __solution_1(values)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)


def __solution_1(values: list[str]) -> int:
    games = set(range(1, len(values) + 1))
    red_max = 12
    green_max = 13
    blue_max = 14

    for idx, line in enumerate(values):
        is_impossible = (
            game_impossible_for_colour(line, "red", red_max)
            or game_impossible_for_colour(line, "blue", blue_max)
            or game_impossible_for_colour(line, "green", green_max)
        )
        if is_impossible:
            games.remove(idx + 1)

    return sum(games)


def __solution_2(values: list[str]):
    answer = 0
    for line in values:
        max_red = get_numbers_for_colour(line, "red")[-1]
        max_green = get_numbers_for_colour(line, "green")[-1]
        max_blue = get_numbers_for_colour(line, "blue")[-1]
        answer += max_red * max_green * max_blue

    return answer


def game_impossible_for_colour(string: str, colour: str, max: int):
    numbers = get_numbers_for_colour(string, colour)
    return any(x > max for x in numbers)


def get_numbers_for_colour(string: str, colour: str) -> list[int]:
    match = re.findall(rf"\d+(?=\s{colour})", string)
    return sorted([int(x) for x in match])
