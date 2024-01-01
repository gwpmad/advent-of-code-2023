from functools import reduce
from math import ceil, floor
from typing import TypedDict

from sympy import symbols
from sympy.solvers import solve

from utils import open_file


def solution():
    values = open_file("6").split("\n")
    solution_1 = __solution_1(values)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)


class Game(TypedDict):
    time: int
    record: int


def __get_single_game(values: list[str]) -> Game:
    ints = list(map(lambda line: int("".join(line.split()[1:])), values))
    return {"time": ints[0], "record": ints[1]}


def __get_games(values: list[str]) -> list[Game]:
    numbers = list(map(lambda line: list(map(int, line.split()[1:])), values))
    return list(
        map(
            lambda i: {"time": numbers[0][i], "record": numbers[1][i]},
            range(0, len(numbers[0])),
        )
    )


def get_ints_between_solutions_for_record(game):
    x = symbols("x")
    min_max_for_record = solve(
        ((game["time"] - x) * x) - game["record"], x
    )  # from here: https://docs.sympy.org/latest/tutorials/intro-tutorial/solvers.html#a-note-about-equations
    return ceil(float(min_max_for_record[1])) - floor(float(min_max_for_record[0])) - 1


def __solution_1(values: list[str]):
    def multiply_solutions(product, game):
        return product * get_ints_between_solutions_for_record(game)

    return reduce(multiply_solutions, __get_games(values), 1)


def __solution_2(values: list[str]):
    return get_ints_between_solutions_for_record(__get_single_game(values))
