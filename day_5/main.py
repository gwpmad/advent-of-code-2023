from typing import Tuple, TypedDict

from utils import open_file


def solution():
    values = open_file("5").split("\n\n")
    solution_1 = __solution_1(values)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)


def get_slices_from_two_ranges(stage_map: Tuple[int, int], seed_range: Tuple[int, int]):
    below_stage_map = list(filter(lambda x: x < stage_map[0], seed_range))
    if len(below_stage_map) == 1:
        below_stage_map.append(stage_map[0])
    above_stage_map = list(filter(lambda x: x > stage_map[1], seed_range))
    if len(above_stage_map) == 1:
        above_stage_map.insert(0, stage_map[1])
    inside_stage_map = [
        below_stage_map[1] if len(below_stage_map) else seed_range[0],
        above_stage_map[0] if len(above_stage_map) else seed_range[1],
    ]
    if inside_stage_map[0] == inside_stage_map[1]:
        inside_stage_map = []
    return (tuple(below_stage_map), tuple(inside_stage_map), tuple(above_stage_map))


class StageMap(TypedDict):
    range: Tuple[int, int]
    difference: int


def get_stages(values: list[str]) -> list[list[StageMap]]:
    stages = []
    for maps in values[1:]:
        stage = []
        for line in maps.split("\n")[1:]:
            ints = list(map(int, line.split()))
            stage_map = {
                "range": (ints[1], ints[1] + ints[2]),
                "difference": ints[1] - ints[0],
            }
            stage.append(stage_map)
        stages.append(stage)
    return stages


def get_lowest_lower_bound_from_tuples(tuples):
    return min(tuples, key=lambda x: x[0])[0]


def transform_seed_ranges_to_location_ranges(
    stages: list[list[StageMap]], seed_ranges: list[Tuple[int, int]]
) -> list[Tuple[int, int]]:
    for stage in stages:
        seed_ranges_for_next_stage = []
        for stage_map in stage:
            temp_next_stage_map_seed_ranges = []
            for seed_range in seed_ranges:
                (below, inside, above) = get_slices_from_two_ranges(
                    stage_map["range"], seed_range
                )
                if len(below):
                    temp_next_stage_map_seed_ranges.append(below)
                if len(above):
                    temp_next_stage_map_seed_ranges.append(above)
                if len(inside):
                    seed_ranges_for_next_stage.append(
                        (
                            inside[0] - stage_map["difference"],
                            inside[1] - stage_map["difference"],
                        )
                    )
            seed_ranges = temp_next_stage_map_seed_ranges
        seed_ranges.extend(seed_ranges_for_next_stage)
    return seed_ranges


def get_seed_ranges_from_seed_line(seed_line: str) -> list[Tuple[int, int]]:
    seeds_list = list(map(int, seed_line.split()[1:]))
    seed_ranges = []
    for i in range(0, len(seeds_list), 2):
        seed_ranges.append((seeds_list[i], seeds_list[i] + seeds_list[i + 1]))
    return seed_ranges


def __solution_1(values: list[str]):
    stages = get_stages(values)
    seeds_list = list(map(int, values[0].split()[1:]))
    seed_ranges = list(map(lambda x: (x, x + 1), seeds_list))
    location_ranges = transform_seed_ranges_to_location_ranges(stages, seed_ranges)
    return get_lowest_lower_bound_from_tuples(location_ranges)


def __solution_2(values: list[str]):
    stages = get_stages(values)
    seed_ranges = get_seed_ranges_from_seed_line(values[0])
    location_ranges = transform_seed_ranges_to_location_ranges(stages, seed_ranges)
    return get_lowest_lower_bound_from_tuples(location_ranges)
