import copy

from utils import open_file


def solution():
    values = open_file("14").split("\n")
    solution_1 = __solution_1(values)
    print('solution_1 still right', solution_1 == 136)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)


def __solution_1(rocks: list[str]):
    transposed_rocks = [[*list(tup),'#'] for tup in (zip(*rocks[::-1]))]
    
    return sum([_get_load_for_line(line) for line in transposed_rocks])

def _get_load_for_line(line: list[str]) -> int:
    sub_sums = []
    num_circular_rocks = 0
    for idx, space in enumerate(line):
        current_load = idx + 1
        if space == "O":
            num_circular_rocks += 1
        if space == '#' and num_circular_rocks > 0:
            sub_sum = sum(range(current_load - num_circular_rocks, current_load))
            sub_sums.append(sub_sum)
            num_circular_rocks = 0
    return sum(sub_sums)

def __solution_2(rocks: list[str]):
    used_strings = []
    cycles = 1000000000
    idx = 0
    cycles_for_loop = 0
    while idx < cycles:
        rocks = _tilt_north(rocks)
        rocks = _tilt_west(rocks)
        rocks = _tilt_south(rocks)
        rocks = _tilt_east(rocks)
        if cycles_for_loop == 0:
            rocks_string = ''.join(rocks)
            if rocks_string in used_strings:
                repeated_from_idx = used_strings.index(rocks_string)
                cycles_for_loop = idx - repeated_from_idx
                # idx = (cycles + repeated_from_idx + 1) - (cycles_for_loop * (repeated_from_idx + 1))
                # idx += cycles_for_loop * ((cycles - idx) // cycles_for_loop)
                #         cycle += cycle_length * ((goal - cycle) // cycle_length)
                # cycles -= repeated_from_idx
                # new_idx = ((cycles // cycles_for_loop) * cycles_for_loop)
                # while new_idx > cycles:
                #     new_idx -= cycles_for_loop
                # idx = new_idx
                # continue
            else:
                used_strings.append(rocks_string)
        idx += 1
    transposed_rocks = [[*list(tup),'#'] for tup in (zip(*rocks[::-1]))]
    return sum([_get_load_for_line(list(line)) for line in transposed_rocks])

# 13 - (13 // 3) + 2
def _tilt_line(line: str) -> str:
    split_by_hash = line.split('#')
    return '#'.join([''.join(sorted(part)) for part in split_by_hash])

def _tilt_east(rocks: list[str],) -> list[str]: # works as tilt_east
    return [_tilt_line(line) for line in rocks]

def _transpose_rocks_90_to_right(rocks: list[str]) -> list[str]:
    return [''.join(tup) for tup in (zip(*rocks[::-1]))]

def _transpose_rocks_90_to_left(rocks: list[str]) -> list[str]:
    return [''.join(tup) for tup in zip(*rocks)][::-1]

def _tilt_north(rocks: list[str]) -> list[str]:
    transposed = _transpose_rocks_90_to_right(rocks)
    tilted = _tilt_east(transposed)
    return _transpose_rocks_90_to_left(tilted)

def _tilt_south(rocks: list[str]) -> list[str]:
    transposed = _transpose_rocks_90_to_left(rocks)
    tilted = _tilt_east(transposed)
    return _transpose_rocks_90_to_right(tilted)

def _tilt_west(rocks: list[str]) -> list[str]:
    tranposed_180 = _transpose_rocks_90_to_left(_transpose_rocks_90_to_left(rocks))
    tilted = _tilt_east(tranposed_180)
    return _transpose_rocks_90_to_right(_transpose_rocks_90_to_right(tilted))

# def _tilt_east(rocks: list[str]) -> list[str]:
#     tranposed_90 = _transpose_rocks_90_to_left(rocks)
#     tranposed_180 = _transpose_rocks_90_to_left(tranposed_90)
#     all_strings_reversed = list(reversed([line[::-1] for line in tranposed_180]))
#     tilted = _tilt_to_the_right(all_strings_reversed)
#     tilted_unreversed = list(reversed([line[::-1] for line in tilted]))
#     return _transpose_rocks_90_to_right(_transpose_rocks_90_to_right(tilted_unreversed))
