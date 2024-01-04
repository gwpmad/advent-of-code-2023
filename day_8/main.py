import json
from math import lcm
from typing import Tuple, cast

from utils import open_file


def solution():
    values = open_file("8").split("\n\n")
    instructions, locations_map = get_instructions_and_locations_map(values)
    solution_1 = __solution_1(instructions, locations_map)
    solution_2 = __solution_2(instructions, locations_map)
    return (solution_1, solution_2)


def get_instructions_and_locations_map(
    values: list[str],
) -> Tuple[list[int], dict[str, list[str]]]:
    instructions = list(map(int, list(values[0].translate(str.maketrans("LR", "01")))))
    locations_map = json.loads(
        (
            '{"'
            + values[1].translate(
                str.maketrans(
                    {
                        "=": '":',
                        "(": '["',
                        ")": '"]',
                        ",": '","',
                        "\n": ',\n"',
                        " ": None,
                    }
                )
            )
            + "}"
        )
    )
    return instructions, locations_map


def __solution_1(instructions: list[int], locations_map: dict[str, list[str]]):
    counter = 0
    key = "AAA"
    while key != "ZZZ":
        idx = instructions[counter % len(instructions)]
        key = locations_map[key][idx]
        counter += 1
    return counter


def __solution_2(instructions: list[int], locations_map: dict[str, list[str]]):
    # The node after nodes ending in A is the same as after the related node ending in Z.
    keys = [key for key in locations_map.keys() if key.endswith("A")]
    intervals: list[None | int] = [None] * len(keys)

    counter = 0
    while not all(intervals):
        idx = int(instructions[counter % len(instructions)])
        keys = [locations_map[key][idx] for key in keys]

        counter += 1
        indexes_with_z_end = [idx for idx, key in enumerate(keys) if key.endswith("Z")]
        if len(indexes_with_z_end):
            for i in indexes_with_z_end:
                if not intervals[i]:
                    intervals[i] = counter

    return lcm(*cast(list[int], intervals))
