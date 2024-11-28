from functools import reduce

from utils import open_file


def solution():
    values = open_file("16").split("\n")
    solution_1 = __solution_1(values)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)


class BeamState:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.location = f"{x},{y}"
        self.direction = direction
        self.loc_dir_combo = f"{self.location},{direction}"


def __solution_1(grid: list[str]):
    x_max = len(grid[0]) - 1
    y_max = len(grid) - 1
    tiles_energised = set[str]()
    previous_loc_dir_combos = set[str]()
    queue: list[BeamState] = [BeamState(x=0, y=0, direction="R")]
    while len(queue):
        beam_state = queue.pop(0)
        tiles_energised.add(beam_state.location)
        previous_loc_dir_combos.add(beam_state.loc_dir_combo)
        queue.extend(
            _get_new_beam_states(
                beam_state,
                previous_loc_dir_combos,
                x_max,
                y_max,
                current_grid_value=grid[beam_state.y][beam_state.x],
            )
        )

    return len(tiles_energised)


def _get_new_beam_states(
    current_beam_state: BeamState,
    previous_loc_dir_combos: set[str],
    x_max: int,
    y_max: int,
    current_grid_value: str,
) -> list[BeamState]:
    def _maybe_create_new_beam_state(
        acc: list[BeamState], direction: str
    ) -> list[BeamState]:
        (x, y) = direction_to_location(
            direction, (current_beam_state.x, current_beam_state.y)
        )
        new_beam_state = BeamState(x, y, direction)
        if not (
            _beam_has_left_grid((new_beam_state.x, new_beam_state.y), x_max, y_max)
            or new_beam_state.loc_dir_combo in previous_loc_dir_combos
        ):
            acc.append(new_beam_state)
        return acc

    return reduce(
        _maybe_create_new_beam_state,
        _direction_mirror_lookup[current_beam_state.direction][current_grid_value],
        [],
    )


_direction_mirror_lookup = {
    "R": {
        "/": ["U"],
        "\\": ["D"],
        "|": ["U", "D"],
        "-": ["R"],
        ".": ["R"],
    },
    "L": {
        "/": ["D"],
        "\\": ["U"],
        "|": ["U", "D"],
        "-": ["L"],
        ".": ["L"],
    },
    "U": {
        "/": ["R"],
        "\\": ["L"],
        "|": ["U"],
        "-": ["L", "R"],
        ".": ["U"],
    },
    "D": {
        "/": ["L"],
        "\\": ["R"],
        "|": ["D"],
        "-": ["L", "R"],
        ".": ["D"],
    },
}


def direction_to_location(
    direction: str, current_coords: tuple[int, ...]
) -> tuple[int, ...]:
    (x, y) = current_coords
    match direction:
        case "R":
            return (x + 1, y)
        case "L":
            return (x - 1, y)
        case "U":
            return (x, y - 1)
        case "D":
            return (x, y + 1)
        case _:
            raise ValueError(f"Invalid direction: {direction}")


def _beam_has_left_grid(new_coords: tuple[int, ...], x_max: int, y_max: int) -> bool:
    (x, y) = new_coords
    return x < 0 or y < 0 or x > x_max or y > y_max


def __solution_2(values: list[str]):
    return None
